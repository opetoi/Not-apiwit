from tkinter import *

root = Tk()
grad = StringVar()
clas = StringVar()
classes = []
grades = []
def add():
    grade = grad.get()
    classs = clas.get()
    grades.append(grade)
    classes.append(classs)
    grad.set("")
    clas.set("")
    for x in range(len(classes)):
        textt = f"classes: {classes[x]}    score: {grades[x]}"
        Label(root,text=textt).grid(row=1+x)
    Button(root,text="Calculate GPA",command=calc).grid(row=x+2)
def calc():
    for x in grades:
        sum=int(x)
    Label(root,text="GPA: "+str(sum/len(grades))).grid(row=2,column=1)

Entry(root,textvariable=clas).grid(row=0,column=0)
Entry(root,textvariable=grad).grid(row=0,column=1)
Button(root,text="add class",command=add).grid(row=0,column=2)


root.mainloop()