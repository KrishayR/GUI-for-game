from tkinter import *
import tkinter.messagebox
import pygame
root = Tk()
root.title('LIFE')
root.configure(bg='#0d3d00')


label = Label(text = "  L   I   F   E  ",font=('Helvetica',85,'bold'),fg='#13690b')
label.configure(bg='#fff2a0')

label.pack(fill=X)


def newworld():
    hi = tkinter.messagebox.askquestion('LIFE','This is a private server. Only you will be able to see this. Are you sure you want to make a new world?')
    if hi == 'yes':
        e = Entry(root)
        e.pack()
    elif hi == 'no':
        e.pack_forget()
        
    def newButton():
        Button(text=e.get(),font=('Helvetica',20,'bold'),width = 25,height = 2,bg='#ffb57c',fg='black').pack()
        ok1.pack_forget()
        e.pack_forget()
    
    def ok():
        okdokey = tkinter.messagebox.showinfo('LIFE','You just created a server!')
    ok1 = Button(text="Done",bg='#192569',command=newButton,padx=50,pady=15,fg='white')
    ok1.pack(side=BOTTOM)
def newpublic():
    kk = tkinter.messagebox.askquestion('LIFE','Everyone will see this server. Are you sure you want to create one?')
    if kk == 'yes':
        p = Entry(root)
        p.pack()
    elif kk == 'no':
        p.pack_forget()
        
    def newBut():
        Button(text=p.get(),font=('Helvetica',20,'bold'),width = 25,height = 2,bg='#ffb57c',fg='black').pack()
        o.pack_forget()
        p.pack_forget()
    
    def k():
        omg = tkinter.messagebox.showinfo('LIFE','You just created a public server!')
    o = Button(text="Done",bg="#34428a",command=newBut,padx=50,pady=15,fg='#ffffff')
    o.pack(side=BOTTOM)
    
def window():
    root2 = Toplevel(root)
    stl = Label(root2,text='Stats & Settings',font=('Helvetica',25,'bold'),bg="black",fg='white')
    stl.pack()
    root2.configure(bg='black')
def nnnwindow():
    root3 = Toplevel(root)
    strfb = Label(root3,text='~ CHAT ~',font=('Helvetica',25,'bold'),bg="black",fg='white')
    strfb.pack()
    root3.configure(bg='black')
def kkkwindow():
    root4 = Toplevel(root)
    strb = Label(root4,text='Friends',font=('Helvetica',25,'bold'),bg="black",fg='white')
    strb.pack()
    root4.configure(bg='black')
tab = Button(root,text='Stats & Settings',font=('Helvetica',15,'bold'),width = 15,height = 3,command=window)
tab.pack(anchor='sw')
tab2 = Button(root,text='Chat',font=('Helvetica',15,'bold'),width = 15,height = 3,command=nnnwindow)
tab2.pack(anchor='sw')
tab3 = Button(root,text='Friends',font=('Helvetica',15,'bold'),width = 15,height = 3,command=kkkwindow)
tab3.pack(anchor='sw')
public = Button(text = "Create Public Server",font=('Helvetica',20,'bold'),width = 25,height = 2,command=newpublic)
public.configure(bg='#7d7456')
public.place(relx=0.5, rely=0.5, anchor='center')
public.pack()
neworld = Button(text = "Create New World",font=('Helvetica',20,'bold'),width = 25,height = 2,command=newworld)
neworld.configure(bg='#7d7456')
neworld.place(relx=0.5, rely=0.5, anchor='center')
neworld.pack()


root.mainloop()
