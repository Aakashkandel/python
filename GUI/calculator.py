from tkinter import *
root=Tk()
root.title("Calculator from daraz")
e=Entry(root,width=50,bg='skyblue',fg='black', borderwidth=5)
e.grid(row=0,column=0,padx=20,pady=10,columnspan=4)

def button_click(n):
     current= e.get()
     e.delete(0,END)
     e.insert(0,str(current)+str(n))
     
def clear():
    e.delete(0,END) 
    
         
     
def add_click():
    global f_num
    f_n=e.get()
    f_num = int(f_n)
    e.delete(0,END)
    global math
    math="addition"
    
def sub_click():
    f_num=e.get()
    e.delete(0,END)
    math="sub"
    
def mul_click():
    f_num=e.get()
    e.delete(0,END)
    math="mul"

def divide_click():
    f_num=e.get()
    e.delete(0,END)
    math="div"
    
def equal():
    s_n=e.get()
    e.delete(0,END)
    if(math=='addition'):
        e.insert(0,int(s_n)+f_num)
    elif(math=='sub'):
        e.insert(0,int(s_n-f_num))
    elif(math=='mul'):
        e.insert(0,int(s_n*f_num))
        
    elif(math=='div'):
        e.insert(0,int(s_n/f_num))
    
        
btn1=Button(root,text="7",padx=20,pady=20 ,command=lambda:button_click(7))
btn1.grid(row=1,column=0,padx=20,pady=20)

btn2=Button(root,text="8",padx=20,pady=20 ,command=lambda:button_click(8))
btn2.grid(row=1,column=1,padx=20,pady=20)

btn1=Button(root,text="9",padx=20,pady=20  ,command=lambda:button_click(9))
btn1.grid(row=1,column=2, padx=20,pady=20)

btn1=Button(root,text="Ac",padx=20,pady=20  ,command=clear)
btn1.grid(row=1,column=3, padx=20,pady=20)

btn1=Button(root,text="4",padx=20,pady=20  ,command=lambda:button_click(4))
btn1.grid(row=2,column=0, padx=20,pady=20)

btn1=Button(root,text="5",padx=20,pady=20  ,command=lambda:button_click(5))
btn1.grid(row=2,column=1, padx=20,pady=20)

btn1=Button(root,text="6",padx=20,pady=20  ,command=lambda:button_click(6))
btn1.grid(row=2,column=2, padx=20,pady=20)

btn1=Button(root,text="+",padx=20,pady=20  ,command=add_click)
btn1.grid(row=2,column=3, padx=20,pady=20)

btn1=Button(root,text="1",padx=20,pady=20  ,command=lambda:button_click(1))
btn1.grid(row=3,column=0, padx=20,pady=20)

btn1=Button(root,text="2",padx=20,pady=20  ,command=lambda:button_click(2))
btn1.grid(row=3,column=1, padx=20,pady=20)

btn1=Button(root,text="3",padx=20,pady=20 ,command=lambda:button_click(3))
btn1.grid(row=3,column=2, padx=20,pady=20)

btn1=Button(root,text="*",padx=20,pady=20 ,command=mul_click)
btn1.grid(row=3,column=3, padx=20,pady=20)

btn1=Button(root,text=".",padx=20,pady=20 ,command=lambda:button_click("."))
btn1.grid(row=4,column=0, padx=20,pady=20)

btn1=Button(root,text="0",padx=20,pady=20 ,command=lambda:button_click(0))
btn1.grid(row=4,column=1, padx=20,pady=20)

btn1=Button(root,text="/",padx=20,pady=20 ,command=divide_click)
btn1.grid(row=4,column=2, padx=20,pady=20)

btn1=Button(root,text="=",padx=20,pady=20 ,command=equal)
btn1.grid(row=4,column=3, padx=20,pady=20)



root.mainloop()


