


from random import*
from tkinter import*


class PassGen:
       
    def __init__(self,root):
        self.root=root
        self.SetGui()
        
    def SetGui(self):
         
        l1=Label(self.root,text="Password Generator",bg="green")
        l1.grid(row=0, columnspan=2)

        l2=Label(self.root, text="Length Of Password")
        l2.grid(row=1, column=0)
        self.e1=Entry(self.root)
        self.e1.grid(row=1, column=1)

        self.level=IntVar()
        self.level.set(2)#default level to easy 

        l3=Label(self.root, text="Level of password")
        l3.grid(row=2, column=0)
        r1=Radiobutton (self.root,text="Easy", variable=self.level,value=2)
        r1.grid(row=2, column=1)
        r2=Radiobutton (self.root,text="Medium", variable=self.level,value=3)
        r2.grid(row=2, column=2)
        r3=Radiobutton (self.root,text="Hard", variable=self.level,value=4)
        r3.grid(row=2, column=3)

        b1=Button (self.root,text="Generate",command=self.gen)
        b1.grid(row=3, column=1)

        self.e2=Entry(self.root, width=25)
        self.e2.grid(row=4, column=1)
    
            
           
    def gen(self):
        try:#check user's input 
            length = int(self.e1.get())
        except ValueError:
            self.e2.delete(0, 'end')
            self.e2.insert(0, "Invalid input")
            return    
        if (self.e1.get()==""):
            self.e2.delete("0","end")
            self.e2.insert("0","Invalid input")
        elif (int(self.e1.get())<8):
            self.e2.delete("0","end")
            self.e2.insert("0","Invalid length")
        else:
            a=int(self.e1.get()) 
            lev=self.level.get()
            

             #list of all characters require for password making            
            Upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

            Lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

            Symbol =["@","$","#","*","&","_"]

            Number=["0","1","2","3","4","5","6","7","8","9"]
            password=choice(Upper)+choice(Lower)+choice(Symbol)+choice(Number) 

 
            for i in range (a-4):
                All=[Lower, Upper,Number,Symbol]
                rand=All[randrange(0,lev)]#here randrange[] function return random number from given range.
      
                password+=choice(rand)#appending other character to password 
                
        
            
            strong_pass=list(password)

    
            shuffle(strong_pass)#shuffle's' the elements of list randomly 
            passw="".join(strong_pass)#converting list to string
            self.e2.delete("0","end")
            self.e2.insert("0",passw)
            
        
    
      



root=Tk()

PassGen(root)
root.mainloop()
