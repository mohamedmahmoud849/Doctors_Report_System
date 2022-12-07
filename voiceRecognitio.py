import speech_recognition as sr
import pyttsx3
import ReportWriter as rw
import Mail
import sqlite3

def test():
    print("test")
    
def speak(message):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 10)
    engine.say('{}'.format(message))
    engine.runAndWait()


def addrecord(name, Patemail, arr):
    patientname = name
    patemail = Patemail
    admitteddate = arr[0]
    reasonforadmission = arr[1]
    pasthistory = arr[2]
    progress = arr[3]
    currentcondition = arr[4]
    prognosis = arr[5]
    labresults = arr[6]
    currentmedication = arr[7]
    arrangements = arr[8]
    conn = sqlite3.connect('Hospital.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Reports (PatientName TEXT,Email TEXT,q1 TEXT,q2 TEXT,q3 TEXT,q4 TEXT,q5 TEXT,q6 TEXT,q7 TEXT, q8 TEXT,q9 TEXT)')
    cursor.execute(
        'INSERT INTO Reports (PatientName,Email,q1,q2,q3,q4,q5,q6,q7,q8,q9 ) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
        (
            patientname, patemail, admitteddate, reasonforadmission, pasthistory, progress, currentcondition,
            prognosis,
            labresults, currentmedication, arrangements))
    print("done")
    conn.commit()





def ask(name , email) :    
    data = []
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    print(sr.Microphone.list_microphone_names())
    questions = ["When were they admitted to your hospital?", "Reason for admission and medical diagnosis ",
             "Past medical history (if known)", "Progress on ward", "Current clinical condition",
             "Prognosis and prospects for rehabilitation", "Relevant laboratory results, x-rays etc",
             "Current medication ", "Arrangements to follow up "]
    for question in questions:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            while 1:
                speak(question)
                try:
                    audio = r.listen(source)
                    print("Recognizing now..")
                    text = r.recognize_google(audio)
                    data.append(text)
                    print(text)
                    speak("you said" + text)
                    break
                except:
                    speak("i didn't hear you clearly")
    rw.fill(name,email,data)
    addrecord(name,email,data)
    Mail.send_email(name, email)               





