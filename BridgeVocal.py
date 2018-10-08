# -*- coding: utf-8 -*-

import threading, time
# import pygame
# from serial import *
# import math
# from numpy.linalg import inv
# import math
# import numpy
from BridgeConf import BridgeConfClass, BridgeClass, BridgeCoordClass
import scipy.io as spio
import winsound # per audio feedback

import speech_recognition as sr


class Thread_VocalControlClass(threading.Thread):
    def __init__(self, Bridge, Conf, Coord, Debug=False):

        threading.Thread.__init__(self)
        self.stop           = threading.Event()
        self.Conf           = Conf
        self.Coord          = Coord
        self.Bridge         = Bridge

        # variabili per il riconoscimento vocale
        self.r = sr.Recognizer()
        #self.r.energy_threshold = 4500
        self.r.dynamic_energy_threshold = False

        # variabili per il controllo dei cicli
        self.running_VocalControl = True
        self.running_2 = False
        self.running_3 = False
        self.c = 0

        # variabili per controllo "step"    
        self.Coord.steps = self.Coord.max_steps

        # variabili per la memorizzazione
        self.var_mem = ['','','','','']       
        self.NumVarMem = 0
        self.vm   = 4*[0]

        # dizionari
        self.instr_dict = {'fer':'fermo', 'rip':'riposo', 'mem':'memorizza', 'dor':'dormi'}
        self.direction_dict = {'sin':[-1,0,0,0], 'des':[1,0,0,0], 'sal':[0,0,-1,0], 'sce':[0,0,1,0], 'ava':[0,-1,0,0], 'ind':[0,1,0,0]}
        # self.step_dict = {'uno': 1, 'due': 2, 'tre':3, 'qua': 4, 'cin':5, 'sei':6, 'set':7, 'ott':8, 'nov':9, 'die':10}
        self.step_dict = {'spostamento picc': self.Conf.step_param[0], 'spostamento medi': self.Conf.step_param[1], 'spostamento gran':self.Conf.step_param[2]}

        self.Coord.p0 = [0, 0, 0, 0] # TODO rimuovere

    def run(self):

        print '* Start vocal control'

        " Introduzione controllo vocale "
        winsound.PlaySound('Jarvis.wav', winsound.SND_FILENAME)
        self.Bip()

        while self.running_VocalControl == True:

            print '*************************************************************'
            print "***   Per attivare il riconoscimento pronunciare JARVIS   ***"
            print "*** Per disattivare il riconoscimento pronunciare TERMINA ***"
            print '*************************************************************'
            
            jarvis = self.WaitForInstructions()           
            print jarvis
            " Check Allarme "
            if jarvis[0:4] == 'aiut':
                print '*** ALLARME!'
                self.Coord.VocalCtrlPos = 'aiuto'
                self.running_VocalControl = False
                self.running_2 = False
                self.running_3 = False


            #" Ciclo esterno per attivare/disattivare il controllo vocale + conferma "
            elif jarvis == 'Jarvis':
                winsound.PlaySound('ConfermaAttivazione.wav', winsound.SND_FILENAME)
                self.Bip()
                print '*** Mi hai chiamato? [Vero/Falso] ***'
                conf = self.WaitForInstructions()               
                print conf 
                
                if conf == 'vero' :
                    print '*** CONTROLLO VOCALE ATTIVATO ***'
                    self.Coord.VocalCtrlPos = 'schermata'
                    winsound.PlaySound('SonoAttivo.wav', winsound.SND_FILENAME)
                    self.Bip()
                    self.running_2 = True
                    self.c = 1

                elif conf == 'falso' :
                    winsound.PlaySound('Jarvis.wav', winsound.SND_FILENAME)
                    print '*** Sono in ascolto ***'
                    self.Bip()
                    self.c = 0

                elif conf[0:4] == 'aiut':
                    print '*** ALLARME!'
                    self.Coord.VocalCtrlPos = 'aiuto'
                    self.running_VocalControl = False
                    self.running_2 = False
                    self.running_3 = False

                else :                    
                    winsound.PlaySound('IstruzioneNonValida.wav', winsound.SND_FILENAME)
                    self.c = 0
                    self.Bip()

                " Ciclo interno in cui il programma riconosce i comandi "
                while self.running_2 == True and self.c == 1 :
                    print "*** Pronunciare un comando ***"
                    print "*** Per tornare in modalita' ascolto pronunciare DORMI ***"
                    
                    try:
                        instr = self.WaitForInstructions()                       
                        print instr
                        " Check Allarme "
                        if instr[0:4] == 'aiut':
                            print '*** ALLARME!'
                            self.Coord.VocalCtrlPos = 'aiuto'
                            self.running_VocalControl = False
                            self.running_2 = False
                            self.running_3 = False

                        else:

                            self.CommandRecognition(instr)

                            if self.Coord.VocalCtrlPos ==  'dormi':
                                winsound.PlaySound('Dormi.wav', winsound.SND_FILENAME)
                                self.Bip()
                                self.running_2 = False
                                self.c = 0

                            if self.Coord.VocalCtrlPos == 'memorizza':
                                winsound.PlaySound('Memorizza.wav', winsound.SND_FILENAME)
                                self.Bip()
                                self.running_3 = True

                                print '*** Vuoi memorizzare questa posizione come nuovo comando? [Vero/Falso] ***'
                                conf_memo = self.WaitForInstructions()                          
                                print conf_memo

                                if conf_memo == 'falso':
                                    self.running_3 = False
                                    self.Bip()

                                elif conf_memo == 'vero':
                                    self.Memorizza()

                                elif conf_memo[0:4] == 'aiut':
                                    print '*** ALLARME!'
                                    self.Coord.VocalCtrlPos = 'aiuto'
                                    self.running_VocalControl = False
                                    self.running_2 = False
                                    self.running_3 = False

                                else :
                                    self.running_3 = False
                                    self.Bip()

                        
                    except sr.UnknownValueError:
                        print '*** Scusa, non ho capito le tue istruzioni ***'
                        winsound.PlaySound('IstruzioneNonValida.wav', winsound.SND_FILENAME)
                        self.Bip()
            
            elif jarvis == 'termina':
                self.Coord.VocalCtrlPos = 'jarvis'
                winsound.PlaySound('ConfermaSpegnimento.wav', winsound.SND_FILENAME)
                self.Bip()

                print '*** Vuoi che mi spenga? [Vero/Falso] ***'
                conf_term = self.WaitForInstructions()

                if conf_term == 'vero':
                    print '*** Controllo vocale disattivato ***'
                    winsound.PlaySound('Spegnimento.wav', winsound.SND_FILENAME)

                    self.running_VocalControl = False
                    self.running_2 = False
                    self.running_3 = False

                elif conf_term == 'falso':
                    print '*** Resto in stand-by ***'
                    winsound.PlaySound('Dormi2.wav', winsound.SND_FILENAME)
                    self.c = 0
                else :
                    winsound.PlaySound('IstruzioneNonValida.wav', winsound.SND_FILENAME)
                    self.Bip()
                    self.c = 0
            else :
                print '*** Sono in ascolto ***' 
                self.Coord.VocalCtrlPos = 'jarvis'

    # funzione di riconoscimento dei comandi che può essere personalizzata -> custumizzazione
    def CommandRecognition(self, instr):

        if instr[0:3] in self.instr_dict:
            self.Coord.VocalCtrlPos = self.instr_dict[instr[0:3]]

        elif instr[0:3] in self.direction_dict:
            self.Coord.VocalCtrlPos = 'moving'
            self.Coord.p0 = self.direction_dict[instr[0:3]]
            self.Coord.countSteps = 0


        elif instr[0:16] in self.step_dict:
            self.Coord.steps = self.step_dict[instr[0:16]]
            print 'Numero di step selezionati: ', self.Coord.steps

        elif instr == self.var_mem[0]:
            print '*** Vado a',self.var_mem[0],'***'
            self.Coord.VocalCtrlPos = 'memo1'

        elif instr == self.var_mem[1]:
            print '*** Vado a',self.var_mem[1],'***'
            self.Coord.VocalCtrlPos = 'memo2'

        elif instr == self.var_mem[2]:
            print '*** Vado a',self.var_mem[2],'***'
            self.Coord.VocalCtrlPos = 'memo3'

        elif instr == self.var_mem[3]:
            print '*** Vado a',self.var_mem[3],'***'
            self.Coord.VocalCtrlPos = 'memo4'

        elif instr == self.var_mem[4]:
            print '*** Vado a',self.var_mem[4],'***'
            self.Coord.VocalCtrlPos = 'memo5'
       
        else :
            print '*** Istruzione non valida ***'
            print 'ZZZ'
            winsound.PlaySound('IstruzioneNonValida.wav', winsound.SND_FILENAME)
            self.Bip()

    def Memorizza(self):

        winsound.PlaySound('NomeNuovaPosizione.wav', winsound.SND_FILENAME)
        self.Bip()
        print '*** Dimmi come vuoi chiamare la nuova posizione ***'
        self.var = self.WaitForInstructions()                                
        print '*** Parola scelta : ', self.var,'***'

        if  self.var [0:3] == 'sin' or self.var [0:5] == 'destr' or self.var == 'salire' or self.var == 'scendere' or self.var [0:3] == 'ava' or self.var [0:3] == 'ind' or self.var [0:3] == 'rip' or self.var [0:4] == 'memo' or self.var == 'fermo' or self.var == 'dormi' or self.var == self.var_mem[0] or self.var == self.var_mem[1] or self.var == self.var_mem[2] or self.var == self.var_mem[3] or self.var == self.var_mem[4] or self.var[0:4] == 'aiut':
            print '*** Parola gia presente tra i comandi disponibili, pronunciare un nuovo comando ***'
            winsound.PlaySound('MancataMemo.wav', winsound.SND_FILENAME)
            self.Bip()

        else :
            check = 0
            for ii in range(0,4):
                if ii == 0:
                    winsound.PlaySound('RipetiNuovaPosizione1.wav', winsound.SND_FILENAME)
                else:
                    winsound.PlaySound('RipetiNuovaPosizione2.wav', winsound.SND_FILENAME)

                self.Bip()
                print '*** Ripeti la parola che hai scelto ***'
                self.vm[ii] = self.WaitForInstructions()
                print '*** Ripetizione ', ii+1 ,' :',self.vm[ii],'***'

                if self.var == self.vm[ii]:
                    check = check+1

            #CONFRONTO TRA LE RIPETIZIONI PER VERIFICARE SE SALVARE LA NUOVA VARIABILE               
            if check >= 3:
                self.var_mem[self.NumVarMem] = self.var
                print '*** Posizione memorizzata :',self.var_mem[self.NumVarMem],'***'
                winsound.PlaySound('NuovaPosizioneMemorizzata.wav', winsound.SND_FILENAME)
                self.Bip()

                self.NumVarMem = self.NumVarMem+1
                if self.NumVarMem > 5 :
                    self.NumVarMem = 1
                    print '*** Da questo momento le nuove posizioni verranno sovrascritte in ordine a partire dalla meno recente ***'
                    winsound.PlaySound('Sovrascrivere.wav', winsound.SND_FILENAME)
                    self.Bip()

            else:
                print '*** Non sono riuscito a salvare il nuovo comando ***'
                winsound.PlaySound('ImpossibileMemorizzare.wav', winsound.SND_FILENAME)
                self.Bip()

    def WaitForInstructions(self):
        with sr.Microphone() as source:
            cmd = self.r.listen(source)
            print '*** Ho sentito qualcosa... ***'
            self.Coord.p0 = [0, 0, 0, 0]
            # metto al massimo il numero di step fatti così interrompo il ciclo
            self.Coord.countSteps = self.Coord.steps
            try:
                instruction = self.r.recognize_google(cmd, language = "it-IT")
            except Exception as e:
                instruction = 'xxx'
                print '... Connection timeout'
            
            return instruction

    def Bip(self):
        Freq = 700 # Set Frequency To 2500 Hertz
        Dur = 950 # Set Duration To 1000 ms == 1 second
        winsound.Beep(Freq,Dur)

    def terminate(self):
        self.running_VocalControl == False



