
from tkinter import*
root=Tk()

root.title("Quiz Game")
root.geometry("700x1400")

#------Game logic 
class Quizz:
    
    score =0
    def checkAns():
        var=opt1.get()
        var1=opt2.get()
        var2=opt3.get()
        var3=opt4.get()
        
       #q1
        if (int(var)==1):
           
            Quizz.score=Quizz.score+1
            a1.config(text="correct",fg="green")
        elif (int(var)==0):
            a1.config(text="Answer is not given",fg="brown")
            
        else:
            a1.config(text="Incorrect,The answer is Entry ",fg="red")
         
        #q2   
        if (int(var1)==3):
           
            Quizz.score=Quizz.score+1
            qa1.config(text="correct",fg="green")
        elif (int(var1)==0):
            qa1.config(text="Answer is not given",fg="brown")
            
        else:
            qa1.config(text="Incorrect,The answer is except",fg="red")
        
        #q3
        if (int(var2)==4):
           
            Quizz.score=Quizz.score+1
            qa2.config(text="correct",fg="green")
        elif (int(var2)==0):
            qa2.config(text="Answer is not given",fg="brown")
            
        else:
            qa2.config(text="Incorrect,The answer is Close()",fg="red")
            
       #q4
        if (int(var3)==2):
           Quizz.score=Quizz.score+1
           qa3.config(text="correct",fg="green")
       
        elif (int(var3)==0):
           qa3.config(text="Answer is not given",fg="brown")
            
        else:
           qa3.config(text="Incorrect,The answer is Ctrl+C",fg="red")
                         
        b1.config(state="disabled")
        ans.config(text="Score is "+str(Quizz.score))
            
    def reset():
        Quizz.score=0
        opt1.set(0)
        opt2.set(0)
        opt3.set(0)
        opt4.set(0)
        a1.config(text="")
        qa1.config(text="")
        qa2.config(text="")
        qa3.config(text="")
        ans.config(text="")
        b1.config(state="normal") 


#----------Game UI
l1=Label(root,text="Python Quiz Game",bd=15,bg="lightblue",fg="violet")
l1.place(x=220,y=20)


#question1
q1=Label(root,text="1. Which widget is used to display set of line of text?",bd=15,fg="grey")
q1.place(x=10,y=100)
#question 1 options
opt1=IntVar()
r1=Radiobutton(root, text="Entry",fg="purple",variable =opt1,value=1)
r1.place(x=60,y=180)
r2=Radiobutton(root, text="Text",fg="purple",variable =opt1,value=2)
r2.place(x=380,y=180)
r3=Radiobutton(root, text="List",fg="purple",variable =opt1,value=3)
r3.place(x=60,y=260)
r4=Radiobutton(root, text="TextArea",fg="purple",variable =opt1,value=4)
r4.place(x=380,y=260)
a1=Label(root,text="")
a1.place(x=80,y=310)


#question2
q2=Label(root,text="2. Python exceptions are caught by the ____ keyword",bd=15,fg="grey")
q2.place(x=10,y=350)
#options
opt2=IntVar()
qr1=Radiobutton(root, text="try",fg="purple",variable =opt2,value=1)
qr1.place(x=60,y=430)
qr2=Radiobutton(root, text="catch",fg="purple",variable =opt2,value=2)
qr2.place(x=380,y=430)
qr3=Radiobutton(root, text="except",fg="purple",variable =opt2,value=3)
qr3.place(x=60,y=500)
qr4=Radiobutton(root, text="finally",fg="purple",variable =opt2,value=4)
qr4.place(x=380,y=500)
qa1=Label(root,text="")
qa1.place(x=80,y=550)


#question3
q3=Label(root,text="3. ____ function is used to close file in python.",bd=15,fg="grey")
q3.place(x=10,y=590)
#options
opt3=IntVar()
q3r1=Radiobutton(root, text="finish()",fg="purple",variable =opt3,value=1)
q3r1.place(x=60,y=670)
q3r2=Radiobutton(root, text="end()",fg="purple",variable =opt3,value=2)
q3r2.place(x=380,y=670)
q3r3=Radiobutton(root, text="stop()",fg="purple",variable =opt3,value=3)
q3r3.place(x=60,y=750)
q3r4=Radiobutton(root, text="close()",fg="purple",variable =opt3,value=4)
q3r4.place(x=380,y=750)
qa2=Label(root,text="")
qa2.place(x=80,y=800)


#question4
q4=Label(root,text="4. KeyboardInterrupt is made using ____ in python",bd=15,fg="grey")
q4.place(x=10,y=840)
#options
opt4=IntVar()
q4r1=Radiobutton(root, text="Ctrl+Z",fg="purple",variable =opt4,value=1)    
q4r1.place(x=60,y=920)
q4r2=Radiobutton(root, text="Ctrl+C",fg="purple",variable =opt4,value=2)
q4r2.place(x=380,y=920)
q4r3=Radiobutton(root, text="Ctrl+X",fg="purple",variable =opt4,value=3)
q4r3.place(x=60,y=1000)
q4r4=Radiobutton(root, text="Ctrl+V",fg="purple",variable =opt4,value=4)
q4r4.place(x=380,y=1000)
qa3=Label(root,text="")
qa3.place(x=80,y=1050)


#submit
b1=Button(root,text="Submit",bg="green",fg="white", command=Quizz.checkAns)
b1.place(x=170,y=1150)
#reset
b2=Button(root,text="Reset",bg="green",fg="white",command=Quizz.reset)
b2.place(x=370,y=1150)
#score
ans=Label(root,text="")
ans.place(x=275,y=1250)


root.mainloop()