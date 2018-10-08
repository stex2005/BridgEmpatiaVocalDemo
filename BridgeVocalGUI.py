# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BridgeVocalWin
###########################################################################

class BridgeVocalWin ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BridgeVocal V0.1", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1002,536 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Connect"+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_MENU ) )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Clear"+ u"\t" + u"Ctrl+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem4 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Close"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Preferences"+ u"\t" + u"Ctrl+P", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem3.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REPORT_VIEW, wx.ART_MENU ) )
		self.m_menu2.AppendItem( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu2, u"Tools" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.vocal_instructions = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3.Add( self.vocal_instructions, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Activities" ), wx.HORIZONTAL )
		
		
		sbSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.button_loadPatient = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.button_loadPatient, 0, wx.ALL, 5 )
		
		self.button_StartCtrl = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.button_StartCtrl, 0, wx.ALL, 5 )
		
		self.butt_StopControl = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.butt_StopControl, 0, wx.ALL, 5 )
		
		
		sbSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer3, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.show_terminal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.show_terminal.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.show_terminal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer5.Add( self.show_terminal, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4.SetMinSize( wx.Size( -1,500 ) ) 
		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetMaxSize( wx.Size( -1,100 ) )
		
		bSizer4.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.exo3d_container = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer4.Add( self.exo3d_container, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetMaxSize( wx.Size( -1,100 ) )
		
		bSizer4.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"2D view" ), wx.VERTICAL )
		
		self.exo_piano1 = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2.Add( self.exo_piano1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.exo_piano2 = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2.Add( self.exo_piano2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.exo_piano3 = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2.Add( self.exo_piano3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		bSizer2.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close )
		self.Bind( wx.EVT_MENU, self.connect_command, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.exit, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.preferences, id = self.m_menuItem3.GetId() )
		self.button_loadPatient.Bind( wx.EVT_BUTTON, self.loadPatient_command )
		self.button_StartCtrl.Bind( wx.EVT_BUTTON, self.enableCtrlVoice_command )
		self.butt_StopControl.Bind( wx.EVT_BUTTON, self.disableCtrl_command )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()
	
	def connect_command( self, event ):
		event.Skip()
	
	def exit( self, event ):
		event.Skip()
	
	def preferences( self, event ):
		event.Skip()
	
	def loadPatient_command( self, event ):
		event.Skip()
	
	def enableCtrlVoice_command( self, event ):
		event.Skip()
	
	def disableCtrl_command( self, event ):
		event.Skip()
	

