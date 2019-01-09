import speech_recognition as sr
import os
print('1.System montoring\n2.Text encryption and decryption\n')
b=int(input('enter your option:'))
if b==1:
        print('1.Music \n2.Pictures\n3.Downloads\n4.Documents\n5.Videos\n6.softwares')
        a=int(input('enter your option:'))
        if(a==1):
                print('1.vida1.mp3 \n2.vidya2.mp3 \n3.vidy3.mp3 \n5.one.mp3 \n6.three.mp3\n')
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('Say Something')
                    audio=r.listen(source)
                    d=r.recognize_google(audio)
                    print(d)
                    if d=='1':
                        os.startfile('C:\\Users\\User\\Music\\vv\\vidya1.mp3')
                    elif d=='2':
                        os.startfile('C:\\Users\\User\\Music\\vv\\vidya2.mp3')
                    elif d=='3':
                        os.startfile('C:\\Users\\User\\Music\\vv\\vidya3.mp3')
                    elif d=='4':
                        os.startfile('C:\\Users\\User\\Music\\vv\\one.mp3')
                    elif d=='5':
                        os.startfile('C:\\Users\\User\\Music\\vv\\two.mp3')
                    elif d=='6':
                        os.startfile('C:\\Users\\User\\Music\\vv\\three.mp3')
                    else:
                        pass
        elif(a==2):
                print('1.sam \n2.Rasi \n3.Niveda\n4.Korean\n')
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('Say Something')
                    audio=r.listen(source)
                    d=r.recognize_google(audio)
                    print(d)
                    if(d=='Sam'):
                        os.startfile('C:\\Users\\User\\Pictures\\Actors\\sam.jpg')
                    elif(d=='Rasi'):
                        os.startfile('C:\\Users\\User\\Pictures\\Actors\\rasi.jpg')
                    elif(d=='Niveda'):
                        os.startfile('C:\\Users\\User\\Pictures\\Actors\\nivedha.jpg')
                    elif(d=='Korean'):
                        os.startfile('C:\\Users\\User\\Pictures\\Actors\\korean.jpg')
                    else:
                        pass
        elif(a==3):
                print('\n1.projects \n2.exe files \n3.dld \n4.books \n')
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('Say Something')
                    audio=r.listen(source)
                    d=r.recognize_google(audio)
                    print(d)
                    if(d=='project'):
                        os.startfile('C:\\Users\\User\\Downloads\\project')
                    elif(d=='exe'):
                        os.startfile('C:\\Users\\User\\Downloads\\exe')
                    elif(d=='DLD'):
                        os.startfile('C:\\Users\\User\\Downloads\\dld')
                    elif(d=='books'):
                        os.startfile('C:\\Users\\User\\Downloads\\books')
                    else:
                        pass
        elif(a==4):
                print('\n1.dm \n2.flat \n3.lecture \n4.math \n5.cpp \n')
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('Say Something')
                    audio=r.listen(source)
                    d=r.recognize_google(audio)
                    print(d)
                    if(d=='DM'):
                        os.startfile('C:\\Users\\User\\Documents\\dm.pdf')
                    elif(d=='flat'):
                        os.startfile('C:\\Users\\User\\Documents\\flat.pdf')
                    elif(d=='lecture'):
                        os.startfile('C:\\Users\\User\\Documents\\lecture.pdf')
                    elif(d=='mat'):
                        os.startfile('C:\\Users\\User\\Documents\\math.pdf')
                    elif(d=='CPP'):
                        os.startfile('C:\\Users\\User\\Documents\\cpp.pdf')
                    else:
                        pass
        elif(a==5):
                print('\n1.ts\n2.karthikeya \n3.u turn \n4.vidya vox \n')
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('Say Something')
                    audio=r.listen(source)
                    d=r.recognize_google(audio)
                    print(d)
                    if(d=='TS'):
                        os.startfile('C:\\Users\\User\\Videos\\videos\\ts.mp4')
                    elif(d=='Karthikeyan'):
                        os.startfile('C:\\Users\\User\\Videos\\videos\\karthikeya.mp4')
                    elif(d=='U turn'):
                        os.startfile('C:\\Users\\User\\Videos\\videos\\uturn.mp4')
                    elif(d=='Vidya vox'):
                        os.startfile('C:\\Users\\User\\Videos\\videos\\vidya vox.mp4')
                    else:
                        pass
        elif(a==6):
                print('\n1.Firefox\n2.Google chrome\n3.Shareit\n4.Dev c++')
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print('Say Something')
                    audio=r.listen(source)
                    d=r.recognize_google(audio)
                    print(d)
                    if(d=='Firefox'):
                            os.startfile('C:\\Users\\User\\Downloads\\exe\\softwares\\Mozilla Firefox')
                    elif(d=='Google Chrome'):
                            os.startfile('C:\\Users\\User\\Downloads\\exe\\softwares\\Google Chrome')
                    elif(d=='shareit'):
                            os.startfile('C:\\Users\\User\\Downloads\\exe\\softwares\\SHAREit')
                    elif(d=='Dev'):
                            os.startfile('C:\\Users\\User\\Downloads\\exe\\softwares\\Dev-C++')
                    else:
                            pass
elif b==2:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Something')
            audio=r.listen(source)
            pt1=r.recognize_google(audio)
            print('original text:')
            print(pt1)
            s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            index=[]
            ks=[]
            ct=[]
            ct2=[]
            pt2=[]
            for j in range(len(pt1)):
                for i in range(len(s)):
                    if(pt1[j]==s[i]):
                        index.append(i)
            key=int(input('Enter any number as key:'))
            ks.append(key)
            for i in range(0,len(index)-1):
                ks.append(index[i])
            for i in range(len(ks)):
                ct.append((ks[i]+index[i])%26)
            print('cipher text:')
            print(ct)
            for i in range(len(ct)):
                ct2.append((ct[i]-ks[i])%26)
            for i in range(len(ct2)):
                pt2.append(s[ct2[i]])
            print('Original plainext:')
            print(pt2)
else:
        pass
