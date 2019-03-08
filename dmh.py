from tkinter import *


dm=Tk()
dm_text=Label(dm,text="Bonjour tout le monde ce code est en cours de developement ")
dm_leboutton=Button(dm,text="Salut a tous ",command=hello)
dm_saisit=Entry(dm,text="Lets go ",show="*")
dm_cocher=Checkbutton(dm,text="Hé yo les amigos ")
dm_text.pack()
dm_leboutton.pack()
dm_saisit.pack()
dm_cocher.pack()
dm.minsize(540,400)
dm.maxsize(1230,500)
dm.mainloop()
