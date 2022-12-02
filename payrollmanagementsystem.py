from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Payroll Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)
Bottoms = Frame(root,width=600, relief = SUNKEN)
Bottoms.pack(side=BOTTOM)
f1=Frame(root,width=800,height=200,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=300,bd=8,relief="raise")
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',30,'bold'),text="Payroll Management System",fg="Black",bd=8,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=8,anchor='w')
lblInfo.grid(row=1,column=0)

def iExit():
    root.destroy()
          

def Reset():
     Name.set("")
     Address.set("")
     HoursWorked.set("")
     wageshour.set("")
     Payable.set("")
     Employee.set("")
     ID.set("")
     GrossPayable.set("")
     txtPaySlip.delete("1.0",END)


def EnterInfo():
     txtPaySlip.insert(END, "\t\tPay Slip\n\n")
     txtPaySlip.insert(END, "Name\t\t" + Name.get() + "\n\n")
     txtPaySlip.insert(END, "Address\t\t" + Address.get() + "\n\n")
     txtPaySlip.insert(END, "NI Number\t\t" + ID.get() + "\n\n")
     txtPaySlip.insert(END, "Hours Worked\t\t" + HoursWorked.get() + "\n\n")
     txtPaySlip.insert(END, "Wages Per Hour\t\t" + wageshour.get() + "\n\n")
     txtPaySlip.insert(END, "Payable\t\t" + Payable.get() + "\n\n")
     
def WeeklyWages():
     HoursWorkedPerWeek = float(HoursWorked.get())
     WagesPerHour = float(wageshour.get())

     paydue =   WagesPerHour * HoursWorkedPerWeek
     PaymentDue = "RS." , str('%.2f'%(paydue))
     Payable.set(PaymentDue)    

Name = StringVar()
Address = StringVar()
Employee = StringVar()
ID = StringVar()
wageshour = StringVar()
HoursWorked = StringVar()
Payable = StringVar()
GrossPayable = StringVar()
TimeOfOrder =  StringVar()
DateOfOrder = StringVar()

lblName = Label(f1, text="Name", font=('arial',14,'bold'), bd =10).grid(row=0,column=0)
lblAddress = Label(f1, text="Address", font=('arial',14,'bold'), bd =10).grid(row=0,column=2)
lblEmployee = Label(f1, text="Employee", font=('arial',14,'bold'), bd =10).grid(row=1,column=0)
lblNINumber = Label(f1, text="ID", font=('arial',14,'bold'), bd=10).grid(row=1,column=2)
lblHoursworked = Label(f1, text="Hours Worked", font=('arial',14,'bold'), bd=10).grid(row=2,column=0)
lblhourlyRate = Label(f1, text="Hourly Rate", font=('arial',14,'bold'), bd=10).grid(row=2,column=2)
lblGrossPay = Label(f1, text="Salary", font=('arial',14,'bold'), bd=10).grid(row=4,column=0)

etxtName = Entry(f1,textvariable=Name, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtName.grid(row=0,column=1)
etxtAddress = Entry(f1,textvariable=Address, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtAddress.grid(row=0,column=3)
etxtEmployee = Entry(f1,textvariable=Employee, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtEmployee.grid(row=1,column=1)
etxtHoursWorked = Entry(f1,textvariable=HoursWorked, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtHoursWorked.grid(row=2,column=1)
etxtWagesPerHour = Entry(f1,textvariable=wageshour, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtWagesPerHour.grid(row=2,column=3)
etxtninoW = Entry(f1,textvariable=ID, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtninoW.grid(row=1,column=3)
etxtGrossPay = Entry(f1,textvariable=Payable, font=('arial',14,'bold'),bd=10, width=22,justify='left')
etxtGrossPay.grid(row=4,column=1)


lblPaySlip=Label(f2,font=('arial',20,'bold'),text = "Payslip").grid(row=0,column=0)
txtPaySlip=Text(f2, height = 22, width = 34, bd=14,font=('arial',12,'bold'))
txtPaySlip.grid(row=0,column=0)

btnSalary = Button(f1,text='Calculate',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1, command = WeeklyWages).grid(row=5,column=0)

btnReset = Button(f1,text='Reset',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1,command=Reset).grid(row=5,column=1)

btnPaySlip = Button(f1,text='Pay Slip',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1,command = EnterInfo).grid(row=5,column=2)

btnExit = Button(f1,text='Exit System',padx=8,pady=8,bd=8,fg="black",font=('arial',14,'bold'),width=10, height=1, command = iExit).grid(row=5,column=3)

root.mainloop()