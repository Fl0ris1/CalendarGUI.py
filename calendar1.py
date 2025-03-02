#importing librarys 
from tkinter import *
import calendar


#creating the calendar window
def show_cal():
    rootcal=Tk()
    rootcal.title("Calendar")
    rootcal.geometry("550x600")
    rootcal.config(background="#C5EDAC")
    year=int(year_input.get())
    cal=calendar.calendar(year)
    calendar_lbl=Label(rootcal,text=cal,font=("consolas",10,"bold"))
    calendar_lbl.grid(row=5,column=1,padx=20)
    rootcal.mainloop()    

#creating main window
root=Tk()
root.title("Calendar")
root.geometry("300x300")
root.config(background="#baf2d8")
cl=Label(root,text="My Calendar",fg="#6494AA",bg="#baf2d8", font=("arial",20,"bold"))
cl.pack(anchor="center",pady=10)
year_lbl=Label(root,text="Enter Year: ",bg="#baf2d8", fg="#496F5D",font=("arial",16,"bold"))
year_lbl.pack(anchor="center",pady=10)
year_input=Entry(root,width=15)
year_input.pack(anchor="center",pady=10)
show_btn=Button(root,text="Show Calendar", bg="#A0EEC0",fg="#775253",font=("arial",14,"bold"),command=show_cal)
show_btn.pack(anchor="center",pady=10)
exit_btn=Button(root,text="Exit",bg="#A0EEC0",fg="#775253",font=("arial",14,"bold"),command=exit)
exit_btn.pack(anchor="center",pady=10)

root.mainloop()