from tkinter import *
root=Tk()
root.title("First GUI Application")
root.geometry("1980x720")
e=Entry(root,width=50,bg='skyblue',fg='black')
e.pack()

def myclick():
    label=Label(root,text="hello "+e.get())
    label.pack()
button=Button(root,text="say hello rudal",command=myclick)
button.pack()
root.mainloop()