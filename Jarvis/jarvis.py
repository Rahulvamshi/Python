import speech_recognition as sr
import os
import pyttsx3
import ctypes
import webbrowser as w
import time
import keyboard as key
import subprocess as app

try:
    engine=pyttsx3.init()
except ImportError:
        print('Driver not found')
except RuntimeError:
        print("Not initialized")
        
    
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate=engine.getProperty('rate')
engine.setProperty('rate',rate)    

def talk(cmd):
    engine.say(cmd)
    engine.runAndWait()

def aye(cmd):
    os.startfile(cmd)
    time.sleep(2)    
def close_app(app):
    try:
        os.system('TASKKILL /F /IM '+app+'.exe')
    except Exception as e:
        print(e)    
def take_input():
      r = sr.Recognizer()
      with sr.Microphone() as source:
          #aye('happy.mp3')
          print('Ready')
          print('Listening')
          #r.adjust_for_ambient_noise(source, duration=0.1)
          audio = r.listen(source)
      try:
          command =r.recognize_google(audio)
          print(command)
          a=process_the_speech(command)
          return a
      except Exception as e:
          print(e)
      
      except:
          talk("Sorry i didn\'t get you")
          print("Sorry i didn\'t get you")  
 
def search_input():
      r = sr.Recognizer()
      with sr.Microphone() as source:
          #aye('happy.mp3')
          print('TEll me')
          r.adjust_for_ambient_noise(source, duration=0.1)
          audio = r.listen(source)
      try:
          command =r.recognize_google(audio)
          print(command)
          return command
      except:
          talk("Sorry can you repeate")
       
def process_the_speech(command):
    if 'hello' in command:
        talk('Hai sir')
        
    elif 'happy' in command:
        aye('happy.mp3')
    
    elif 'lock the screen' in command:
        talk('Give me a second')
        ctypes.windll.user32.LockWorkStation()
    
    elif 'open Chrome' in command:
         talk('Give me a second')
         talk('Wait')
         talk('Should i must search anything or just open it')
         c=search_input()
         if 'search' in c:
             talk('Tell m what to search')
             s=search_input()
             talk('Give me a second')
             search_terms = [c]
             for term in search_terms:
                 url = "https://www.google.com.tr/search?q={}".format(term)
                 w.open_new_tab(url)
         else:
            try:
             app.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
         
            except Exception as e:
             print(e)

    elif 'open Facebook' in command:
         talk('Give me a second')
         w.open('https://www.facebook.com/')  
         
    elif 'open YouTube' in command:
         talk('Give me a second')
         talk('Wait')
         talk('Should i must search anything or just open it')
         c=search_input()
         if 'search' in c:
             talk('Tell m what to search')
             s=search_input()
             talk('Give me a second')
             search_terms = [s]
             for term in search_terms:
                  url = "https://www.youtube.com/results?search_query={}".format(term)
                  w.open_new_tab(url)
                  key.press('end')
         else:
             talk('Give me a second')
             w.open('https://www.youtube.com/?gl=IN')
             
             
    elif 'open mail' in command:
         talk('Give me a second')
         w.open('https://mail.google.com')       
    
    elif 'Google' in command:
         talk('Give me a second')
         w.open('https://www.google.com')
    
    elif 'stop' in command:
        return 'S'

    
    elif 'wait' in command:
        talk('Okay')
        time.sleep(20)
    
    elif 'unlock the screen' in command:
        #key.press('enter')
        key.press('2,0,0,1')
        key.press('enter')

        
    
    elif 'close an application' in command:
          talk('Which application should i must Close')
          c=search_input()
          close_app(c)
        
    elif 'tell about yourself' in command:
        talk('Okay')
        talk('My name is happy')
        talk('I was created by Rahul')
        talk('i can do any thing you say')
        talk('Note to use me you must have internet')
    
    elif 'go to sleep mode' in command: 
        try:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return 'S'
        except Exception as e:
            talk('Sir their is a problem')
            print(e)
    elif 'scroll down' in command:
        key.press('page on')

while True:
    a=take_input()
    if a=='S':
        break


