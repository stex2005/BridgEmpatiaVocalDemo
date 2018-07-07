# -*- coding: utf-8 -*-

instr_dict = {'fer':'fermo', 'rip':'riposo', 'mem':'memorizza', 'dor':'dormi', 'sin':[0,0,0], 'des':'destra', \
    'sal':'salire', 'sce':'scendere', 'ava':'avanti', 'ind':'indietro'}
step_dict = {'uno': 1, 'due': 2, 'tre':3, 'qua': 4, 'cin':5, 'sei':6, 'set':7, 'ott':8, 'nov':9, 'die':10}

# !!!! var_mem da gestire autonomamente!

i = 'sin'
instr = i[0:3]

if instr in instr_dict:
    cmd = instr_dict[instr[0:3]]
    print cmd
else:
    print 'no'