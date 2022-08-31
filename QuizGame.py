from tkinter import *
import json
import random
import time
from tkinter import messagebox as Message
from tkinter.font import Font
from PIL import ImageTk,Image





#Start Button Functionality
def StartBtnFunc():
    lbl.destroy()
    lblImg.destroy()
    bt1.destroy()
    bt2.destroy()
    MainMenu()

#To display menu to select topic
def MainMenu():
     label.pack(side=TOP)
     label.place(x=450,y=0)
     Bt1.pack()
     Bt1.place(x= 450,y=120)
     Bt2.pack()
     Bt2.place(x= 450,y=220)
     Bt3.pack()
     Bt3.place(x= 450,y=320)
     Bt4.pack()
     Bt4.place(x= 450,y=420)
     Bt5.pack()
     Bt5.place(x= 450,y=520)
     Bt6.pack()
     Bt6.place(x= 450,y=620)
        
#If you press SST Button
def optionCommandHistory():
                label.destroy()
                Bt3.destroy()
                Bt4.destroy()
                Bt5.destroy()
                Bt6.destroy()
                Bt1.destroy()
                Bt2.destroy()
                HistoryQUIZ()
                
#If you press GK Button
def optionCommandGK():
                label.destroy()
                Bt3.destroy()
                Bt4.destroy()
                Bt5.destroy()
                Bt6.destroy()
                Bt1.destroy()
                Bt2.destroy()
                GKQUIZ()

#If you press COMPUTERS Button
def optionCommandComputers():
                label.destroy()
                Bt2.destroy()
                Bt3.destroy()
                Bt4.destroy()
                Bt5.destroy()
                Bt6.destroy()
                Bt1.destroy()
                ComputersQUIZ()

#If you press MATHS Button
def optionCommandMaths():
                label.destroy()
                Bt2.destroy()
                Bt3.destroy()
                Bt4.destroy()
                Bt5.destroy()
                Bt6.destroy()
                Bt1.destroy()
                MathsQUIZ()

#If you press SCIENCE Button
def optionCommandScience():
                label.destroy()
                Bt2.destroy()
                Bt3.destroy()
                Bt4.destroy()
                Bt5.destroy()
                Bt6.destroy()
                Bt1.destroy()
                ScienceQUIZ()

##If you press ENGLISH Button
def optionCommandEnglish():
                label.destroy()
                Bt2.destroy()
                Bt3.destroy()
                Bt4.destroy()
                Bt5.destroy()
                Bt6.destroy()
                Bt1.destroy()
                EnglishQUIZ()
    
            
                
        
#FOR PLAYING GK QUIZ        
class GKQUIZ:
    def __init__(self):

        #Question no
        self.no=0

        #Option Selected
        self.opt=IntVar()
        
        #correct answer variable to store answer selected by user
        self.correct_Answer=0

        #To store scores
        self.score=0

        #Index of question no
        self.index=0

        
        #next button to go to next question
        nxtButton= Button(root,bg='black',fg='white',text="NEXT",height=2,width=5,font=('bold',10),command=self.Next)
        nxtButton.pack()
        nxtButton.place(x=1270,y=689,anchor=SW)

        #ESCAPE BUTTON TO EXIT FROM GAME IN BETWEEN
        EscpButton= Button(root,bg='red',fg='white',text="ESCAPE",height=2,width=10,font=('bold',10),command=self.Escape)
        EscpButton.pack()
        EscpButton.place(x=5,y=689,anchor=SW)


        
        #varibles for clock
        self.hour=StringVar()
        self.minute=StringVar()
        self.sec=StringVar()

        HourEn=Entry(root,width=5,font=('Bold',15),textvariable=self.hour,state=DISABLED)
        HourEn.pack()
        HourEn.place(x=140,y=80)
        MinuteEn=Entry(root,width=5,font=('Bold',15),textvariable=self.minute,state=DISABLED)
        MinuteEn.pack()
        MinuteEn.place(x=210,y=80)
        SecEn=Entry(root,width=5,font=('Bold',15),textvariable=self.sec,state=DISABLED)
        SecEn.pack()
        SecEn.place(x=300,y=80)
        
        #Fonts
        self.myfont=Font(family="Helvetica",weight="bold",size=20)
        self.myfont2=Font(family="Times New Roman",weight="bold",size=20)
        self.myfont3=Font(family="Times New Roman",weight="bold",size=30)
        self.myfont4=Font(family="Times New Roman",weight="bold",size=15)

        #Lables for Time
        Timeleft=Label(text="Time Left: ",font=self.myfont2,background='white')
        Timeleft.pack()
        Timeleft.place(x=0,y=80)
        Hourlbl=Label(text="Hrs",font=self.myfont2,background='white')
        Hourlbl.pack()
        Hourlbl.place(x=140,y=25)
        Minlbl=Label(text="Min",font=self.myfont2,background='white')
        Minlbl.pack()
        Minlbl.place(x=230,y=25)
        Seclbl=Label(text="Sec",font=self.myfont2,background='white')
        Seclbl.pack()
        Seclbl.place(x=320,y=25)

        #To display score making score label
        self.var = StringVar()
        self.var.set(str(self.score))
        scorelbl=Label(root,fg="red",text="Score",font=self.myfont3,background='white')
        scorelbl.place(x=1150,y=60)
        score=Label(root,fg="black",textvariable=self.var,font= self.myfont3,background="white")
        score.pack()
        score.place(x=1260,y=60)
    

        #Changing background color from black to white
        root.config(background="white")

    
        #Function call
        self.displayQuestion()
        self.displayOption()
        self.setFunc()
        self.counter()

        
        

    #To display options,radio buttons to display option   
    def displayOption(self):
        rb1 = Radiobutton(root,variable=self.opt,value=0,text=GK[self.no]["answers"][self.index],bg="blue",height=2,width=30,font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb1.pack()
        rb1.place(x=100,y=300)
        rb2 = Radiobutton(root,variable=self.opt,value=1,text=GK[self.no]["answers"][self.index+1],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb2.pack()
        rb2.place(x=100,y=375)
        rb3 = Radiobutton(root,variable=self.opt,value=2,text=GK[self.no]["answers"][self.index+2],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb3.pack()
        rb3.place(x=100,y=450)
        rb4 = Radiobutton(root,variable=self.opt,value=3,text=GK[self.no]["answers"][self.index+3],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb4.pack()
        rb4.place(x=100,y=525)
        
        
        
        
    #To display question    
    def displayQuestion(self):
            
            ques_lbl=Label(root,background="white",fg="black",text=GK[self.no]["question"],height=5,width=75,font=self.myfont )
            ques_lbl.pack()
            ques_lbl.place(x = 0,y=150,anchor=NW)

    

    #to check whether option selected is wrong or right        
    def GetCorrectAnswerValue(self):
            self.correct_Answer= self.opt.get()

    
    #To calculate results and updating value of score
    def checkResults(self):
        
        if(GK[self.no-1]["correct_answer"]==self.correct_Answer):
            self.score+=1
        else:
            self.score+=0
            
        self.var.set(str(self.score))

        
    #Intialising the value of timer after pressing next button
    def setFunc(self):
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("30")

        
    #To decrese the counter after every 1 sec
    def counter(self):
        t=30
        while t>-1:
            (a,b)= divmod(t,60)
            self.hour.set("{0:2d}".format(00))
            self.minute.set("{0:2d}".format(00))
            self.sec.set("{0:2d}".format(b))

            try:
                root.update()
                time.sleep(1)
                t=t-1
            except:
                break

            if t==0:
                Message.showinfo("Time out")
                self.Next()
        
    #to display next question and option 
    def Next(self):
        
        if(self.no+1==len(GK)):
            self.no+=1
            self.checkResults()
            Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
            root.destroy()

        else:
            self.no+=1
            self.checkResults()
            self.displayQuestion()
            self.displayOption()
            self.setFunc()
            self.counter()

            
    #Escape Button functionality
    def Escape(self):
        
            response=Message.askquestion("EXIT","ARE YOU SURE")
            if response=="yes":
                Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
                root.destroy()

#FOR PLAYING MATHS QUIZ  
class MathsQUIZ:
    def __init__(self):

        
        #Question no
        self.no=0

        #Option Selected
        self.opt=IntVar()
        
        #correct answer variable to store answer selected by user
        self.correct_Answer=0

        #To store scores
        self.score=0

        #Index of question no
        self.index=0


        #next button to go to next question
        nxtButton= Button(root,bg='black',fg='white',text="NEXT",height=2,width=5,font=('bold',10),command=self.Next)
        nxtButton.pack()
        nxtButton.place(x=1270,y=689,anchor=SW)

        #ESCAPE BUTTON TO EXIT FROM GAME IN BETWEEN
        EscpButton= Button(root,bg='red',fg='white',text="ESCAPE",height=2,width=10,font=('bold',10),command=self.Escape)
        EscpButton.pack()
        EscpButton.place(x=5,y=689,anchor=SW)

        #varibles for clock
        self.hour=StringVar()
        self.minute=StringVar()
        self.sec=StringVar()

        HourEn=Entry(root,width=5,font=('Bold',15),textvariable=self.hour,state=DISABLED)
        HourEn.pack()
        HourEn.place(x=140,y=80)
        MinuteEn=Entry(root,width=5,font=('Bold',15),textvariable=self.minute,state=DISABLED)
        MinuteEn.pack()
        MinuteEn.place(x=210,y=80)
        SecEn=Entry(root,width=5,font=('Bold',15),textvariable=self.sec,state=DISABLED)
        SecEn.pack()
        SecEn.place(x=300,y=80)

        #Fonts
        self.myfont=Font(family="Helvetica",weight="bold",size=20)
        self.myfont2=Font(family="Times New Roman",weight="bold",size=20)
        self.myfont3=Font(family="Times New Roman",weight="bold",size=30)
        self.myfont4=Font(family="Times New Roman",weight="bold",size=15)

        #Label for time
        Timeleft=Label(text="Time Left: ",font=self.myfont2,background='white')
        Timeleft.pack()
        Timeleft.place(x=0,y=80)
        Hourlbl=Label(text="Hrs",font=self.myfont2,background='white')
        Hourlbl.pack()
        Hourlbl.place(x=140,y=25)
        Minlbl=Label(text="Min",font=self.myfont2,background='white')
        Minlbl.pack()
        Minlbl.place(x=230,y=25)
        Seclbl=Label(text="Sec",font=self.myfont2,background='white')
        Seclbl.pack()
        Seclbl.place(x=320,y=25)

        #To display score making score label
        self.var = StringVar()
        self.var.set(str(self.score))
        scorelbl=Label(root,fg="red",text="Score",font=self.myfont3,background='white')
        scorelbl.place(x=1150,y=60)
        score=Label(root,fg="black",textvariable=self.var,font= self.myfont3,background="white")
        score.pack()
        score.place(x=1260,y=60)
    

        #Changing background color from black to white
        root.config(background="white")

    

        
        #function call
        self.displayQuestion()
        self.displayOption()
        self.setFunc()
        self.counter()

        
        

    #To display options,radio buttons to display option   
    def displayOption(self):
        rb1 = Radiobutton(root,variable=self.opt,value=0,text=Maths[self.no]["answers"][self.index],bg="blue",height=2,width=30,font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb1.pack()
        rb1.place(x=100,y=300)
        rb2 = Radiobutton(root,variable=self.opt,value=1,text=Maths[self.no]["answers"][self.index+1],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb2.pack()
        rb2.place(x=100,y=375)
        rb3 = Radiobutton(root,variable=self.opt,value=2,text=Maths[self.no]["answers"][self.index+2],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb3.pack()
        rb3.place(x=100,y=450)
        rb4 = Radiobutton(root,variable=self.opt,value=3,text=Maths[self.no]["answers"][self.index+3],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb4.pack()
        rb4.place(x=100,y=525)
        
        
        
        
    #To display question    
    def displayQuestion(self):
            
            ques_lbl=Label(root,background="white",fg="black",text=Maths[self.no]["question"],height=5,width=75,font=self.myfont )
            ques_lbl.pack()
            ques_lbl.place(x = 0,y=150,anchor=NW)

    

    #to check whether option selected is wrong or right       
    def GetCorrectAnswerValue(self):
            self.correct_Answer= self.opt.get()

    
    #To calculate results and updating value of score
    def checkResults(self):
        
        if(Maths[self.no-1]["correct_answer"]==self.correct_Answer):
            self.score+=1
        else:
            self.score+=0
            
        self.var.set(str(self.score))

        
    #Intialising the value of timer after pressing next button
    def setFunc(self):
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("30")

    #To decrese the counter after every 1 sec
    def counter(self):
        t=30
        while t>-1:
            (a,b)= divmod(t,60)
            self.hour.set("{0:2d}".format(00))
            self.minute.set("{0:2d}".format(00))
            self.sec.set("{0:2d}".format(b))

            try:
                root.update()
                time.sleep(1)
                t=t-1
            except:
                break

            if t==0:
                Message.showinfo("Time out")
                self.Next()
        
    #to display next question and option 
    def Next(self):
        
        if(self.no+1==len(Maths)):
            self.no+=1
            self.checkResults()
            Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
            root.destroy()

        else:
            self.no+=1
            self.checkResults()
            self.displayQuestion()
            self.displayOption()
            self.setFunc()
            self.counter()

            
   #Escape Button functionality
    def Escape(self):
        
            response=Message.askquestion("EXIT","ARE YOU SURE")
            if response=="yes":
                Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
                root.destroy()


            
#FOR PLAYING SST QUIZ  
class HistoryQUIZ:
    def __init__(self):

        #Question no
        self.no=0

        #Option Selected
        self.opt=IntVar()
        
        #correct answer variable to store answer selected by user
        self.correct_Answer=0

        #To store scores
        self.score=0

        #Index of question no
        self.index=0
        
        #next button to go to next question
        nxtButton= Button(root,bg='black',fg='white',text="NEXT",height=2,width=5,font=('bold',10),command=self.Next)
        nxtButton.pack()
        nxtButton.place(x=1270,y=689,anchor=SW)

        #ESCAPE BUTTON TO EXIT FROM GAME IN BETWEEN
        EscpButton= Button(root,bg='red',fg='white',text="ESCAPE",height=2,width=10,font=('bold',10),command=self.Escape)
        EscpButton.pack()
        EscpButton.place(x=5,y=689,anchor=SW)

        #varibles for clock
        self.hour=StringVar()
        self.minute=StringVar()
        self.sec=StringVar()

        HourEn=Entry(root,width=5,font=('Bold',15),textvariable=self.hour,state=DISABLED)
        HourEn.pack()
        HourEn.place(x=140,y=80)
        MinuteEn=Entry(root,width=5,font=('Bold',15),textvariable=self.minute,state=DISABLED)
        MinuteEn.pack()
        MinuteEn.place(x=210,y=80)
        SecEn=Entry(root,width=5,font=('Bold',15),textvariable=self.sec,state=DISABLED)
        SecEn.pack()
        SecEn.place(x=300,y=80)

        #Fonts
        self.myfont=Font(family="Helvetica",weight="bold",size=20)
        self.myfont2=Font(family="Times New Roman",weight="bold",size=20)
        self.myfont3=Font(family="Times New Roman",weight="bold",size=30)
        self.myfont4=Font(family="Times New Roman",weight="bold",size=15)

        #Label for time
        Timeleft=Label(text="Time Left: ",font=self.myfont2,background='white')
        Timeleft.pack()
        Timeleft.place(x=0,y=80)
        Hourlbl=Label(text="Hrs",font=self.myfont2,background='white')
        Hourlbl.pack()
        Hourlbl.place(x=140,y=25)
        Minlbl=Label(text="Min",font=self.myfont2,background='white')
        Minlbl.pack()
        Minlbl.place(x=230,y=25)
        Seclbl=Label(text="Sec",font=self.myfont2,background='white')
        Seclbl.pack()
        Seclbl.place(x=320,y=25)


        #To display score making score label
        self.var = StringVar()
        self.var.set(str(self.score))
        scorelbl=Label(root,fg="red",text="Score",font=self.myfont3,background='white')
        scorelbl.place(x=1150,y=60)
        score=Label(root,fg="black",textvariable=self.var,font= self.myfont3,background="white")
        score.pack()
        score.place(x=1260,y=60)
    

        #Changing background color from black to white
        root.config(background="white")

    

    

        #function call
        self.displayQuestion()
        self.displayOption()
        self.setFunc()
        self.counter()

        
        

   #To display options,radio buttons to display option     
    def displayOption(self):
        rb1 = Radiobutton(root,variable=self.opt,value=0,text=History[self.no]["answers"][self.index],bg="blue",height=2,width=30,font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb1.pack()
        rb1.place(x=100,y=300)
        rb2 = Radiobutton(root,variable=self.opt,value=1,text=History[self.no]["answers"][self.index+1],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb2.pack()
        rb2.place(x=100,y=375)
        rb3 = Radiobutton(root,variable=self.opt,value=2,text=History[self.no]["answers"][self.index+2],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb3.pack()
        rb3.place(x=100,y=450)
        rb4 = Radiobutton(root,variable=self.opt,value=3,text=History[self.no]["answers"][self.index+3],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb4.pack()
        rb4.place(x=100,y=525)
        
        
        
        
    #To display question    
    def displayQuestion(self):
            
            ques_lbl=Label(root,background="white",fg="black",text=History[self.no]["question"],height=5,width=75,font=self.myfont )
            ques_lbl.pack()
            ques_lbl.place(x = 0,y=150,anchor=NW)

    

    #to check whether option selected is wrong or right        
    def GetCorrectAnswerValue(self):
            self.correct_Answer= self.opt.get()

    
    #To calculate results and updating value of score
    def checkResults(self):
        
        if(History[self.no-1]["correct_answer"]==self.correct_Answer):
            self.score+=1
        else:
            self.score+=0
            
        self.var.set(str(self.score))

        
    #Intialising the value of timer after pressing next button
    def setFunc(self):
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("30")

    #To decrese the counter after every 1 sec
    def counter(self):
        t=30
        while t>-1:
            (a,b)= divmod(t,60)
            self.hour.set("{0:2d}".format(00))
            self.minute.set("{0:2d}".format(00))
            self.sec.set("{0:2d}".format(b))

            try:
                root.update()
                time.sleep(1)
                t=t-1
            except:
                break

            if t==0:
                Message.showinfo("Time out")
                self.Next()
        
    #to display next question and option
    def Next(self):
        
        if(self.no+1==len(History)):
            self.no+=1
            self.checkResults()
            Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
            root.destroy()

        else:
            self.no+=1
            self.checkResults()
            self.displayQuestion()
            self.displayOption()
            self.setFunc()
            self.counter()

            
    #Escape Button functionality
    def Escape(self):
        
            response=Message.askquestion("EXIT","ARE YOU SURE")
            if response=="yes":
                Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
                root.destroy()

            
        
#FOR PLAYING SCIENCE QUIZ  
class ScienceQUIZ:
    def __init__(self):

        #Question no
        self.no=0

        #Option Selected
        self.opt=IntVar()
        
        #correct answer variable to store answer selected by user
        self.correct_Answer=0

        #To store scores
        self.score=0

        #Index of question no
        self.index=0
        
        #next button to go to next question
        nxtButton= Button(root,bg='black',fg='white',text="NEXT",height=2,width=5,font=('bold',10),command=self.Next)
        nxtButton.pack()
        nxtButton.place(x=1270,y=689,anchor=SW)

        #ESCAPE BUTTON TO EXIT FROM GAME IN BETWEEN
        EscpButton= Button(root,bg='red',fg='white',text="ESCAPE",height=2,width=10,font=('bold',10),command=self.Escape)
        EscpButton.pack()
        EscpButton.place(x=5,y=689,anchor=SW)

        #varibles for clock
        self.hour=StringVar()
        self.minute=StringVar()
        self.sec=StringVar()

        HourEn=Entry(root,width=5,font=('Bold',15),textvariable=self.hour,state=DISABLED)
        HourEn.pack()
        HourEn.place(x=140,y=80)
        MinuteEn=Entry(root,width=5,font=('Bold',15),textvariable=self.minute,state=DISABLED)
        MinuteEn.pack()
        MinuteEn.place(x=210,y=80)
        SecEn=Entry(root,width=5,font=('Bold',15),textvariable=self.sec,state=DISABLED)
        SecEn.pack()
        SecEn.place(x=300,y=80)

        #Fonts
        self.myfont=Font(family="Helvetica",weight="bold",size=20)
        self.myfont2=Font(family="Times New Roman",weight="bold",size=20)
        self.myfont3=Font(family="Times New Roman",weight="bold",size=30)
        self.myfont4=Font(family="Times New Roman",weight="bold",size=15)

        #Label for time
        Timeleft=Label(text="Time Left: ",font=self.myfont2,background='white')
        Timeleft.pack()
        Timeleft.place(x=0,y=80)
        Hourlbl=Label(text="Hrs",font=self.myfont2,background='white')
        Hourlbl.pack()
        Hourlbl.place(x=140,y=25)
        Minlbl=Label(text="Min",font=self.myfont2,background='white')
        Minlbl.pack()
        Minlbl.place(x=230,y=25)
        Seclbl=Label(text="Sec",font=self.myfont2,background='white')
        Seclbl.pack()
        Seclbl.place(x=320,y=25)


        #To display score making score label
        self.var = StringVar()
        self.var.set(str(self.score))
        scorelbl=Label(root,fg="red",text="Score",font=self.myfont3,background='white')
        scorelbl.place(x=1150,y=60)
        score=Label(root,fg="black",textvariable=self.var,font= self.myfont3,background="white")
        score.pack()
        score.place(x=1260,y=60)
    

        #Changing background color from black to white
        root.config(background="white")

    

        

        #function call
        self.displayQuestion()
        self.displayOption()
        self.setFunc()
        self.counter()

        
        

   #To display options,radio buttons to display option     
    def displayOption(self):
        rb1 = Radiobutton(root,variable=self.opt,value=0,text=Science[self.no]["answers"][self.index],bg="blue",height=2,width=30,font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb1.pack()
        rb1.place(x=100,y=300)
        rb2 = Radiobutton(root,variable=self.opt,value=1,text=Science[self.no]["answers"][self.index+1],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb2.pack()
        rb2.place(x=100,y=375)
        rb3 = Radiobutton(root,variable=self.opt,value=2,text=Science[self.no]["answers"][self.index+2],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb3.pack()
        rb3.place(x=100,y=450)
        rb4 = Radiobutton(root,variable=self.opt,value=3,text=Science[self.no]["answers"][self.index+3],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb4.pack()
        rb4.place(x=100,y=525)
        
        
        
        
    #To display question     
    def displayQuestion(self):
            
            ques_lbl=Label(root,background="white",fg="black",text=Science[self.no]["question"],height=5,width=75,font=self.myfont )
            ques_lbl.pack()
            ques_lbl.place(x = 0,y=150,anchor=NW)

    

    #to check whether option selected is wrong or right        
    def GetCorrectAnswerValue(self):
            self.correct_Answer= self.opt.get()

    
    #To calculate results and updating value of score
    def checkResults(self):
        
        if(Science[self.no-1]["correct_answer"]==self.correct_Answer):
            self.score+=1
        else:
            self.score+=0
            
        self.var.set(str(self.score))

        
    #Intialising the value of timer after pressing next button
    def setFunc(self):
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("30")

    #To decrese the counter after every 1 sec
    def counter(self):
        t=30
        while t>-1:
            (a,b)= divmod(t,60)
            self.hour.set("{0:2d}".format(00))
            self.minute.set("{0:2d}".format(00))
            self.sec.set("{0:2d}".format(b))

            try:
                root.update()
                time.sleep(1)
                t=t-1
            except:
                break

            if t==0:
                Message.showinfo("Time out")
                self.Next()
        
    #to display next question and option 
    def Next(self):
        
        if(self.no+1==len(Science)):
            self.no+=1
            self.checkResults()
            Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
            root.destroy()

        else:
            self.no+=1
            self.checkResults()
            self.displayQuestion()
            self.displayOption()
            self.setFunc()
            self.counter()

            
    #Escape Button functionality
    def Escape(self):
        
            response=Message.askquestion("EXIT","ARE YOU SURE")
            if response=="yes":
                Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
                root.destroy()

            

#FOR PLAYING COMPUTERS QUIZ  
class ComputersQUIZ:
    def __init__(self):

        #Question no
        self.no=0

        #Option selected
        self.opt=IntVar()

        #correct answer variable to store answer selected by user
        self.correct_Answer=0

        #To store score
        self.score=0

        #Index of question
        self.index=0

        #next button to go to next question
        nxtButton= Button(root,bg='black',fg='white',text="NEXT",height=2,width=5,font=('bold',10),command=self.Next)
        nxtButton.pack()
        nxtButton.place(x=1270,y=689,anchor=SW)


        #ESCAPE BUTTON TO EXIT FROM GAME IN BETWEEN
        EscpButton= Button(root,bg='red',fg='white',text="ESCAPE",height=2,width=10,font=('bold',10),command=self.Escape)
        EscpButton.pack()
        EscpButton.place(x=5,y=689,anchor=SW)

        #varibles for clock
        self.hour=StringVar()
        self.minute=StringVar()
        self.sec=StringVar()

        HourEn=Entry(root,width=5,font=('Bold',15),textvariable=self.hour,state=DISABLED)
        HourEn.pack()
        HourEn.place(x=140,y=80)
        MinuteEn=Entry(root,width=5,font=('Bold',15),textvariable=self.minute,state=DISABLED)
        MinuteEn.pack()
        MinuteEn.place(x=210,y=80)
        SecEn=Entry(root,width=5,font=('Bold',15),textvariable=self.sec,state=DISABLED)
        SecEn.pack()
        SecEn.place(x=300,y=80)


        #Fonts
        self.myfont=Font(family="Helvetica",weight="bold",size=20)
        self.myfont2=Font(family="Times New Roman",weight="bold",size=20)
        self.myfont3=Font(family="Times New Roman",weight="bold",size=30)
        self.myfont4=Font(family="Times New Roman",weight="bold",size=15)

        #Label for time
        Timeleft=Label(text="Time Left: ",font=self.myfont2,background='white')
        Timeleft.pack()
        Timeleft.place(x=0,y=80)
        Hourlbl=Label(text="Hrs",font=self.myfont2,background='white')
        Hourlbl.pack()
        Hourlbl.place(x=140,y=25)
        Minlbl=Label(text="Min",font=self.myfont2,background='white')
        Minlbl.pack()
        Minlbl.place(x=230,y=25)
        Seclbl=Label(text="Sec",font=self.myfont2,background='white')
        Seclbl.pack()
        Seclbl.place(x=320,y=25)


        #To display score making score label
        self.var = StringVar()
        self.var.set(str(self.score))
        scorelbl=Label(root,fg="red",text="Score",font=self.myfont3,background='white')
        scorelbl.place(x=1150,y=60)
        score=Label(root,fg="black",textvariable=self.var,font= self.myfont3,background="white")
        score.pack()
        score.place(x=1260,y=60)
    

        #Changing background color from black to white
        root.config(background="white")

    

        #function call
        self.displayQuestion()
        self.displayOption()
        self.setFunc()
        self.counter()

        
        

    #To display options,radio buttons to display option   
    def displayOption(self):
        rb1 = Radiobutton(root,variable=self.opt,value=0,text=Computers[self.no]["answers"][self.index],bg="blue",height=2,width=30,font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb1.pack()
        rb1.place(x=100,y=300)
        rb2 = Radiobutton(root,variable=self.opt,value=1,text=Computers[self.no]["answers"][self.index+1],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb2.pack()
        rb2.place(x=100,y=375)
        rb3 = Radiobutton(root,variable=self.opt,value=2,text=Computers[self.no]["answers"][self.index+2],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb3.pack()
        rb3.place(x=100,y=450)
        rb4 = Radiobutton(root,variable=self.opt,value=3,text=Computers[self.no]["answers"][self.index+3],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb4.pack()
        rb4.place(x=100,y=525)
        
        
        
        
    #To display question   
    def displayQuestion(self):
            
            ques_lbl=Label(root,background="white",fg="black",text=Computers[self.no]["question"],height=5,width=75,font=self.myfont )
            ques_lbl.pack()
            ques_lbl.place(x =0,y=150,anchor=NW)

    

    #to check whether option selected is wrong or right        
    def GetCorrectAnswerValue(self):
            self.correct_Answer= self.opt.get()

    
    #To calculate results and updating value of score
    def checkResults(self):
        
        if(Computers[self.no-1]["correct_answer"]==self.correct_Answer):
            self.score+=1
        else:
            self.score+=0
            
        self.var.set(str(self.score))

        
    #Intialising the value of timer after pressing next button
    def setFunc(self):
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("30")


    #To decrese the counter after every 1 sec
    def counter(self):
        t=30
        while t>-1:
            (a,b)= divmod(t,60)
            self.hour.set("{0:2d}".format(00))
            self.minute.set("{0:2d}".format(00))
            self.sec.set("{0:2d}".format(b))

            try:
                root.update()
                time.sleep(1)
                t=t-1
            except:
                break

            if t==0:
                Message.showinfo("Time out")
                self.Next()
        
    #to display next question and option 
    def Next(self):
        
        if(self.no+1==len(Computers)):
            self.no+=1
            self.checkResults()
            Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
            root.destroy()

        else:
            self.no+=1
            self.checkResults()
            self.displayQuestion()
            self.displayOption()
            self.setFunc()
            self.counter()
            
    #Escape Button functionality
    def Escape(self):
        
            response=Message.askquestion("EXIT","ARE YOU SURE")
            if response=="yes":
                Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
                root.destroy()


            
#FOR PLAYING ENGLISH QUIZ  
class EnglishQUIZ:
    def __init__(self):

        #Question no
        self.no=0

        #Option Selected
        self.opt=IntVar()
        
        #correct answer variable to store answer selected by user
        self.correct_Answer=0

        #To store scores
        self.score=0

        #Index of question no
        self.index=0

        
        #next button to go to next question
        nxtButton= Button(root,bg='black',fg='white',text="NEXT",height=2,width=5,font=('bold',10),command=self.Next)
        nxtButton.pack()
        nxtButton.place(x=1270,y=689,anchor=SW)


        #ESCAPE BUTTON TO EXIT FROM GAME IN BETWEEN
        EscpButton= Button(root,bg='red',fg='white',text="ESCAPE",height=2,width=10,font=('bold',10),command=self.Escape)
        EscpButton.pack()
        EscpButton.place(x=5,y=689,anchor=SW)
         
        #varibles for clock
        self.hour=StringVar()
        self.minute=StringVar()
        self.sec=StringVar()

        HourEn=Entry(root,width=5,font=('Bold',15),textvariable=self.hour,state=DISABLED)
        HourEn.pack()
        HourEn.place(x=140,y=80)
        MinuteEn=Entry(root,width=5,font=('Bold',15),textvariable=self.minute,state=DISABLED)
        MinuteEn.pack()
        MinuteEn.place(x=210,y=80)
        SecEn=Entry(root,width=5,font=('Bold',15),textvariable=self.sec,state=DISABLED)
        SecEn.pack()
        SecEn.place(x=300,y=80)


        #Fonts
        self.myfont=Font(family="Helvetica",weight="bold",size=20)
        self.myfont2=Font(family="Times New Roman",weight="bold",size=20)
        self.myfont3=Font(family="Times New Roman",weight="bold",size=30)
        self.myfont4=Font(family="Times New Roman",weight="bold",size=15)


        #Label for time 
        Timeleft=Label(text="Time Left: ",font=self.myfont2,background='white')
        Timeleft.pack()
        Timeleft.place(x=0,y=80)
        Hourlbl=Label(text="Hrs",font=self.myfont2,background='white')
        Hourlbl.pack()
        Hourlbl.place(x=140,y=25)
        Minlbl=Label(text="Min",font=self.myfont2,background='white')
        Minlbl.pack()
        Minlbl.place(x=230,y=25)
        Seclbl=Label(text="Sec",font=self.myfont2,background='white')
        Seclbl.pack()
        Seclbl.place(x=320,y=25)


        #To display score making score label
        self.var = StringVar()
        self.var.set(str(self.score))
        scorelbl=Label(root,fg="red",text="Score",font=self.myfont3,background='white')
        scorelbl.place(x=1150,y=60)
        score=Label(root,fg="black",textvariable=self.var,font= self.myfont3,background="white")
        score.pack()
        score.place(x=1260,y=60)
    

        #Changing background color from black to white
        root.config(background="white")

    

        #function call
        self.displayQuestion()
        self.displayOption()
        self.setFunc()
        self.counter()

        
        

    #To display options,radio buttons to display option 
    def displayOption(self):
        rb1 = Radiobutton(root,variable=self.opt,value=0,text=English[self.no]["answers"][self.index],bg="blue",height=2,width=30,font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb1.pack()
        rb1.place(x=100,y=300)
        rb2 = Radiobutton(root,variable=self.opt,value=1,text=English[self.no]["answers"][self.index+1],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb2.pack()
        rb2.place(x=100,y=375)
        rb3 = Radiobutton(root,variable=self.opt,value=2,text=English[self.no]["answers"][self.index+2],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb3.pack()
        rb3.place(x=100,y=450)
        rb4 = Radiobutton(root,variable=self.opt,value=3,text=English[self.no]["answers"][self.index+3],height=2,width=30,bg='blue',font=self.myfont4,command=self.GetCorrectAnswerValue)
        rb4.pack()
        rb4.place(x=100,y=525)
        
        
        
        
    #To display question    
    def displayQuestion(self):
            
            ques_lbl=Label(root,background="white",fg="black",text=English[self.no]["question"],height=5,width=75,font=self.myfont )
            ques_lbl.pack()
            ques_lbl.place(x = 0,y=150,anchor=NW)

    

    #to check whether option selected is wrong or right        
    def GetCorrectAnswerValue(self):
            self.correct_Answer= self.opt.get()

    
    #To calculate results and updating value of score
    def checkResults(self):
        
        if(English[self.no-1]["correct_answer"]==self.correct_Answer):
            self.score+=1
        else:
            self.score+=0
            
        self.var.set(str(self.score))

        
    #Intialising the value of timer after pressing next button
    def setFunc(self):
        self.hour.set("00")
        self.minute.set("00")
        self.sec.set("30")
        
    #To decrese the counter after every 1 sec
    def counter(self):
        t=30
        while t>-1:
            (a,b)= divmod(t,60)
            self.hour.set("{0:2d}".format(00))
            self.minute.set("{0:2d}".format(00))
            self.sec.set("{0:2d}".format(b))

            #try block since update raise exception if we destroy gui window
            try:
                root.update()
                time.sleep(1)
                t=t-1
            except:
                break

            if t==0:
                Message.showinfo("Time out")
                self.Next()
        
   #to display next question and option 
    def Next(self):
        
        if(self.no+1==len(English)):
            self.no+=1
            self.checkResults()
            Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
            root.destroy()

        else:
            self.no+=1
            self.checkResults()
            self.displayQuestion()
            self.displayOption()
            self.setFunc()
            self.counter()
            
   #Escape Button functionality
    def Escape(self):
        
            response=Message.askquestion("EXIT","ARE YOU SURE")
            if response=="yes":
                Message.showinfo("SCORE","FINAL SCORE"+" "+str(self.score))
                root.destroy()

        
   
            
#Loading Data into JSON file    
with open('GeneralKnowledge.txt','r') as json_file:
            data1 = json.load(json_file)
with open('Maths.txt','r') as json_file:
            data2 = json.load(json_file)
with open('Science.txt','r') as json_file:
            data3 = json.load(json_file)
with open('English.txt','r') as json_file:
            data4 = json.load(json_file)
with open('History.txt','r') as json_file:
            data5 = json.load(json_file)
with open('Computers.txt','r') as json_file:
            data6 = json.load(json_file)

GK = data1["questions"]
Maths = data2["questions"]
Science = data3["questions"]
English = data4["questions"]
History = data5["questions"]
Computers = data6["questions"]


#To make Window
root = Tk()

# To set title of window       
root.title("QUIZZ")

# To set size of window
root.geometry("1366x768")
root.minsize(1366,768)

# To set background color of window
root.configure(background="black")


#Images for labels and Buttons
img =ImageTk.PhotoImage(Image.open("quiz2.png"))
welcomeimg=ImageTk.PhotoImage(Image.open("welcome.png"))
START =ImageTk.PhotoImage(Image.open("START.jpg"))
EXIT =PhotoImage(file="EXITT.png")
Choose =ImageTk.PhotoImage(Image.open("Choose.jpg"))
Sst =ImageTk.PhotoImage(Image.open("Sst.png"))
Gk =PhotoImage(file="Gk.png")
Sci =PhotoImage(file="Science.png")
Math =PhotoImage(file="Maths.png")
Computer =PhotoImage(file="comp.png")
Eng =PhotoImage(file="English.png")



#welcome label
lbl = Label(root,image=welcomeimg,borderwidth=0,fg="black",bg="white",font=( 'Arial' ,35 ))

lblImg=Label(root,image=img,background='black')


#start and quit button
bt1=Button(root,image=START,background='black',bg="black",borderwidth=0,command=StartBtnFunc)
bt2= Button(root,image=EXIT,background='black',bg="black",borderwidth=0,command=root.destroy)


#packing labels and button
lbl.pack(side=TOP)
lblImg.pack(side=LEFT,fill=BOTH)
bt1.pack()
bt2.pack()
bt2.place(x=570,y=450,anchor=NW)
bt1.place(x=550,y=250,anchor=NW)

Bt1=Button(image=Sst,background='black',bg="black",borderwidth=0,command=optionCommandHistory)
Bt2=Button(image=Gk,background='black',bg="black",borderwidth=0,command=optionCommandGK)
Bt3=Button(image=Computer,background='black',bg="black",borderwidth=0,command=optionCommandComputers)
Bt4=Button(image=Sci,background='black',bg="black",borderwidth=0,command=optionCommandScience)
Bt5=Button(image=Eng,background='black',bg="black",borderwidth=0,command=optionCommandEnglish)
Bt6=Button(image=Math,background='black',bg="black",borderwidth=0,command=optionCommandMaths)
label = Label(root,image=Choose,background='black',bg="black",borderwidth=0)



root.mainloop()
