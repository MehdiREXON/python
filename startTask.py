import os,glob
import gnupg
from time import sleep
from getpass import getpass
from colorama import Fore
from colorama import Style
gpg = gnupg.GPG(gnupghome='/home/'+os.getlogin()+'/.gnupg')
gpg.encoding = 'utf-8'
appPath = os.getcwd()

clean = lambda: os.system('tput reset')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Program:
    __key = '';
    __username = os.getlogin()
    __version = "1.0.0"
    __author = "Mehdi ghazanfari"
    __information = []
    publicKey = ''
    
    #not fixed yet!!!!!!!!!!!!!!!!!
    def __init__(self):
        pass
    #fixed
    def returnKey(self):
        return (self.__key)
    #need to be fixed for more options
    def showItems(self):
        clean()
        print(f"{Fore.RED}[1]{Fore.GREEN} generate a new key\n" )
        print(f"{Fore.RED}[2]{Fore.GREEN} remove a key (need fingerprint)\n" )
        print(f"{Fore.RED}[3]{Fore.GREEN} show key's information\n")
        print(f"{Fore.RED}[4]{Fore.GREEN} start encrypting any files in the directory of the application(be careful!)\n")
        print(f"{Fore.RED}[5]{Fore.GREEN} start decrypting any files in the directory of the application\n")
        print(f"{Fore.RED}[6]{Fore.GREEN} about us\n")
        print(f"{Fore.RED}[7]{Fore.GREEN} exit the program\n{Fore.RESET}")
    #fix th numbers
    def getOption(self):
        option = int(input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your option ... {Fore.RESET}"))
        if option == 1:
            self.getData()
            self.generate_key()
            self.__re()
        elif option == 2:
            self.removeKey()
        elif option == 3:
            self.keysInformations()
            self.__re()
        elif option == 4:
            if self.__information == []:
                self.getData()
            self.startEncryption()
            self.__re()
        elif option == 5:
            if self.__information == []:
                self.getData()
            self.startDecryption()
            self.__re()
        elif option == 6:
            self.aboutUs()
            self.__re()
        elif option == 7:
            print(f"{Fore.YELLOW}the program will terminate in 5 seconds{Fore.RESET}")
            sleep(5)
            os._exit(0)
    #fixed
    def getData(self):
        email = input("enter your email address : ")
        passphrase = getpass("Enter your passphrase : ")
        length = input("Enter key's length(default 1024) : ")
        key_type = input("Enter key's type(RSA is default) : ")
        self.__information = [email, passphrase, length, key_type]
    #maybe fixed
    def generate_key(self):
        inputData = gpg.gen_key_input(
        name_email = self.__information[0],
        passphrase = self.__information[1],
        key_type= self.__information[3],
        key_length = self.__information[2]
        )
        self.__key = gpg.gen_key(inputData)
    #maybe fixed
    def removeKey(self):
        try:
            if(self.__key == ''):
                raise Exception(f"{Fore.RED}[- output]{Fore.YELLOW}you did not entered any key to the program or it's not valid.at first please specify a key.{Fore.RESET}")
            else:
                passcode = input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your passphrase {Fore.RESET}")
                result = gpg.delete_keys(self.__key,secret=True,passphrase=passcode)
                if result.status == 'No such key':
                    raise Exception(f"{Fore.RED}[- output]{Fore.YELLOW}your key is not valid.try again{Fore.RESET}")
                else:
                    gpg.delete_keys(self.__key,passphrase=passcode)
                    print(f"{Fore.RED}[- output]{Fore.YELLOW}the key deleted successfully{Fore.RESET}")
            
        except Exception as error:
            print(error)
            self.__key = input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW}enter your key fingerprint{Fore.RESET}")
            self.removeKey()
            self.__re()
    #fixed
    def aboutUs(self):
        clean()
        print(f"{Fore.RED}[author]{Fore.GREEN} " + self.__author + f'\n{Fore.RESET}' )
        print(f"{Fore.RED}[discord]{Fore.GREEN} ItsOverflow#2755\n" )
        print(f"{Fore.RED}[email]{Fore.GREEN} m.ghazanfari1384@gmail.com\n")
        print(f"{Fore.RED}[currect version]{Fore.GREEN} " + self.__version + f'\n{Fore.RESET}')
    #fixed
    def __re(self):
        try:
            result =int( input(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}to return to menu press {Fore.RED}-1{Fore.RESET} and for exit press {Fore.RED}0{Fore.RESET}...\n"))
            if result == -1:
                self.showItems()
                self.getOption()
                return -1
            elif result == 0:
                return os._exit(0)
            else:
                raise Exception(f"{Fore.RED}[- output]{Fore.YELLOW}entered value is not valid.try again{Fore.RESET}")
        except Exception as error:
            print(error)
            self.__re()
    #need to be fixed
    def importKey(self,key):
        self.publicKey = key
    #fixed
    def keysInformations(self):
        print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}public keys are these :{Fore.RED}\n")
        publicKeys = gpg.list_keys(False)
        print(publicKeys)

        print(f"{Fore.MAGENTA}\n[- output]{Fore.YELLOW}private keys are these :{Fore.RED}\n")
        privateKeys = gpg.list_keys(True)
        print(privateKeys)    
    #need to be fixed
    def exportKeys(self):
        pass
    #fixed
    def startEncryption(self):

        print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}choose one of these to encrypt\n{Fore.RESET}")

        data = os.listdir(appPath)

        for this in data:
            print(f"{Fore.RED}[+] {Fore.RESET}"+this + '\n')
        selectedFile =input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW} which one?type full name of it\n{Fore.RESET}")    

        selectedFilePath = os.path.abspath(selectedFile)

        with open(selectedFilePath, 'rb') as file:
            status = gpg.encrypt_file(file,recipients= [self.__information[0]],output= os.path.splitext(selectedFilePath)[0] + '.safe' )

        print(f"{Fore.RED}"+status.stderr) 
        print(f"{Fore.RED}"+status.status+ f"{Fore.RESET}")
    #fixed
    def startDecryption(self):
        print(f"{Fore.MAGENTA}[- output]{Fore.YELLOW}we found this/these files that have crypted\n{Fore.RESET}")
    
        for file in glob.glob("*.safe"):
            print(f"{Fore.RED}"+file)

        selectedFile =input(f"{Fore.LIGHTGREEN_EX}[+ input]{Fore.YELLOW} which one?type full name of it\n{Fore.RESET}")
        selectedFilePath = os.path.abspath(selectedFile)

        with open(selectedFilePath, 'rb') as file:
            status = gpg.decrypt_file(file,passphrase = self.__information[1],output= os.path.splitext(selectedFilePath)[0])

        print(f"{Fore.RED}"+status.stderr) 
        print(f"{Fore.RED}"+status.status+ f"{Fore.RESET}")

app = Program()

app.showItems()
app.getOption()
