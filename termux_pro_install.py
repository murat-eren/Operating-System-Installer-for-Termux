import os
os.system("clear")



###I SPENDED 10 MINUTES ON THIS BANNER RESPECT FOR LABOR


print ("Files to Install :")
print("\033[91m   _______________  \033[0m")
print("   \\\033[94m Kali  \033[0m       \\")
print("\033[91m    \\==============\\\033[0m")
print("     \\ \033[94mUbuntu  \033[0m     \\")
print("\033[91m      \\==============\\\033[0m")
print("       \\\033[94m Debian  \033[0m     \\")
print("\033[91m        \\==============\\\033[0m")
print("         \\ \033[94mArch Linux \033[0m  \\")
print("\033[91m          \\==============\\\033[0m")    
print("           \\ \033[94mManjaro  \033[0m    \\")
print("\033[91m            \\==============\\\033[0m")      
print("             \\ \033[94mFedora    \033[0m   \\")
print("\033[91m              \\==============\\\033[0m")            
print("               \\ \033[94mVoid  \033[0m       \\")
print("\033[91m                \\==============\\")          
print("                 \\\033[94m Alpine    \033[0m   \\\033[0m")
print("\033[91m                  \\______________\\\033[0m")          


print("""




""")
print("Press Any Key to Continue ")
print("to get out press  \033[91m Ctrl+C\033[0m ")
try:
    input(" ")
    os.system("clear")
    #package insttall
    os.system("pkg update-y")
    os.system("pkg install curl proot tar -y")
    os.system("")
    
    ################################################
    print("Kali Linux Installing")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash")
    os.system("clear")
    print("Kali Was established")
    ################################################
    print("Ubuntu Installing")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
    os.system("clear")
    print("Ubuntu Was established")
    ################################################
    print("Debian Installing")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
    os.system("clear")
    print("Debian Was established")
    ################################################
    print("Arch Linux Installing")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
    os.system("clear")
    print("Arch Linux Was established")
    ################################################
    print("Manjaro Installing")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
    os.system("clear")
    print("Manjaro Was established")
    ################################################
    print("Fedora Was established")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
    os.system("clear")
    print("Fedora Was established")
    ################################################
    print("Void Was established")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash")
    os.system("clear")
    print("Void Was established")
    ################################################
    print("Alpine Installing")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
    os.system("clear")
    print("Alpine Was established")
    print("""\033[91m



                 INSTALLATION IS COMPLETED
    BECAUSE THE PROGRAMS ARE HIDDEN, YOU CAN CONTROL WITH THE COMMAND "ls -la"
             EXAMPLE COMMAND : "./start-kali.sh"
    \033[0m""")
except:
    print("By Bye")





