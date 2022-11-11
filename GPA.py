from tkinter import *

root = Tk()
root.title('GPA Calculator แบบง่ายๆ')
grad = StringVar()
clas = StringVar()
classes = []
grades = []
add_btn = False
def add():
    global add_btn
    global add_btn_real
    grade = grad.get()
    classs = clas.get()
    grades.append(grade)
    classes.append(classs)
    grad.set("")
    clas.set("")
    for x in range(len(classes)):
        textt = f"วิชา: {classes[x]}    เกรด: {grades[x]}"
        Label(root,text=textt).grid(row=1+x)
    if add_btn is False:
        add_btn_real = Button(root,text="คำนวณ GPA",command=calc,bg="#cce6ff")
        add_btn_real.grid(row=x+2)
        add_btn = True
    else:
        old_b = add_btn_real
        add_btn_real = Button(root,text="คำนวณ GPA",command=calc,bg="#cce6ff")
        add_btn_real.grid(row=x+2)
        old_b.pack()
def calc():
    sum = 0
    for x in grades:
        sum=sum+float(x)
    Label(root,text="GPA: "+str(sum/len(grades))).grid(row=2,column=1)

Entry(root,textvariable=clas).grid(row=0,column=0)
Entry(root,textvariable=grad).grid(row=0,column=1)
Button(root,text="เพิ่มวิชา",command=add,bg="#cce6ff").grid(row=0,column=2)


root.mainloop()