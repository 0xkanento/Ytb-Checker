import requests


print("""
██╗   ██╗████████╗██████╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚██╗ ██╔╝╚══██╔══╝██╔══██╗    ██╔════╝██║  ██║██╔════╝ ██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ╚████╔╝    ██║   ██████╔╝    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
  ╚██╔╝     ██║   ██╔══██╗    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║      ██║   ██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝      ╚═╝   ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")



#Banner
print("""

      [-] Username Checker [-]
             [ Youtube ]
        ======================================= 
        [+] Developper : Kanento.             |
        [+] Discription: A username Checker.  |
        [+] Discord : Kanento#6882            |
        [+] Credit :  0xkanento               |
        =======================================
  
""")
#Banner

def insta():

  

  url = "https://www.youtube.com/c/"
  username = input("[?] Enter the username : ")
 
  headers={
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
   
  }
  
  r = requests.get(f"{url}{username}", headers=headers)
  
  
  if (r.text.__contains__('Not Found')):
    print("Your username is not taken")
  else:
    print('Your username is taken')

  
  
  
#

if __name__ == "__main__":
  insta()









