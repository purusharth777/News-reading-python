import json
import requests

def speak(str):
    from win32com.client import Dispatch as p
    u=p("Sapi.SpVoice")
    u.Speak(str)
if __name__ == '__main__':
   url=requests.get("News api here").text
   news=json.loads(url)
   arts=news['articles']
   print(news['status'])
   for i in arts:
       speak(i['title'])
       for j in arts:
        speak(j['description'])


