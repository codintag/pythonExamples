from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

cal = Tk()
cal.title("Calculatrice")
operator = ""
text_input = StringVar()
#for relief = RIDGE, FLAT, RAISED, SUNKEN, GROOVE
txtdisplay = Entry(cal,relief=RIDGE, font=('arial', 16, 'bold'), textvariable=text_input, bd=19, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4, pady=2)

myBtn7 = Button(cal, padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="7", bg="tomato", command=lambda:btnClick(7)).grid(row=1, column=0)

myBtn8 = Button(cal,padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="8", bg="tomato", command=lambda:btnClick(8)).grid(row=1, column=1)

myBtn9 = Button(cal,padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="9", bg="tomato", command=lambda:btnClick(9)).grid(row=1, column=2)

Addition = Button(cal,padx=13, pady=16, bd=4, fg="black", font=('arial', 18, 'bold'), text="+", bg="tomato", command=lambda:btnClick("+")).grid(row=1, column=3)
#============================================================
myBtn4 = Button(cal,padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="4", bg="tomato", command=lambda:btnClick(4)).grid(row=2, column=0)

myBtn5 = Button(cal,padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="5", bg="tomato", command=lambda:btnClick(5)).grid(row=2, column=1)

myBtn6 = Button(cal,padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="6", bg="tomato", command=lambda:btnClick(6)).grid(row=2, column=2)

Subtraction = Button(cal,padx=16, pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="-", bg="tomato", command=lambda:btnClick("-, command=lambda:btnClick(7)")).grid(row=2, column=3)
#============================================================
myBtn1 = Button(cal,padx=16,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="1", bg="tomato", command=lambda:btnClick(1)).grid(row=3, column=0)

myBtn2 = Button(cal,padx=16,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="2", bg="tomato", command=lambda:btnClick(2)).grid(row=3, column=1)

myBtn3 = Button(cal,padx=16,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="3", bg="tomato", command=lambda:btnClick(3)).grid(row=3, column=2)

Multiply = Button(cal,padx=15,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="*", bg="tomato", command=lambda:btnClick("*")).grid(row=3, column=3)
#==============================================================
myBtn0 = Button(cal,padx=16,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="0", bg="tomato", command=lambda:btnClick(0)).grid(row=4, column=0)

myBtnClear = Button(cal,padx=14,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="C", bg="tomato", command = btnClearDisplay).grid(row=4, column=1)

myBtnEqual = Button(cal,padx=16,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="=", bg="tomato", command = btnEqualsInput).grid(row=4, column=2)

Division = Button(cal,padx=16,pady=16, bd=4, fg="black", font=('arial', 19, 'bold'), text="/", bg="tomato", command=lambda:btnClick("/")).grid(row=4, column=3)

cal.mainloop()