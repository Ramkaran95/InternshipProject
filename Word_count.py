


from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("700x1400")
root.title("Word count App")

#logic

def find():
    text1=text.get("1.0","end-1c")
    entry1=entry.get()
    
    #error handling for empty input 
    if (text1==""):
        
        messagebox.showinfo("Error_of_field_one","Please enter any sentence or paragraph.")
        label3.config(text="")
        
    elif (entry1==""):
        messagebox.showinfo("Error_of_field_two","Please enter any word to find count.")
        label3.config(text="")
    else:
        
        lower_text=text1.lower()
        lower_entry=entry1.lower()
        split_text=lower_text.split()
        count=split_text.count(lower_entry)
    
        label3.config(text="The occurrence of word "+" '"+entry1+"' "+" is "+str(count)+" .")
        print("The occurrence of word "+" '"+entry1+"' "+" is "+str(count)+" .")
    
def clear_hint(event):
    current_text=text.get("1.0","end-1c")
    if( current_text==hint_text):
        text.delete("1.0","end")
    
    



#design

label1=Label(root,text="Enter your text ")
label1.pack(pady=10)

text=Text(root, height=4,fg="black",bg="white",bd=2)
hint_text="Click here to enter your sentence...."
text.insert("1.0",hint_text)
text.pack()
text.bind("<FocusIn>",clear_hint)

lable2=Label(root,text="Enter word to find occurrence")
lable2.pack(pady=10)

entry=Entry(root)
entry.pack(pady=10)
button1=Button(root,text="Submit",command=find)
button1.pack(pady=15)
label3=Label(root,text="")
label3.pack(pady=10)



root.mainloop()
