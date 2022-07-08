import datetime
from tkinter import *
import random
a = Tk()
a.geometry('1600x700')
a.title("Restaurent Management System")
topf = Frame(a,bg="white",width=1600,height=50)
topf.pack(side=TOP)
##side= TOP,LEFT,RIGHT,BOTTOM
bottomf = Frame(a,bg="steel blue",width=1600,height=50)
bottomf.pack(side=BOTTOM)

f1 = Frame(a,width=900,height=600)
f1.pack(side=LEFT)

f2 = Frame(a,width=600,height=600)
f2.pack(side=RIGHT)

d = datetime.datetime.now()

lblinto = Label(topf,text="Res Mang System",fg="steel blue",bd=10,font=( 'aria' ,16, 'bold' ))
lblinto.grid(row=0,column=1)

lbltime = Label(topf,text=d,fg="steel blue",bd=10,font=( 'aria' ,16, 'bold' ))
lbltime.grid(row=2,column=1)

orderno = IntVar()
orderno.set("")
Fishmeal = IntVar()
Fishmeal.set("")
Chickenmeal = IntVar()
drinks = IntVar()
total = IntVar()
scharge = IntVar()
tax = IntVar()
overall = IntVar()
Chickenmeal.set("")
MuttonMeal = IntVar()
MuttonMeal.set("")
drinks.set("")
total .set("")
scharge.set("")
tax.set("")
overall.set("")
def tot():
    x = random.randint(1000, 10000)
    orderno.set(x)

    Fish = Fishmeal.get()
    Chick = Chickenmeal.get()
    Mutton = MuttonMeal.get()
    drink = drinks.get()

    cfish = Fish * 300
    cchick = Chick * 200
    cmutton = Mutton * 250
    cdrink = drink * 50

    subtotal = cfish + cchick + cmutton + cdrink
    paytax = (cfish + cchick + cmutton + cdrink) * 0.25
    servicecharge = (cfish + cchick + cmutton + cdrink) / 99
    Overalltotal = subtotal + paytax + servicecharge

    total.set(subtotal)
    tax.set(paytax)
    scharge.set(servicecharge)
    overall.set(Overalltotal)

def res():
    orderno.set("")
    Fishmeal.set("")
    Chickenmeal.set("")
    MuttonMeal.set("")
    drinks.set("")
    total.set("")
    scharge.set("")
    tax.set("")
    overall.set("")

def ex():
    a.destroy()

def pric():
    b = Tk()
    b.title("Price List")
    b.geometry('680x440')

    ##LABELS IN  PRICE SCREEN

    lbl1 = Label(b, text="ITEMS", padx=16, pady=8, font=('aria', 16, 'bold')).grid(row=2, column=1)
    lbl1 = Label(b, text="PRICE/QUANTITY", padx=16, pady=8, font=('aria', 16, 'bold')).grid(row=2, column=3)

    lbl1 = Label(b,text="Fish Meal :",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=4,column=1)
    lbl1 = Label(b, text="300",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=4, column=3)

    lbl2 = Label(b, text="Chicken Meal :",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=6, column=1)
    lbl2 = Label(b, text="200",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=6, column=3)

    lbl3 = Label(b, text="Mutton Meal :",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=8, column=1)
    lbl3 = Label(b, text="250",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=8, column=3)

    lbl4 = Label(b, text="Drinks :",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=10, column=1)
    lbl4 = Label(b, text="50",padx=16,pady=8,font=( 'aria' ,16, 'bold' )).grid(row=10, column=3)


    b.mainloop()


##LABELS AND ENTRIES IN HOME SCREEN

Label(f1,padx=16,pady=8,text="Order No:",font=( 'aria' ,16, 'bold' )).grid(row=1,column=1)
Entry(f1,textvariable=orderno,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=1,column=2)

Label(f1,padx=16,pady=8,text="Fish Meal:",font=( 'aria' ,16, 'bold' )).grid(row=3,column=1)
Entry(f1,textvariable=Fishmeal,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=3,column=2)

Label(f1,padx=16,pady=8,text="Chicken Meal:",font=( 'aria' ,16, 'bold' )).grid(row=5,column=1)
Entry(f1,textvariable=Chickenmeal,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=5,column=2)

Label(f1,padx=16,pady=8,text="Mutton Meal:",font=( 'aria' ,16, 'bold' )).grid(row=7,column=1)
Entry(f1,textvariable=MuttonMeal,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=7,column=2)

Label(f1,padx=16,pady=8,text="Drinks:",font=( 'aria' ,16, 'bold' )).grid(row=1,column=3)
Entry(f1,textvariable=drinks,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=1,column=4)

Label(f1,padx=16,pady=8,text="Total:",font=( 'aria' ,16, 'bold' )).grid(row=3,column=3)
Entry(f1,textvariable=total,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=3,column=4)

Label(f1,padx=16,pady=8,text="Tax:",font=( 'aria' ,16, 'bold' )).grid(row=5,column=3)
Entry(f1,textvariable=tax,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=5,column=4)

Label(f1,padx=16,pady=8,text="Service Charge:",font=( 'aria' ,16, 'bold' )).grid(row=7,column=3)
Entry(f1,textvariable=scharge,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=7,column=4)

Label(f1,padx=16,pady=8,text="Overall Cost:",font=( 'aria' ,16, 'bold' )).grid(row=9,column=2)
Entry(f1,textvariable=overall,font=( 'aria' ,16, 'bold' ),bd=6,insertwidth=4,bg="sky blue" ,justify='right').grid(row=9,column=3)

lblTotal = Label(f1,text="--------------------------------------------------------------------------",fg="white")
lblTotal.grid(row=8,columnspan=3)
lblTotal = Label(f1,text="--------------------------------------------------------------------------",fg="white")
lblTotal.grid(row=10,columnspan=3)

Label(f2,padx=16,pady=8,text="By -",font=( 'aria' ,20, 'bold','italic','underline' )).grid(row=1,column=1)
Label(f2,padx=16,pady=8,text=" Barath Kumar C",font=( 'aria' ,20, 'bold','italic','underline' )).grid(row=3,column=2)



btnTotal=Button(f1,text="PRICE",command=pric,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, bg="powder blue")
btnTotal.grid(row=11, column=1)

btnTotal=Button(f1, text="TOTAL",command=tot,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, bg="powder blue")
btnTotal.grid(row=11, column=2)

btnreset=Button(f1,text="RESET",command=res,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10,  bg="powder blue")
btnreset.grid(row=11, column=3)

btnexit=Button(f1,text="EXIT",command=ex,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10,  bg="powder blue")
btnexit.grid(row=11, column=4)

a.mainloop()
