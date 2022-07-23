'''
Name: Aneesha Kavathekar
Roll No-1020159
Practical 5
GUI
'''

from tkinter import*
from tkinter import messagebox
record=Tk()
record.geometry("450x400")
record.title('Attendance Record')
frame=Frame(record)

label1=Label(record, text='Name').grid(row=1, column=3)
label2=Label(record, text='Roll No.').grid(row=3, column=3)
label3=Label(record,text='Semester').grid(row=5, column=3)
label4=Label(record, text='Date').grid(row=7, column=3)
e1=Entry(record)
e2=Entry(record)
e3=Entry(record)
e4=Entry(record)
e1.grid(row=1, column=5)
e2.grid(row=3, column=5)
e3.grid(row=5, column=5)
e4.grid(row=7, column=5)
def clicked1():
  messagebox.showinfo("Attendance Recorded")
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)
def clicked2():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)
submit=Button(record, text='Submit',command=clicked1)
cancel=Button(record, text='Cancel',command=clicked2)
submit.grid(row=9,column=3)
cancel.grid(row=9,column=4)

record.mainloop()
