import smtplib
import pyttsx3
import speech_recognition as sr
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()




def get_info() :
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        try:
            info = listener.recognize_google(voice)
            print(format(info))
            return info.lower()

        except:
            talk('did not hear properly')




def send_email(rceriver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ps9800589@gmail.com','Paras@123')
    email = EmailMessage()
    email['from'] ='ps9800589@gmail.com'
    email['to'] =rceriver
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)




Name_list = {
    'paras':'ps713677@gamil.com',
    'sagar':'ps468257@gamil.com',
    'vasu':'surajsharma935991@gmail.com'
}




def get_email_info():
    talk('hi to whom you want to send email')
    name = get_info()
    rceriver= Name_list[name]
    talk('what is the subject of your email')
    subject= get_info()
    talk('what is content of your email')
    message = get_info()
    send_email(rceriver,subject,message)
    talk('hey dude your message is sent')
    talk('do you want to send more emails')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()

