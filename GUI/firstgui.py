from tkinter import *
root =Tk()
label1=Label(root,text="how are you mr. Rudal murdar").grid(row=0,column=0)

label2=Label(root,text="I am ffdsa").grid(row=1,column=1)
def myclick():
    mylabel=Label(root,text="Button is clicked")
    mylabel.grid()
button1=Button(root,text='Click me',bg='purple',fg='white', padx=10,pady=10,command=myclick)
button1.grid()



root.mainloop()
