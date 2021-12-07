import schedule
import time
import webbrowser
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 180) # if you want to set speaking speed 
# engine.setProperty('voice','voices[1].id') for female voice 
engine.runAndWait()

def speak(audio):

    engine.say(audio)
    engine.runAndWait() 
 
# Save the file as .pyw
# And set this at this position 
'''C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'''
      
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def eco():
  speak ("Its Economics class now") 


def launch0():    
 url= 'https://us04web.zoom.us/j/79814235033?pwd=U014K0l4Z1ZhcjN1OWk0OEsxajNjQT09'
 webbrowser.open_new_tab(url)     



def eng():
       speak("Its English class now!!")
 
  
def launch2():
    url= 'https://us05web.zoom.us/j/9719627196?pwd=OVV5Y09nempaN3lGL0NVRzJiSHgwdz09'
    webbrowser.open_new_tab(url)     
 

def BS():
     speak("Its Business Studies class now!!")

def launch3():
    url= ' https://us04web.zoom.us/j/4711097803?pwd=TWkvVERmZkRsSU1yQ0VmOXAyaVJQUT09'
    webbrowser.open_new_tab(url)   
   



def ac():
    speak("Its Accounts class now!!")

def launch4():
    url= 'https://us04web.zoom.us/j/3158952513?pwd=bllXYW5UK1I2TysvRGc5cUhGbUwwZz09'
    webbrowser.open_new_tab(url)   
    




def comp():
    speak("Its Computer class now")

def launch5():
    url= 'https://us04web.zoom.us/j/6366119606?pwd=VFlORUdDOVB0b0p1OU9TZS9SakZLZz09'
    webbrowser.open_new_tab(url)   
 

def assembly():
    speak("Its assembly Time.Bro ")

def launch6():
    url= 'https://us04web.zoom.us/j/3321067982?pwd=MitCaTV4R3VpV1VtZ0JabkhDQ2o2Zz09'
    webbrowser.open_new_tab(url)   
    

def ss():
    speak ("THIS YOUR SELF STUDY PERIOD!!  BRO!!!.  AND YOU HAVE TO DO THE SAME!!!.   PLEASE BRO!!!")


# assembly 
schedule.every().day.at("08:40").do(assembly)
schedule.every().day.at("08:40").do(launch6)

# mon
schedule.every().monday.at("09:00").do(eng)
schedule.every().monday.at("09:45").do(BS)
schedule.every().monday.at("10:30").do(comp)
schedule.every().monday.at("11:20").do(eco)
schedule.every().monday.at("12:05").do(eco)

schedule.every().monday.at("09:00").do(launch2)
schedule.every().monday.at("09:45").do(launch3)
schedule.every().monday.at("10:30").do(launch5)
schedule.every().monday.at("11:20").do(launch0)
schedule.every().monday.at("12:05").do(launch0)
# tue
schedule.every().tuesday.at("09:00").do(comp)
schedule.every().tuesday.at("09:45").do(BS)
schedule.every().tuesday.at("10:30").do(eco)
schedule.every().tuesday.at("11:20").do(ac)
schedule.every().tuesday.at("12:05").do(ac)

schedule.every().tuesday.at("09:00").do(launch5)
schedule.every().tuesday.at("09:45").do(launch3)
schedule.every().tuesday.at("10:30").do(launch0)
schedule.every().tuesday.at("11:20").do(launch4)

# wed
schedule.every().wednesday.at("09:00").do(eng)
schedule.every().wednesday.at("09:45").do(eco)
schedule.every().wednesday.at("10:30").do(ac)
schedule.every().wednesday.at("11:20").do(ss)
schedule.every().wednesday.at("12:05").do(ss)

schedule.every().wednesday.at("09:00").do(launch2)
schedule.every().wednesday.at("09:45").do(launch0)
schedule.every().wednesday.at("10:30").do(launch4)
schedule.every().wednesday.at("11:20").do(ss)
schedule.every().wednesday.at("12:05").do(ss)

# thurs
schedule.every().thursday.at("09:00").do(eng)
schedule.every().thursday.at("09:45").do(BS)
schedule.every().thursday.at("10:30").do(ss)
schedule.every().thursday.at("11:20").do(eco)
schedule.every().thursday.at("12:05").do(eco)

schedule.every().thursday.at("09:00").do(launch2)
schedule.every().thursday.at("09:45").do(launch3)
schedule.every().thursday.at("11:20").do(launch0)
schedule.every().thursday.at("12:05").do(launch0)
# fri
schedule.every().friday.at("09:00").do(comp)
schedule.every().friday.at("09:45").do(comp)
schedule.every().friday.at("10:30").do(ac)
schedule.every().friday.at("11:20").do(BS)
schedule.every().friday.at("12:05").do(ac)

schedule.every().friday.at("09:00").do(launch5)
schedule.every().friday.at("09:45").do(launch5)
schedule.every().friday.at("10:30").do(launch4)
schedule.every().friday.at("11:20").do(launch3)
schedule.every().friday.at("12:05").do(launch4)
# sat
schedule.every().saturday.at("09:00").do(eng)
schedule.every().saturday.at("09:45").do(BS)
schedule.every().saturday.at("10:30").do(ac)
schedule.every().saturday.at("11:20").do(BS)
schedule.every().saturday.at("12:05").do(eng)

schedule.every().saturday.at("09:00").do(launch2)
schedule.every().saturday.at("09:45").do(launch3)
schedule.every().saturday.at("10:30").do(launch4)
schedule.every().saturday.at("11:20").do(launch3)
schedule.every().saturday.at("12:05").do(launch2)


while True:
    schedule.run_pending()
    time.sleep(1)