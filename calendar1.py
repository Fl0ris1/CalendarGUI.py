#importing librarys 
from tkinter import *
import calendar

#creating main window
root=Tk()
root.title("Calendar")
root.geometry("300x200")
root.config(background="#baf2d8")
cl=Label(root,text="My Calendar",fg="#6494AA",bg="#baf2d8", font=("arial",20,"bold"))
cl.pack()
year_lbl=Label(root,text="Enter Year: ",bg="#baf2d8", fg="#496F5D",font=("arial",16,"bold"))
year_lbl.pack()
year_input=Entry(root,width=15)
year_input.pack()
show_btn=Button(root,text="Show Calendar", bg="#C1CFDA",fg="#775253",font=("arial",14,"bold"))
show_btn.pack()




root.mainloop()