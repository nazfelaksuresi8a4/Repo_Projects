from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys as _system_
import os as _osystem_
import nmap as _nm_
from datetime import datetime as _dt_

class mainTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_current_root_PassWord___=[]
        rootpassscreen_la1=QVBoxLayout()
        self.setrootpasswordmaindirerctory=QSplashScreen(self)
        source_=r'C:\Desktop\apk_internal\umbrella_ico.webp'
        img=QImage(source_)
        self.main_lbl=QLabel()
        self.mainpix1=QPixmap(img)
        self.main_lbl.setAlignment(Qt.AlignCenter)
        self.main_lbl.setPixmap(self.mainpix1)
        self.mainpix1.toImage()
        mainrootpasswordlbl1=QPushButton("←↑→↓↖↗↘↙ **Umbrella ya hoşgeldiniz lütfen başlamadan önce bir root şifresi belirleyin** ←↑→↓↖↗↘↙")
        self.setrootpasswordmaindirerctory.setGeometry(650,350,900,300)
        self.setrootpasswordmaindirerctory.setStyleSheet('''
background-color:black;        
border:2px solid red
''')
        self.main_lbl.setStyleSheet('color:')
        self.main_rootpasswordmain_set_edit=QLineEdit()
        self.mainrootpasswordconfirmhexedit=QLineEdit()
        self.main_rootpasswordmain_set_edit.setPlaceholderText('**root şifrenizi girin**')
        self.mainrootpasswordconfirmhexedit.setPlaceholderText('**root şifrenizi onaylayın**')
        self.main_rootpasswordmain_set_edit.setEchoMode(QLineEdit.Password)
        self.mainrootpasswordconfirmhexedit.setEchoMode(QLineEdit.Password)
        self.main_rootpasswordmain_set=QPushButton('TAMAM')
        mainrootpasswordlbl1.setStyleSheet('''
background-color:red;
color:black;
border:2px solid blue;
border-radius:5px;
font-size:20px;
font-weight:bold;
''')
        self.main_rootpasswordmain_set_edit.setStyleSheet('''QLineEdit{
background-color:darkred;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QLineEdit:hover{
background-color:darkgreen;
color:white;
font-size:15px;           
border: 1.5px solid orange;            
}
QLineEdit:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}      
''')
        self.mainrootpasswordconfirmhexedit.setStyleSheet('''QLineEdit{
background-color:darkred;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QLineEdit:hover{
background-color:darkgreen;
color:white;
font-size:15px;           
border: 1.5px solid orange;            
}
QLineEdit:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}
''')
        self.main_rootpasswordmain_set.setStyleSheet('''QPushButton{
background-color:black;
color:red;
font-size:15px;
font-weight:bold;
border:0.5px solid darkblue;
}
QPushButton:hover{
background-color:darkgreen;
color:darkred;
font-size:16px;
font-weight:italic                                 
}
QPushButton:pressed{
background-color:darkblue;
color:darkred;
font-size:20px;
font-weight:bold                                   
}''')
        rootpassscreen_la1.addWidget(mainrootpasswordlbl1)
        rootpassscreen_la1.addWidget(self.main_lbl)
        rootpassscreen_la1.addWidget(self.main_rootpasswordmain_set_edit)
        rootpassscreen_la1.addWidget(self.mainrootpasswordconfirmhexedit)
        rootpassscreen_la1.addWidget(self.main_rootpasswordmain_set)
        self.setrootpasswordmaindirerctory.show()
        self.setrootpasswordmaindirerctory.setLayout(rootpassscreen_la1)
        self.main_rootpasswordmain_set.clicked.connect(self.main_root_pass_confirmer1111)
        self.main_wid=QWidget()
        self.sec_la=QFormLayout()
        self.main_la=QHBoxLayout(self.main_wid)
        self.main_central_splt_1=QSplitter(Qt.Vertical)
        self.main_central_splt_2=QSplitter(Qt.Vertical)
        self.main_la.addWidget(self.main_central_splt_1)
        self.main_la.addWidget(self.main_central_splt_2)
        self.setStyleSheet('background-color:gray')
        self.setWindowTitle('İP/PORT Tracker+')
        self.setGeometry(650,350,1060,200)
        self.menubars=self.menuBar()
        self.main_setting_bar=self.menubars.addMenu('▬GÖRÜNÜM AYARLARI▬')
        self.main_setting_bar_action_bg1=self.main_setting_bar.addAction('arka plan rengi')
        self.main_setting_bar_action_fg=self.main_setting_bar.addAction('yazı görünümü')
        self.main_setting_bar_action_fg=self.main_setting_bar.addAction('')
        self.main_notify_setting_bar=self.menubars.addMenu('▬*BİLDİRİM AYARLARI*▬')
        self.main_net_setting_bar=self.menubars.addMenu('▬*NET AYARLARI*▬')
        self.main_mapper=self.menubars.addMenu('▬*MAPPER*▬')
        self.mapper_ip_scan_screen_ARP=self.main_mapper.addAction('ARP haritası')
        self.mapper_ip_scan_screen_NETSTAT=self.main_mapper.addAction('NETSTAT haritası')
        self.mapper_ip_scan_screen_HELP=self.main_mapper.addAction('**Ne ise yarar**')
        self.main_dev_setting_bar=self.menubars.addMenu('*GELİŞTİRİCİ MODU*▬')
        self.root_password_c1=self.main_dev_setting_bar.addMenu('root şifresi>>')
        self.dev_settings_bar_choose_setting=self.main_dev_setting_bar.addMenu('yönetici modu>>')
        self.dev_mode_up=self.dev_settings_bar_choose_setting.addAction('<<aktif>>')
        self.dev_mode_down=self.dev_settings_bar_choose_setting.addAction('<<de-aktif>>')
        self.set_root_pswrd=self.root_password_c1.addAction('root şifreni değiştir')
        self.set_main_root_pswrd=self.root_password_c1.addAction('root şifresi oluştur')
        self.main_help_bar=self.menubars.addMenu('▬*NASIL KULLANIRIM*▬')
        self.main_raw_ip=QLineEdit()
        self.main_raw_port=QLineEdit()
        self.target_main_raw_ip=QLineEdit()
        self.target_main_raw_port=QLineEdit()
        self.sprotocol1=QComboBox()
        self.sprotocol2=QComboBox()
        self.mainlbl=QPushButton('İPT-1 x64 v-1.0.0',self.main_central_splt_1)
        self.main_raw_ip.setPlaceholderText('input a local ip adress')
        self.main_raw_port.setPlaceholderText('input a local port')
        self.target_main_raw_ip.setPlaceholderText('input a target ip adress')
        self.target_main_raw_port.setPlaceholderText('input a target port')
        self.starT_=QPushButton('<<*taramayı başlat*>>')
        self.action_info=QListWidget()
        self.main_choose_acT=QComboBox()
        self.action_info.addItem('tarama yapilirken detaylar burada gözükecektir>> echo log')
        self.reset_action_inf=QPushButton('sıfırla')
        self.main_clock=self.menubars.addAction(fr'')
        self.main_central_splt_1.setStyleSheet('''border:2px solid darkblue''')
        self.sprotocol1.addItem('--choose local protocol--')
        self.sprotocol1.addItem('*TCP*')
        self.sprotocol1.addItem('*UDP*')
        self.sprotocol1.addItem('*BGP*')
        self.sprotocol1.addItem('*HTTP*')
        self.sprotocol1.addItem('*HTTPS*')
        self.sprotocol1.addItem('*DHCP*')
        self.sprotocol1.addItem('*ICMP*')
        self.sprotocol1.addItem('*SNMP*')
        self.sprotocol1.addItem('*FTP*')
        self.sprotocol1.addItem('*POP3*')
        self.sprotocol1.addItem('*SSL*')
        self.sprotocol1.addItem('*ARP*')
        self.sprotocol1.addItem('*TLS*')
        self.sprotocol1.addItem('*HTTP*')
        self.sprotocol1.addItem('*ARP*')
        self.sprotocol1.addItem('*IMAP*')
        self.sprotocol1.addItem('*SIP*')
        self.sprotocol1.addItem('*RTP*')
        self.sprotocol1.addItem('*RAP*')
        self.sprotocol1.addItem('*PPTP*')
        self.sprotocol1.addItem('*TFTP*')
        self.sprotocol1.addItem('*RLP*')
        self.sprotocol2.addItem('--choose target protocol--')
        self.sprotocol2.addItem('*TCP*')
        self.sprotocol2.addItem('*UDP*')
        self.sprotocol2.addItem('*BGP*')
        self.sprotocol2.addItem('*HTTP*')
        self.sprotocol2.addItem('*HTTPS*')
        self.sprotocol2.addItem('*DHCP*')
        self.sprotocol2.addItem('*ICMP*')
        self.sprotocol2.addItem('*SNMP*')
        self.sprotocol2.addItem('*FTP*')
        self.sprotocol2.addItem('*POP3*')
        self.sprotocol2.addItem('*SSL*')
        self.sprotocol2.addItem('*ARP*')
        self.sprotocol2.addItem('*TLS*')
        self.sprotocol2.addItem('*HTTP*')
        self.sprotocol2.addItem('*ARP*')
        self.sprotocol2.addItem('*IMAP*')
        self.sprotocol2.addItem('*SIP*')
        self.sprotocol2.addItem('*RTP*')
        self.sprotocol2.addItem('*RAP*')
        self.sprotocol2.addItem('*PPTP*')
        self.sprotocol2.addItem('*TFTP*')
        self.sprotocol2.addItem('*RLP*')
        self.main_choose_acT.addItem('--choose scan type--')
        self.main_choose_acT.addItem('*İP SCAN*')
        self.main_choose_acT.addItem('*PORT SCAN*')
        

        self.main_central_splt_2.setStyleSheet('''border:2px solid darkred''')
        self.reset_action_inf.setStyleSheet('''QPushButton{
background-color:black;
color:green;
font-size:16px;
font-weight:bold;
border:2px solid blue;
}
QPushButton:hover{
color:darkgreen;
font-size:17px;
border:2.5px solid darkblue;
}
QPushButton:pressed{
color:red;
font-size:20px;
font-weight:italic;
border:3px solid lightblue
}        

''')
        self.action_info.setStyleSheet('''
background-color:black;
color:green;
font-size:15px;
font-weight:bold;
border:1.5px solid lightblue                                               
''')
        self.starT_.setStyleSheet('''QPushButton{
background-color:black;
color:green;
font-size:16px;
font-weight:bold;
border:2px solid blue;
}
QPushButton:hover{
color:darkgreen;
font-size:17px;
border:2.5px solid darkblue;
}
QPushButton:pressed{
color:red;
font-size:20px;
font-weight:italic;
border:3px solid lightblue
}
''')
        self.menubars.setStyleSheet('''QMenuBar{
background-color:black;
border:1px solid darkblue;
color:darkred;                                   
}
QMenuBar::item:selected{
background-color:black;
color:darkred;
border:3px solid darkgreen;                                    
}
QMenuBar::item:pressed{
background-color:black;
color:darkgreen;
border:2px solid orange;                        
}
''')
        self.mainlbl.setStyleSheet('''
border:none;
background-color:black;
color:green;
font-size:15px;
font-weight:bold
''')
        self.main_raw_ip.setStyleSheet('''QLineEdit{
background-color:darkred;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QLineEdit:hover{
background-color:darkgreen;
color:white;
font-size:15px;           
border: 1.5px solid orange;            
}
QLineEdit:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.main_raw_port.setStyleSheet('''QLineEdit{
background-color:darkred;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QLineEdit:hover{
background-color:darkgreen;
color:white;
font-size:15px;           
border: 1.5px solid orange;            
}
QLineEdit:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.target_main_raw_ip.setStyleSheet('''QLineEdit{
background-color:darkred;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QLineEdit:hover{
background-color:darkgreen;
color:white;
font-size:15px;           
border: 1.5px solid orange;            
}
QLineEdit:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.target_main_raw_port.setStyleSheet('''QLineEdit{
background-color:darkred;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QLineEdit:hover{
background-color:darkgreen;
font-size:15px;           
border: 1.5px solid orange;            
}
QLineEdit:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.sprotocol1.setStyleSheet('''QComboBox{
background-color:red;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QComboBox:hover{
background-color:green;
font-size:15px;           
border: 1.5px solid orange;            
}
QComboBox:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.sprotocol2.setStyleSheet('''QComboBox{
background-color:red;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QComboBox:hover{
background-color:green;
font-size:15px;           
border: 1.5px solid orange;            
}
QComboBox:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.main_choose_acT.setStyleSheet('''QComboBox{
background-color:red;
color:black;
font-size:14px;
font-weight:bold;
border:1px solid lightred;                                   
}
QComboBox:hover{
background-color:green;
font-size:15px;           
border: 1.5px solid orange;            
}
QComboBox:pressed{
background-color:blue;
color:black;
font-size:20px;
font-weight:bold;
border:2px solid orange;
}''')
        self.main_central_splt_2.addWidget(self.reset_action_inf)
        self.main_central_splt_2.addWidget(self.action_info)
        self.main_central_splt_1.addWidget(self.mainlbl)
        self.main_central_splt_1.addWidget(self.sprotocol1)
        self.main_central_splt_1.addWidget(self.main_raw_ip)
        self.main_central_splt_1.addWidget(self.main_raw_port)  
        self.main_central_splt_1.addWidget(self.sprotocol2)
        self.main_central_splt_1.addWidget(self.target_main_raw_ip)
        self.main_central_splt_1.addWidget(self.target_main_raw_port)
        self.main_central_splt_1.addWidget(self.main_choose_acT)
        self.main_central_splt_1.addWidget(self.starT_)
        v=QTimer(self)
        v.start(100)
        v.timeout.connect(self.var_d)
        self.sprotocol1.currentIndexChanged.connect(self.select_header)
        self.starT_.clicked.connect(self.start_header)
        self.reset_action_inf.clicked.connect(self.reset_info_header)
        self.mapper_ip_scan_screen_ARP.triggered.connect(self.main_ARP_MAP)
        self.mapper_ip_scan_screen_NETSTAT.triggered.connect(self.main_NETSTAT_MAPPER)
        self.dev_mode_up.triggered.connect(self.main_dev_mode_up_header)
        self.setCentralWidget(self.main_wid)
    def main_dev_mode_up_header(self):
        try:
            main_dev_splsh1=QSplashScreen(self)
            main_dev_splsh1.resize(350,50)
            main_dev_splsh_la1=QVBoxLayout()
            main_dev_splsh1.setLayout(main_dev_splsh_la1)
            main_dev_splsh1.setStyleSheet('''
            background-color:black;
            border:4px solid darkred
            ''')
            main_dev_splt1=QSplitter(Qt.Vertical)
            self.main_dev_mode_splt_line_e1_main=QLineEdit()
            self.main_dev_mode_splt_bt_b1_main=QPushButton('<<TAMAM>>')
            self.main_dev_mode_splt_line_e1_main.setPlaceholderText('$$>>> ++root sifrenizi girin++')
            self.main_dev_mode_splt_bt_b1_main.setStyleSheet('''QPushButton{
background-color:black;
color:green;
font-size:16px;
font-weight:bold;
border:2px solid blue;
border-radius:10px
}
QPushButton:hover{
color:darkgreen;
font-size:17px;
border:2.5px solid darkblue;
}
QPushButton:pressed{
color:red;
font-size:20px;
font-weight:italic;
border:3px solid lightblue
}''')
            self.main_dev_mode_splt_line_e1_main.setStyleSheet('''QLineEdit{
background-color:black;
color:green;
font-size:14px;
font-weight:bold;
border:2px solid darkblue;            
border-radius:10px
}''')
            main_dev_splsh_la1.addWidget(main_dev_splt1)
            main_dev_splt1.addWidget(self.main_dev_mode_splt_line_e1_main)
            main_dev_splt1.addWidget(self.main_dev_mode_splt_bt_b1_main)
            main_dev_splt1.setStyleSheet('''
background-color:black;
border:3px solid red;
border-radius:10px            
''')
            main_dev_splsh1.show()
        except:
            print('faf')    
    def main_ARP_MAP(self):
        main_current_time=_dt_.now().strftime('%H:%M:%S')
        i_to_s=str(main_current_time)
        self.ARP_SCREEN=QSplashScreen(self)
        self.main_right_b2=QPushButton('←',self.ARP_SCREEN)
        self.main_left_b2=QPushButton('→',self.ARP_SCREEN)
        self.main_down_b2=QPushButton('v',self.ARP_SCREEN)
        self.main_up_b2=QPushButton('↑',self.ARP_SCREEN)
        self.main_up_b2.resize(40,10)
        self.main_down_b2.resize(40,10)
        self.main_right_b2.resize(40,10)
        self.main_left_b2.resize(40,10)
        self.main_left_b2.move(190,0)
        self.main_up_b2.move(60,0)
        self.main_down_b2.move(120,0)
        self.main_up_b2.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:20px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_down_b2.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:10px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_right_b2.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:20px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_left_b2.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:20px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.ARP_SCREEN.setGeometry(1100,400,500,300)
        self.main_la_splash=QVBoxLayout()
        self.ARP_SCREEN.setStyleSheet('background-color:darkred')
        lbl=QLabel(f'(AMC) Arp Mapper Console v1.0.0')
        main_reset=QPushButton('SIFIRLA')
        main_show_arp_ultily_output=QPushButton('TARAMA BAŞLAT')
        self.main_mapper=QListWidget()
        self.select_argument_chooser=QComboBox()
        self.select_argument_chooser.addItem('[ARGÜMAN SEC]')
        self.select_argument_chooser.addItem('argüman>> -a')
        self.main_mapper.addItem('           ARP MAPPER seçeneği ile etrafınızdaki ip adreslerini tarayın')
        self.select_argument_chooser.setStyleSheet('''QComboBox{
background-color:black;
color:blue;
font-weight:bold;
font-size:15px;
border:1.5px solid darkblue;        
}
QComboBox::item:selected{
background-color:blue;
color:black;
border:1.5px solid blue; 
}
''')
        self.main_mapper.setStyleSheet('''
background-color:black;        
color:red;
font-size:14px;
font-weight:italic
''')    
        main_show_arp_ultily_output.setStyleSheet('''QPushButton{
background-color:black;
color:red;
font-size:15px;
font-weight:bold;
border:0.5px solid darkblue;
}
QPushButton:hover{
background-color:darkgreen;
color:darkred;
font-size:16px;
font-weight:italic                                 
}
QPushButton:pressed{
background-color:darkblue;
color:darkred;
font-size:20px;
font-weight:bold                                   
}
''')
        main_reset.setStyleSheet('''QPushButton{
background-color:black;
color:red;
font-size:15px;
font-weight:bold;
border:0.5px solid darkblue;
}
QPushButton:hover{
background-color:darkgreen;
color:darkred;
font-size:16px;
font-weight:italic                                 
}
QPushButton:pressed{
background-color:darkblue;
color:darkred;
font-size:20px;
font-weight:bold                                   
}
''')
        lbl.setStyleSheet('''
background-color:black; 
color:green;
border:1px solid blue;
font-size:20px;
font-weight:bold
''')

        self.main_la_splash.addWidget(lbl)
        self.main_la_splash.addWidget(self.select_argument_chooser)
        self.main_la_splash.addWidget(self.main_mapper)
        self.main_la_splash.addWidget(main_show_arp_ultily_output)
        self.main_la_splash.addWidget(main_reset)
        self.ARP_SCREEN.setLayout(self.main_la_splash)
        self.ARP_SCREEN.show()
        main_show_arp_ultily_output.clicked.connect(self.main_show_arp_scan_output)
        main_reset.clicked.connect(self.main_arp_system_interface_test)
        self.main_right_b2.clicked.connect(self.main_amcs_r_b2)
        self.main_up_b2.clicked.connect(self.main_amcs_d_b2)
        self.main_down_b2.clicked.connect(self.main_amcs_u_b2)
        self.main_left_b2.clicked.connect(self.main_amcs_l_b2)
    def main_NETSTAT_MAPPER(self):
        #←↑→↓↖↗↘↙#
        self.an=('an')
        self.a=('a')
        self.e=('e')
        self.n=('n')
        self.o=('o')
        self.r=('r')
        self.p=('p')
        self.s=('s')
        self.b=('b')
        self.x1x=('x')
        self.y1y=('y')
        main_current_time=_dt_.now().strftime('%H:%M:%S')
        i_to_s=str(main_current_time)
        self.NETSTAT_SCREEN=QSplashScreen(self)
        self.NETSTAT_SCREEN.setGeometry(1100,400,500,300)
        self.main_la2_splash=QVBoxLayout()
        self.NETSTAT_SCREEN.setStyleSheet('background-color:darkred')
        lbl=QLabel(f'(NMC) NETSTAT Mapper Console v1.0.0')
        main_reset=QPushButton('SIFIRLA')
        main_show_arp_ultily_output=QPushButton('TARAMA BAŞLAT')
        self.main_mapper2=QListWidget()
        self.select_argument_chooser2=QComboBox()
        self.select_argument_chooser2.addItem('[ARGÜMAN SEC]')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.an}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.a}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.e}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.n}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.o}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.r}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.p}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.s}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.b}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.x1x}')
        self.select_argument_chooser2.addItem(f'argüman>> -{self.y1y}')
        self.main_mapper2.addItem('NETSTAT MAPPER seçeneği ile NETWORKLER ÜZERİNDE DETAYLI TARAMALAR YAPIN')
        self.select_argument_chooser2.setStyleSheet('''QComboBox{
background-color:black;
color:blue;
font-weight:bold;
font-size:15px;
border:1.5px solid darkblue;        
}
QComboBox::item:selected{
background-color:blue;
color:black;
border:1.5px solid blue; 
}
''')
        self.main_mapper2.setStyleSheet('''
background-color:black;        
color:red;
font-size:14px;
font-weight:italic
''')    
        main_show_arp_ultily_output.setStyleSheet('''QPushButton{
background-color:black;
color:red;
font-size:15px;
font-weight:bold;
border:0.5px solid darkblue;
}
QPushButton:hover{
background-color:darkgreen;
color:darkred;
font-size:16px;
font-weight:italic                                 
}
QPushButton:pressed{
background-color:darkblue;
color:darkred;
font-size:20px;
font-weight:bold                                   
}
''')
        main_reset.setStyleSheet('''QPushButton{
background-color:black;
color:red;
font-size:15px;
font-weight:bold;
border:0.5px solid darkblue;
}
QPushButton:hover{
background-color:darkgreen;
color:darkred;
font-size:16px;
font-weight:italic                                 
}
QPushButton:pressed{
background-color:darkblue;
color:darkred;
font-size:20px;
font-weight:bold                                   
}
''')
        lbl.setStyleSheet('''
background-color:black; 
color:green;
border:1px solid blue;
font-size:20px;
font-weight:bold
''')
        self.main_right_b1=QPushButton('←',self.NETSTAT_SCREEN)
        self.main_left_b1=QPushButton('→',self.NETSTAT_SCREEN)
        self.main_down_b1=QPushButton('v',self.NETSTAT_SCREEN)
        self.main_up_b1=QPushButton('↑',self.NETSTAT_SCREEN)
        self.main_up_b1.resize(40,10)
        self.main_down_b1.resize(40,10)
        self.main_right_b1.resize(40,10)
        self.main_left_b1.resize(40,10)
        self.main_left_b1.move(190,0)
        self.main_up_b1.move(60,0)
        self.main_down_b1.move(120,0)
        self.main_up_b1.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:20px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_down_b1.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:10px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_right_b1.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:20px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_left_b1.setStyleSheet('''QPushButton{
font-weight:bold;
font-size:20px;
border-radius:4px;
border:0.2px solid orange;
background-color:darkblue;
color:white 
}    
QPushButton:hover{   
border:0.3px solid orange;
background-color:blue;
color:green
}
QPushButton:pressed{   
border:1px solid darkred;
background-color:gray;
color:darkgreen;
}
''')
        self.main_la2_splash.addWidget(lbl)
        self.main_la2_splash.addWidget(self.select_argument_chooser2)
        self.main_la2_splash.addWidget(self.main_mapper2)
        self.main_la2_splash.addWidget(main_show_arp_ultily_output)
        self.main_la2_splash.addWidget(main_reset)
        self.NETSTAT_SCREEN.setLayout(self.main_la2_splash)
        self.NETSTAT_SCREEN.show()
        main_show_arp_ultily_output.clicked.connect(self.main_show_netstat_scan_output)
        main_reset.clicked.connect(self.main_netstat_system_interface_test)
        self.main_right_b1.clicked.connect(self.main_nmcs_r_b1)
        self.main_left_b1.clicked.connect(self.main_nmcs_l_b1)
        self.main_up_b1.clicked.connect(self.main_nmcs_d_b1)
        self.main_down_b1.clicked.connect(self.main_nmcs_u_b1)
    def main_nmcs_r_b1(self):
        y_degres=self.NETSTAT_SCREEN.y()
        x_degres=self.NETSTAT_SCREEN.x()
        x_degres-=20
        self.NETSTAT_SCREEN.move(x_degres,y_degres)
    def main_nmcs_l_b1(self):
        y_degres=self.NETSTAT_SCREEN.y()
        x_degres=self.NETSTAT_SCREEN.x()
        x_degres+=20
        self.NETSTAT_SCREEN.move(x_degres,y_degres)
    def main_nmcs_u_b1(self):
        y_degres=self.NETSTAT_SCREEN.y()
        x_degres=self.NETSTAT_SCREEN.x()
        y_degres+=20
        self.NETSTAT_SCREEN.move(x_degres,y_degres)
    def main_nmcs_d_b1(self):
        y_degres=self.NETSTAT_SCREEN.y()
        x_degres=self.NETSTAT_SCREEN.x()
        y_degres-=20
        self.NETSTAT_SCREEN.move(x_degres,y_degres)
    def main_amcs_r_b2(self):
        y_degres=self.ARP_SCREEN.y()
        x_degres=self.ARP_SCREEN.x()
        x_degres-=20
        self.ARP_SCREEN.move(x_degres,y_degres)
    def main_amcs_l_b2(self):
        y_degres=self.ARP_SCREEN.y()
        x_degres=self.ARP_SCREEN.x()
        x_degres+=20
        self.ARP_SCREEN.move(x_degres,y_degres)
    def main_amcs_u_b2(self):
        y_degres=self.ARP_SCREEN.y()
        x_degres=self.ARP_SCREEN.x()
        y_degres+=20
        self.ARP_SCREEN.move(x_degres,y_degres)
    def main_amcs_d_b2(self):
        y_degres=self.ARP_SCREEN.y()
        x_degres=self.ARP_SCREEN.x()
        y_degres-=20
        self.ARP_SCREEN.move(x_degres,y_degres)
    def main_arp_system_interface_test(self):
        self.main_mapper.clear()
        self.main_mapper.addItem('           ARP MAPPER seçeneği ile etrafınızdaki ip adreslerini tarayın')
    def main_netstat_system_interface_test(self):
        self.main_mapper2.clear()    
        self.main_mapper2.addItem('NETSTAT MAPPER seçeneği ile NETWORKLER ÜZERİNDE DETAYLI TARAMALAR YAPIN')
    def main_root_pass_confirmer1111(self):
        current_pass=self.main_rootpasswordmain_set_edit.text()
        confirmer=self.mainrootpasswordconfirmhexedit.text()
        destroy_state_index=0
        try:
            if confirmer=='':
                QMessageBox.warning(self,'!UYARI!','!lütfen şirenizi onaylayın!')
                return
        except Exception as e111:
            print(f'hata {e111}')
        try:
            if current_pass=='':
                QMessageBox.warning(self,'!UYARI!','!şifre alanı boş bırakılamaz!')
                return
        except Exception as e11_c14f:
            print(f'hata: {e11_c14f}')        
        try:
            if current_pass==confirmer:
                destroy_state_index=1
                self.main_current_root_PassWord___=(f"{current_pass}")
                QMessageBox.information(self,'!başarılı!','!root şifreniz damgalandı!')
                self.setrootpasswordmaindirerctory.destroy()
            else:
                QMessageBox.warning(self,'hata: şifreniz uyuşmuyor','lütfen şifrenizi tekrar girin')
        except Exception as MAİN_KERNEL_E:
            print(f'hata: {MAİN_KERNEL_E}')
        try:
            self.setrootpasswordmaindirerctory.destroyed.connect(self.directort_main_f1276e13)
        except:
            print()
        
            
    def main_show_netstat_scan_output(self):
        main_argument_data=self.select_argument_chooser2.currentText()
        try:
            if main_argument_data=='argüman>> -an':
                self.x_1=_osystem_.popen('netstat -an').read()
                self.str_x1=str(self.x_1)
                self.unit_x_1r90=self.str_x1.splitlines()  
                self.main_arp_a_argument_detail_scan()
        except Exception as arp_kernel_e145:
            print(f'hata: {arp_kernel_e145}')        
        try:
            if main_argument_data=='argüman>> -a':
                self.proces=QProcess()
                self.proces.readyReadStandardOutput.connect(self.arp_a_header_r95916f4195)
                self.proces.start('netstat',['-a'])
        except Exception as arp_kernel_e145:
            print(f'hata: {arp_kernel_e145}')        
        try:
            if main_argument_data=='argüman>> -e':
                x_1=_osystem_.popen('netstat -e').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -n':
                x_1=_osystem_.popen('netstat -n').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -o':  
                self.proces2_o=QProcess()
                self.proces2_o.readyReadStandardOutput.connect(self.main_netstat_argument_o_data_header_string)
                self.proces2_o.start('netstat',['-o'])
        except Exception as argument_error:
            print(f'hata: {argument_error}')
        try:
            if main_argument_data=='argüman>> -p':
                x_1=_osystem_.popen('netstat -p').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -r':
                x_1=_osystem_.popen('netstat -r').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -s':
                x_1=_osystem_.popen('netstat -s').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='[ARGÜMAN SEC]':
                QMessageBox.warning(self,'DİKKAT','Lütfen bir argüman seçiniz!  ')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -b':
                x_1=_osystem_.popen('netstat -b').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -x':
                x_1=_osystem_.popen('netstat -x').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='[ARGÜMAN SEC]':
                QMessageBox.warning(self,'DİKKAT','Lütfen bir argüman seçiniz!  ')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='argüman>> -y':
                x_1=_osystem_.popen('netstat -y').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper2.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='[ARGÜMAN SEC]':
                QMessageBox.warning(self,'DİKKAT','Lütfen bir argüman seçiniz!  ')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
    def main_arp_a_argument_detail_scan(self):
            try:
                for arp_datas in self.unit_x_1r90:
                    self.main_mapper2.addItem(str(arp_datas))
            except Exception as kernel_error_e2:
                print(f'hata: {kernel_error_e2}')
    def main_show_arp_scan_output(self):
        main_argument_data=self.select_argument_chooser.currentText()
        try:
            if main_argument_data=='argüman>> -a':
                x_1=_osystem_.popen('arp -a').read()
                str_x=x_1.splitlines()
                try:
                    for arp_datas in str_x:
                        self.main_mapper.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
        try:
            if main_argument_data=='[ARGÜMAN SEC]':
                QMessageBox.warning(self,'DİKKAT','Lütfen bir argüman seçiniz!  ')
                try:
                    for arp_datas in str_x:
                        self.main_mapper.addItem(str(arp_datas))
                except Exception as kernel_error_e2:
                    print(f'hata: {kernel_error_e2}')
        except Exception as kernel_error_e1:
            print(f'hata: {kernel_error_e1}')
    def main_netstat_argument_o_data_header_string(self):
        proces_2_datA=self.proces2_o.readAllStandardOutput().data().decode('utf-8')
        main_split_proces_2r14151f14145=proces_2_datA.splitlines()
        self.main_mapper2.scrollToItem(self.main_mapper2.item(self.main_mapper2.count() - 1))
        try:
            self.main_mapper2.addItems(main_split_proces_2r14151f14145)
        except Exception as kernel_error_e2:
            print(f'hata: {kernel_error_e2}')
    def start_header(self):
        self.main_dt_system2=_dt_.now().strftime('%H:%M:%S')
        self.main_dt_system2_t_St=str(self.main_dt_system2)
        try:
             self.st1=self.main_raw_ip.text()
             self.i_to_s=str(self.st1)
        except:
             QMessageBox.warning(self,'DİKKAT','Lütfen geçerli bir ip adresi girin!')
        try:
             self.st2=self.main_raw_port.text()
             self.i_to_s2=str(self.st1)
        except:
             QMessageBox.warning(self,'DİKKAT','Lütfen geçerli bir ip adresi girin!')
        try:
             self.st1_t=self.target_main_raw_ip.text()
             self.i_to_s=str(self.st1)
        except:
             QMessageBox.warning(self,'DİKKAT','Lütfen geçerli bir ip adresi girin!')
        try:
             self.st2_t=self.target_main_raw_port.text()
             self.i_to_s2=str(self.st1)
        except:
             QMessageBox.warning(self,'DİKKAT','Lütfen geçerli bir ip adresi girin!')
        self.mainstr1_1_1=self.sprotocol1.currentText()
        self.mainstr2_1_2=self.sprotocol2.currentText()
        self.main_0_0=f"local İP: {self.st1} local PORT: {self.st2}"
        self.main_1_1=f"target İP: {self.st1} target PORT: {self.st2}"
        self.main_2_2=f"local PROTOCOL: {self.mainstr1_1_1}"
        self.main_3_3=f"target PROTOCOL: {self.mainstr2_1_2}"
        self.main_4_4_sm=f"scan starting>> {self.main_dt_system2}"
        try:
             self.scan_sf_status=f'scan start: TRUE'
        except:
             QMessageBox(self,'dikkat','tarama esnasında bir hata meydana geldi lütfen tekrar deneyiniz bu hatayı tekrar alırsanız programı yeniden başlatmayı deneyin.')     
        self.main_1=f""
        self.cpt_indeX=0
        self.d=QTimer(self)
        self.d.timeout.connect(self.main_start_header)
        self.d.start(900)
    def arp_a_header_r95916f4195(self):
        main_data=self.proces.readAllStandardOutput().data().decode('utf-8')
        splitted_Data_f19842u402984=main_data.splitlines()
        self.main_mapper2.addItems(splitted_Data_f19842u402984)
        self.main_mapper2.scrollToItem(self.main_mapper2.item(self.main_mapper2.count() - 1))
    def main_dat_defination_1(self):
            self.g=QTimer(self)
            self.g.timeout.connect(self.main_dat_defination_1)
            self.g.start(500)
            main_scanner=_nm_.PortScanner()
            scan_target=self.target_main_raw_ip.text()
            main_scanner.scan(scan_target,arguments='-sS')
            for proto in main_scanner[scan_target].all_protocols():
                ports=main_scanner[scan_target][proto].keys()
                for port in ports:
                    state=main_scanner[scan_target][proto][port]['state']
                    main_scan_output=[f'port: {port} protokol: {proto} durum {state}']
                    self.action_info.addItem(main_scan_output)
    def main_start_header(self):
        self.currstR=self.main_choose_acT.currentText()
        if self.currstR=="*İP SCAN*":
            self.cpt_indeX+=1
            if self.cpt_indeX==1:
                try:
                    self.action_info.addItem(self.main_0_0)
                    self.action_info.addItem('')
                except:
                     print('fg')
            if self.cpt_indeX==2:
                try:
                    self.action_info.addItem(self.main_1_1)
                    self.action_info.addItem('')
                except:
                     print('fe')
            if self.cpt_indeX==3:
                try:
                    self.action_info.addItem(self.main_2_2)
                    self.action_info.addItem('')
                except:
                     print('fe')
            if self.cpt_indeX==5:
                try:
                    self.action_info.addItem(self.main_3_3)
                    self.action_info.addItem('')
                    self.d.start(2300)
                except:
                     print('fre')
            if self.cpt_indeX==6:
                try:
                    self.action_info.addItem(self.main_4_4_sm)
                    self.action_info.addItem('')
                    self.d.stop()
                    self.main_dat_defination_1()
                except:
                     print('fre')
                     self.d.stop()
        elif self.currstR=="*PORT SCAN*":
            self.d.stop()
            print()
        else:   
            self.d.stop()
            try:
                QMessageBox.warning(self,'DİKKAT','Lütfen geçerli bir tarama türü seçmeden tarama başlatmaya çalışmayın')
            except:
                QMessageBox.information(self,"**bilgilendirme**","Lütfen karşınıza gelen ekrandan bir tarama türü seçip (TAMAM)'a basın..")
                print('!geri bildirim başarısız!')
            try:
                self.main_choose_acT.setCurrentText('**İP SCAN**')
                self.main_qsplah=QSplashScreen(self)
                self.main_qsplah.setStyleSheet('''background-color:gray''')
                self.main_select_box=QComboBox()
                self.main_select_box.addItem('**İP TARAMASI**')
                self.main_select_box.addItem('**PORT TARAMASI**')
                self.mainapplybtn=QPushButton('TAMAM')
                self.main_select_box.setStyleSheet('''
                background-color:white;
                color:black;
                ''') 
                lA_=QVBoxLayout()
                self.main_qsplah.setLayout(lA_)
                lA_.addWidget(self.main_select_box)
                lA_.addWidget(self.mainapplybtn)
                self.main_qsplah.show()
                self.d.stop() 
                self.mainapplybtn.clicked.connect(self.ffzero_select_Headr)
            except Exception as e:
                print(f"error: {e}")  
                try:
                    self.ffzero_select_Headr()
                except Exception as e:
                    print(f"error: {e}")
    def ffzero_select_Headr(self):
        try:
            if self.main_select_box.currentText()=="**İP TARAMASI**":
                try:
                    self.main_choose_acT.setCurrentIndex(1)
                    self.main_qsplah.destroy()
                except Exception as kernel_error:
                    print(f"error: {kernel_error}")
        except Exception as small_water_error:
            print(f"error: {small_water_error}")
        try:
            if self.main_select_box.currentText()=="**PORT TARAMASI**":
                try:
                    self.main_choose_acT.setCurrentIndex(2)
                    self.main_qsplah.destroy()
                except Exception as kernel_error:
                    print(f"error: {kernel_error}")
        except Exception as small_water_error2:
            print(f"error: {small_water_error2}")
    def select_header(self,value):
        self.mainstr=self.sprotocol1.currentText()
        if self.mainstr=="--choose local protocol--":
                QMessageBox.warning(self,'!**DİKKAT**!','lütfen geçerli bir protokol seçin')
    def var_d(self):
        self.main_dt_system=_dt_.now().strftime('%H:%M:%S')
        self.main_clock.setText(self.main_dt_system)
    def reset_info_header(self):
        self.action_info.clear()
        self.action_info.reset()
        self.action_info.addItem('tarama yapilirken detaylar burada gözükecektir>> echo log')
if __name__=="__main__":
    main_ap=QApplication(_system_.argv)
    main_wframe=mainTracker()
    main_wframe.show()
    _system_.exit(main_ap.exec_())