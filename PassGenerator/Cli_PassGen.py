
from random import *


#list of all characters require for password making
Upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

Lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

Symbol =["@","$","#","*","&","_"]

Number=["0","1","2","3","4","5","6","7","8","9"]


try:#check user's input 
    a=int(input("Enter length of password: "))
    
   
    if (a>=4):#length of password should be greater than 4
        b=int(input("Enter Numbers of password: "))
        lev=int(input("Enter level of strong password(1-4): "))
        print("Password generated successfully: ")
        for i in range (b):#outer loop for creating multiple passwords 
            password=choice(Upper)+choice(Lower)+choice(Symbol)+choice(Number)#it inscures that password must have one number ,symbol, upper ,lower  case character. here choice() function return random element from list.

 
            for i in range (a-4):# inner loop for selecting other remaining password characters from list of all characters.
                All=[Lower, Upper,Number,Symbol]#list of all characters 
                rand=All[randrange(0,lev)]#here randrange[] function return random number from given range.
  
                password+=choice(rand)#appending other character to password 

    
            strong_pass=list(password)

            
            shuffle(strong_pass)#shuffle's' the elements of list randomly 
            p="".join(strong_pass)#converting list to string
            print(p)
    else:
       print("Password must have 4 or more characters")
except:
    print ("Invalid input")




    
