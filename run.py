import os
import sys
import time
from time import sleep

m = '\x1b[1;31m'
h = '\x1b[1;32m'
k = '\x1b[1;33m'
b = '\x1b[1;36m'
p = '\x1b[1;37m'
u = '\x1b[1;35m'

def wr(w):
    for t in w + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        sleep(1 / 1000)

def tik():
    titik = ['| ', '/ ', '_', '\\ ', '|']
    for o in titik:
        print('\r' + h + 'please wait  ' + o, end='')
        sys.stdout.flush()
        time.sleep(0.5)

ban = '''
 \x1b[1;31m╔╦╗╔═╗╦╔═╗╔╦╗╦   ╦╔═╗ ╦   ╔═╗╔╦╗╔╦╗╦ ╦ ╦╔═╗
 \x1b[1;31m║║║╠═╣║╠═╣ ║ ║   ║║ ║ ║   ╠═╣ ║ ║║║╚╦╝ ║║  
 \x1b[1;31m╩ ╩╩ ╩╩╩ ╩ ╩ ╩   ╩╚═╝ ╩   ╩ ╩ ╩ ╩ ╩ ╩  ╩╚═╝
\x1b[1;32m◀\x1b[1;35m══════════════════════════════════════════════════\x1b[1;32m▶
\x1b[1;37m[\x1b[1;32m+\x1b[1;37m]\x1b[1;36mAuthor  \x1b[1;37m: \x1b[1;33mMR•ANKER
\x1b[1;37m[\x1b[1;32m+\x1b[1;37m]\x1b[1;36mGithub  \x1b[1;37m: \x1b[1;33mhttps://github.com/4NK3R-PRODUCT1ON
\x1b[1;37m[\x1b[1;32m+\x1b[1;37m]\x1b[1;36mYoutube \x1b[1;37m: \x1b[1;33mANKER PRODUCTION
\x1b[1;32m◀\x1b[1;35m══════════════════════════════════════════════════\x1b[1;32m▶
'''

def keluar():
    print(h + 'Exiting...')
    sleep(2)
    print(k + 'Thanks for used my script')
    sys.exit()

def red():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        red()
    else:
        tik()
        tulis = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        tulis.write('#Author : ANKER\n#Github : 4NK3R \n#Youtube\n')
        tulis.write('clear\nsleep 2.1\n')
        tulis.write("echo '\x1b[1;31m         @@@@@                                        @@@@@'\n")
        tulis.write("echo '\x1b[1;31m        @@@@@@@                                      @@@@@@@'\n")
        tulis.write("echo '\x1b[1;31m        @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@'\n")
        tulis.write("echo '\x1b[1;31m         @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@'\n")
        tulis.write("echo '\x1b[1;31m             @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@'\n")
        tulis.write("echo '\x1b[1;31m               @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@'\n")
        tulis.write("echo '\x1b[1;31m                 @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@'\n")
        tulis.write("echo '\x1b[1;31m                    @@@@@@@    @@@@@@    @@@@@@'\n")
        tulis.write("echo '\x1b[1;31m                    @@@@@@      @@@@      @@@@@'\n")
        tulis.write("echo '\x1b[1;31m                    @@@@@@      @@@@      @@@@@'\n")
        tulis.write("echo '\x1b[1;31m                     @@@@@@    @@@@@@    @@@@@'\n")
        tulis.write("echo '\x1b[1;31m                      @@@@@@@@@@@  @@@@@@@@@@'\n")
        tulis.write("echo '\x1b[1;31m                       @@@@@@@@@@  @@@@@@@@@'\n")
        tulis.write("echo '\x1b[1;31m                    @@   @@@@@@@@@@@@@@@@@   @@'\n")
        tulis.write("echo '\x1b[1;31m                   @@@@  @@@@ @ @ @ @ @@@@  @@@@'\n")
        tulis.write("echo '\x1b[1;31m                  @@@@@   @@@ @ @ @ @ @@@   @@@@@'\n")
        tulis.write("echo '\x1b[1;31m                @@@@@      @@@@@@@@@@@@@      @@@@@'\n")
        tulis.write("echo '\x1b[1;31m              @@@@          @@@@@@@@@@@          @@@@'\n")
        tulis.write("echo '\x1b[1;31m           @@@@@              @@@@@@@              @@@@@'\n")
        tulis.write("echo '\x1b[1;31m          @@@@@@@                                 @@@@@@@'\n")
        tulis.write("echo '\x1b[1;31m           @@@@@                                   @@@@@ \necho ''\n")
        tulis.write("echo '\x1b[1;36m                        =[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        tulis.write("echo '\x1b[1;37m                     ====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        tulis.write("echo ''\n")
        tulis.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def nag():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        nag()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write('echo\n')
        t.write("echo '\x1b[96m                     ______________'\n")
        t.write("echo '                ,===:.,            `-._'\n")
        t.write("echo '                `:.`---.__         `-._'\n")
        t.write("echo '                  `:.     `--.         `.'\n")
        t.write("echo '                  `:.     `--.         `.'\n")
        t.write("echo '            (,,(,    \\.         `.   ____,-`.,'\n")
        t.write("echo '         (,      `/   \\.   ,--.___`.'\n")
        t.write("echo '     ,  ,  ,--.   `,   \\. ;`'\n")
        t.write("echo '      `{\x1b[92mD\x1b[97m,{     \\  :    \\ ;  '\n")
        t.write("echo ' \x1b[97m       V,,     /  /    //'\n")
        t.write("echo '        j;;    /  ,  ,-//.    ,---.      ,'\n")
        t.write("echo '        \\;    /  ,  /  _  \\  /  _  \\   , /'\n")
        t.write("echo '              \\   `   / \\  `   / \\  `.  /'\n")
        t.write("echo '               `.___,/   `.__,/   `.__,/'\n")
        t.write("echo ''\n")
        t.write("echo '\x1b[1;36m                     =[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        t.write("echo '\x1b[1;37m                  ====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def ten():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        ten()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write("echo '\x1b[97m                       .:::!~!!!!!:.'\n")
        t.write("echo '                    .xUHWH!! !!?M88WHX:.'\n")
        t.write("echo '                  .X*#M@&!!  !X!M&&&&&&WWx:.'\n")
        t.write("echo '                 :!!!!!!?H! :!&!&&&&&&&&&&8X:'\n")
        t.write("echo '                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'\n")
        t.write("echo '               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'\n")
        t.write("echo '               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'\n")
        t.write("echo '                 !:~~~ .:!MST#&&&&WX??#MRRMMM!'\n")
        t.write("echo '                 ~?WuxiW*`   `√#&&&&8!!!!??!!!'\n")
        t.write("echo '               :X- M&&&&       `rT#&T~!8&WUXU~'\n")
        t.write("echo '              :%`  ~#&&&m:    \x1b[91m✪   \x1b[97m~!~ ?&&&&&&'\n")
        t.write("echo '            :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'\n")
        t.write("echo ' .......   -~~:<` !    ~?T#&&@@W@*?&&   \x1b[91m✪  \x1b[97m/`'\n")
        t.write("echo '\x1b[92mG \x1b[97m|W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'\n")
        t.write("echo '\x1b[92mH \x1b[97m|#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'\n")
        t.write("echo '\x1b[92mO \x1b[97m|:::~:!!`:X~ .: ?H.!u °&&&B&&&!W:U!T&&M~'\n")
        t.write("echo '\x1b[92mS \x1b[97m|.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'\n")
        t.write("echo '\x1b[92mT \x1b[97m|Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'\n")
        t.write("echo ' .......         /   ~&&&&&B&&en:``'\n")
        t.write("echo '\x1b[97m                     ~`##*&&&&M~'\n")
        t.write("echo ''\n")
        t.write("echo '\x1b[1;36m                     =[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        t.write("echo '\x1b[1;37m                  ====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def nam():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama banner Figlet : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        nam()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write('figlet ' + aut + ' | lolcat\n')
        t.write("echo '\x1b[1;37m===================='\n")
        t.write("echo '\x1b[1;33m Welcome To Termux  '\n")
        t.write("echo '\x1b[1;37m===================='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def bl():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        bl()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write("echo '\x1b[92m     ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄██▀    ██░ ██  ▄▄▄     ▄▄▄██████▓'\n")
        t.write("echo '    ▓███▄ ▓██░   ░███▄    ░▓█  ▀█ ▄██░    ░██░██░██░██░██▄   ▓█  ██░ ▓░'\n")
        t.write("echo '    ░██ ▄█░██░   ░██  ▀█▄  ░▓██▀▀█▓██░    ░▓█▄█▓ ░▓███▀░▀██▄ ░▓███▀░ ▓█░'\n")
        t.write("echo '    ░██▀█▄░██░   ░██▄▄▄██░   ░██▄▄█▓██▄     ░██░ ░▓█  ▄█▄ ██░ ░▓█  ▒ ▓█░'\n")
        t.write("echo '    ░██▓ ███░   ░▓█▓ ░██░   ░▓▓█ ░██░     ░█▓ ░██▓░ ▓█   ░██░ ░██░  ▓█ '\n")
        t.write("echo '    ░▓█   ░     ░▓    ░     ░▓    ░      ░▓  ░ ░   ░▓    ░     ░▓   ░  '\n")
        t.write("echo '\x1b[90m    ░          ░  ░  \x1b[1;36m=[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        t.write("echo '\x1b[1;37m                  ====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def fb():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        fb()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write("echo '\x1b[97m█████████      \x1b[96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●'\n")
        t.write("echo '\x1b[97m█▄████▄█ \x1b[0m__--\x1b[92m╔╦╗╔═╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗╔═╗'\n")
        t.write("echo '\x1b[97m█ \x1b[91m▀▀▀▀▀\x1b[0m_---_--\x1b[92m║║║╠═╣╚═╗╠╩╗╚═╗║╣ ╠═╣║ ║╠═╣'\n")
        t.write("echo '\x1b[97m█   \x1b[0m--_-- --_ \x1b[92m║║║║ ║╚═╝╚═╝╚═╝╚═╝║ ║╚═╝║ ║'\n")
        t.write("echo '\x1b[97m█ \x1b[91m▄▄▄▄▄\x1b[0m -_-- -\x1b[92m╚╩╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝'\n")
        t.write("echo '\x1b[97m█████████      \x1b[96m«°°°°°°°°°✧°°°°°°°°°»'\n")
        t.write("echo '\x1b[97m ██ ██'\n")
        t.write("echo '\x1b[37m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'\n")
        t.write("echo ''\n")
        t.write("echo '\x1b[1;36m   =[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        t.write("echo '\x1b[1;37m====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def ano():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        ano()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write("echo '\x1b[31;1m                        `/ymMMMMMMMMmy/`'\n")
        t.write("echo '                    `/ymMMMMMMMMMMMMMMmy/`'\n")
        t.write("echo '                   /hMMMMMMMMMMMMMMMMMMMMMMh/'\n")
        t.write("echo '                 /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/'\n")
        t.write("echo '               `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`'\n")
        t.write("echo '              .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.'\n")
        t.write("echo '             `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`'\n")
        t.write("echo '             ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys'\n")
        t.write("echo '            `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`'\n")
        t.write("echo '            -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-\x1b[37;1m'\n")
        t.write("echo '            -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-'\n")
        t.write("echo '            `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh'\n")
        t.write("echo '             s+-s-odmNNN`     /-:/     .NNNmd+:s-+s'\n")
        t.write("echo '             `mo/-:+ymMm                mMms+:-/om`'\n")
        t.write("echo '              .h/+/y`hhs                yyh`y/+/h.'\n")
        t.write("echo '               `hd/::-+.                .+-::/dy`'\n")
        t.write("echo '                 /hs+/::.--          --.::/+sh:'\n")
        t.write("echo '                   :hds+/-`          `-/+sdh:'\n")
        t.write("echo '                     `/ymM+          oMmy:'\n")
        t.write("echo '                         \x1b[41m W E L C O M E \x1b[0m'\n")
        t.write("echo ''\n")
        t.write("echo '\x1b[1;36m                     =[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        t.write("echo '\x1b[1;37m                  ====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;34m╭───\x1b[1;31m≼\x1b[1;33m" + nt + "\x1b[1;34m•\x1b[1;30m\\w\x1b[1;34m≽ \n\x1b[1;34m╰──╼\x1b[1;31m✠\x1b[1;32m ' \n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

def ter():
    os.system('clear')
    wr(ban)
    print(k + 'Isi Data Berikut :')
    sleep(2)
    aut = input(b + 'Nama di bagian Author : ' + p)
    print(u + '=========================')
    nt = input(b + 'Nama buat di terminal : ' + p)
    print(u + '=========================')
    if aut == '' or nt == '':
        print(m + 'Isi yg bener!')
        sleep(2)
        ter()
    else:
        tik()
        t = open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w')
        t.write('#Author : ANKER\n#Github : ANKER \n#Youtube\n')
        t.write('clear\nsleep 2.1\n')
        t.write("echo '\x1b[31m      ████████ ██   ██ ██    ██ ██    ██ ███    ██ ██   ██ '\n")
        t.write("echo '        ██    ██   ██ ██    ██ ██    ██ ████   ██ ██   ██ '\n")
        t.write("echo '         ██    ███████ ██    ██ ██    ██ ██ ██  ██ ███████ '\n")
        t.write("echo '         ██    ██   ██ ██    ██ ██    ██ ██  ██ ██     ██ '\n")
        t.write("echo '         ██    ██   ██  ██████   ██████  ██   ████      ██ '\n")
        t.write("echo ''\n")
        t.write("echo '\x1b[1;36m                     =[ \x1b[1;37mCoded \x1b[1;33mby\x1b[1;32m " + aut + " \x1b[1;36m]='\n")
        t.write("echo '\x1b[1;37m                  ====[ \x1b[1;32mWelcome To Termux \x1b[1;37m]===='\n")
        t.write("echo ''\n")
        t.write("PS1='\x1b[1;36m╭\x1b[1;37m[\x1b[1;32m" + nt + "\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;33m\\d\x1b[1;37m]\x1b[1;36m—\x1b[1;37m[\x1b[1;35m \\w \x1b[1;37m]\n\x1b[1;36m╰───\x1b[1;33m▶ \x1b[1;37m'\n")
        print(p + '\n[' + h + '✓' + p + ']' + k + 'Berhasil')
        print(p + 'Ketik login untuk mencoba')

os.system('clear')
wr(ban)
wr(b + '               [\x1b[1;41m\x1b[1;37mJenis Style\x1b[00m\x1b[1;36m]')
wr(u + '╔════════════════════════════════════════════════╗')
wr(u + '║ \x1b[1;37m[\x1b[1;32m1\x1b[1;37m]\x1b[1;33mRedskull                     \x1b[1;37m[\x1b[1;32m5\x1b[1;37m]\x1b[1;33mBlackhat\x1b[1;35m    ║')
wr(u + '║ \x1b[1;37m[\x1b[1;32m2\x1b[1;37m]\x1b[1;33mNaga                         \x1b[1;37m[\x1b[1;32m6\x1b[1;37m]\x1b[1;33mDarkFB\x1b[1;35m      ║')
wr(u + '║ \x1b[1;37m[\x1b[1;32m3\x1b[1;37m]\x1b[1;33mTengkorak                    \x1b[1;37m[\x1b[1;32m7\x1b[1;37m]\x1b[1;33mAnonymous\x1b[1;35m   ║')
wr(u + '║ \x1b[1;37m[\x1b[1;32m4\x1b[1;37m]\x1b[1;33mNama                         \x1b[1;37m[\x1b[1;32m8\x1b[1;37m]\x1b[1;33mTermux\x1b[1;35m      ║')
wr(u + '╠════════════════════════════════════════════════╣')
wr(u + '║ \x1b[1;37m[\x1b[1;32m0\x1b[1;37m]\x1b[1;33mExit')
pil = input(u + '║\n╚' + k + '▶ ' + h + 'Pilih ' + p + '> ' + b)

if pil == '0':
    keluar()
elif pil == '1':
    red()
elif pil == '2':
    nag()
elif pil == '3':
    ten()
elif pil == '4':
    nam()
elif pil == '5':
    bl()
elif pil == '6':
    fb()
elif pil == '7':
    ano()
elif pil == '8':
    ter()