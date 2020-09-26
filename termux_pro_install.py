import os
os.system("clear")



###BU BANNERA 10 DK Mİ HARCADIM EMEĞE SAYGI


print ("Kurulacak Dosyalar :")
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
print("Devam Etmek Icin Herhangi Bir Tusa Basin ")
print("Cikmak Icin Ise \033[91m Ctrl+C\033[0m 'ye Basiniz.")
try:
    input(" ")
    os.system("clear")
    #package insttall
    os.system("pkg update-y")
    os.system("pkg install curl proot tar -y")
    os.system("")
    
    ################################################
    print("Kali Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash")
    os.system("clear")
    print("Kali Kuruldu")
    ################################################
    print("Ubuntu Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
    os.system("clear")
    print("Ubuntu Kuruldu")
    ################################################
    print("Debian Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
    os.system("clear")
    print("Debian Kuruldu")
    ################################################
    print("Arch Linux Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
    os.system("clear")
    print("Arch Linux Kuruldu")
    ################################################
    print("Manjaro Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
    os.system("clear")
    print("Manjaro Kuruldu")
    ################################################
    print("Fedora Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
    os.system("clear")
    print("Fedora Kuruldu")
    ################################################
    print("Void Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash")
    os.system("clear")
    print("Void Kuruldu")
    ################################################
    print("Alpine Kuruluyor")
    os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
    os.system("clear")
    print("Alpine Kuruldu")
    print("""\033[91m



                 KURULUM İŞLEMİ TAMAMLANDI 
    PROGAMLAR GİZLİ OLDUĞU İÇİN "ls -la" KOMUDU İLE KONTROL EDEBİLİRSİNİZ
             EXAMPLE COMMAND : "./start-kali.sh"
    \033[0m""")
except:
    print("By Bye")





