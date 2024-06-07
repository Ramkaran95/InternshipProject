

from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x1400")

#logic

class Expense():
    def __init__(self,amt, dte,dis,cat):
        self.amt=amt
        self.dte=dte
        self.dis=dis
        self.cat=cat
    
class Expense_Tracker():
    Expense_List=[]
    sum=0 
    #Add() will get the user value and validate it and store it in the list.
    def Add():
        if e1.get()=="" or e2.get()=="" or e3.get()=="":
            messagebox.showinfo("info", "please input a value")
        else:
            
            
            amount =int( e1.get())
            date=e2.get()
            disc=e3.get()
            cate=var.get()
            e=Expense(amount,date,disc,cate)
            Expense_Tracker.Expense_List.append(e)
            s="Expense of  ₹"+str(amount)+" for "+disc+"\n on date "+date+" is added "+cate
            messagebox.showinfo("info",s)
            
            e1.delete(0,"end")#after adding one value this will delete the past inserted value from the entry widget 
            e2.delete(0,"end")
            e3.delete(0,"end")
    #view() will access the list and display the values in the frame. If there is any widget already existing in the frame then it will delete that all widget and display the value from list in the label widget one by one in frame .And also display the total sum of list.
    def view():
       sum=0
       for widget in p1.winfo_children():           
        widget.destroy()
       Label(p1,text="Sr No.    Price.   Description.     Date.   Categories", bg="pink",anchor="w").pack(anchor="w",fill=X,padx=5,pady=3)
       for i in range(len(Expense_Tracker.Expense_List)):
           a=Expense_Tracker.Expense_List[i]
           amt=str(a.amt)
           sum=sum+a.amt
           d=a.dte
           di=a.dis
           cate=a.cat
           Label(p1, height=2,text=str(i+1)+".   ₹" +amt+"   "+di+"  "+d+"  "+cate,anchor="w",bg="lightgrey").pack(anchor="w",fill=X,padx=5,pady=3)
       
       if sum==0:
            
            Label(p1,text="Empty record",bg="red").pack()
       else:
            Label(p1, text="The total expenditure is  ₹" + str(sum),bg="lightgreen").pack()
    
    # Remove() will delete the expenditure record from list on the basis of it serial number.After deleting the record ,it will again display available record from the list.
    def Remove():
        sum = 0
        if e4.get() == "":
            messagebox.showinfo("info", "please input a value")
        else:
            num = int(e4.get())
            if num == 0:
                messagebox.showinfo("info", "record not found")
            else:
                num = num - 1
                if num < len(Expense_Tracker.Expense_List):
                    Expense_Tracker.Expense_List.pop(num)
                    messagebox.showinfo("info", "record deleted")
                    for widget in p1.winfo_children():
                        widget.destroy()
                   
                    Label(p1,text="Sr No.  Price.   Description.  Date.  Categories", bg="pink",anchor="w").pack(anchor="w",fill=X,padx=5,pady=3)
                    for i in range(len(Expense_Tracker.Expense_List)):
                        a = Expense_Tracker.Expense_List[i]
                        amt = str(a.amt)
                        sum = sum + a.amt
                        d = a.dte
                        di = a.dis
                        cate=a.cat
                        
                        Label(p1, height=2,text=str(i+1)+".   ₹" +amt+"   "+di+"  "+d+"  "+cate,anchor="w",bg="lightgrey").pack(anchor="w",fill=X,padx=5,pady=3)
                        
                                
                    if sum==0:
                        Label(p1,text="Empty record",bg="red").pack()
                    else:
                        
                        Label(p1, text="The total expenditure is  ₹" + str(sum),bg="lightgreen").pack()
                    e4.delete(0,"end")
                else:
                    messagebox.showinfo("info", "record not found")
                    e4.delete(0,"end")
     #Analysis() will sort the list on the category of expenditures and store it ,then represent the all sorted values in pie chart and in percentage form.        
    def Analysis():
             tot=0
             per=0
             tran=0
             ent=0
             food=0
             fam=0
             option=["Personal","Entertainment","Family","Food","Transport"]
             for i in range(len(Expense_Tracker.Expense_List)):
                 price=Expense_Tracker.Expense_List[i]
                 tot=tot+price.amt
                 if price.cat==option[0]:
                     per=per+price.amt
                 elif price.cat==option[1]:
                     ent=ent+price.amt
                 elif price.cat==option[2]:
                     fam=fam+price.amt
                 elif price.cat==option[3]:
                     food=food+price.amt
                 else :
                     tran=tran+price.amt
             data=[per,ent,fam,food,tran]
             color=["blue","green","yellow","orange","red"]
             start_angle=0
             x,y=150,150
             radius=100
             top=Toplevel(root)
             canvas = Canvas(top, width=300, height=300)
             
             canvas.pack()
             perc=[]
             for i in range(len(data)):
                 
                 if data[i]==0:
                     angle=0
                     perc.append(0)
                     
                 else:
                     
                     angle=360*data[i]/tot
                     p=float(100*data[i]/tot)
                     
                     perc.append(round(p,2))
                  
                 canvas.create_arc(x - radius, y - radius, x + radius, y + radius,start=start_angle,extent=angle, fill=color[i])
                 
                 start_angle+=angle           
             Label(top,text=option[0]+" "+str(perc[0])+" %",bg=color[0]).pack()
             Label(top,text=option[1]+" "+str(perc[1])+" %",bg=color[1]).pack()
             Label(top,text=option[2]+" "+str(perc[2])+" %",bg=color[2]).pack()
             Label(top,text=option[3]+" "+str(perc[3])+" %",bg=color[3]).pack()
             Label(top,text=option[4]+" "+str(perc[4])+" %",bg=color[4]).pack() 
             top.mainloop()
                               
            
#design of application 
l1=Label(root,text="Expenditure Tracker",bg="grey")
l1.place(x=250,y=50)
l2=Label(root,text="Enter Amount ",bg="grey")
l2.place(x=30,y=150)
l3=Label(root,text="Enter Date ",bg="grey")
l3.place(x=30,y=250)
l4=Label(root,text="Enter Description",bg="grey")
l4.place(x=30,y=350)
l5=Label(root,text="Choose Category",bg="grey")
l5.place(x=30,y=430)
e1=Entry(root)
e1.place(x=350,y=150)

e2=Entry(root)
e2.place(x=350,y=250)

e3=Entry(root)
e3.place(x=350,y=350)
var=StringVar()
option=["Personal","Entertainment","Family","Food","Transport"]
var.set(option[0])
opt=OptionMenu(root,var,*option)
opt.place(x=350,y=420)
b1=Button(root,text="Add",command=Expense_Tracker.Add)
b1.place(x=150,y=550)
b2=Button(root,text="View", command=Expense_Tracker.view)
b2.place(x=300,y=550)
b3=Button(root,text="Analysis",command=Expense_Tracker.Analysis)
b3.place(x=450,y=550)

l6=Label(root, height =1,text="Enter record no. to delete ",bg="grey")
l6.place(x=30,y=650)
e4=Entry(root, width=3)
e4.place(x=400,y=650)

b4=Button(root,text="Remove",command=Expense_Tracker.Remove)
b4.place(x=490,y=650)



canvas = Canvas(root, width=650, relief ="groove",bd=4,height =500,bg="blue")
p1= Frame(canvas,bg="lightblue")
scrollbar = Scrollbar(root, orient="horizontal", command=canvas.yview,width=50)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.place(x=580,y=1270)
canvas.place(x=15,y=730)
canvas.create_window((5, 5), window=p1, anchor='nw')

def on_frame(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

p1.bind("<Configure>", on_frame)

root.mainloop()
