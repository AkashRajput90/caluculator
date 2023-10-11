from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("270x330")
root.configure(bg="black")
root.resizable(False,False)

expression = ""

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clearbtn(item):
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""

l1 = Label(root,text="Calculator",font="roman 25 bold",fg="grey",bg="black")
l1.pack()

input_text = StringVar()


e1 = Entry(root,textvariable=input_text,width="42",bg="grey")
e1.place(x=5,y=40,height=30)

b1 = Button(root,text="9",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("9"))
b1.place(x=20,y=80,height=50,width=50)

b2 = Button(root,text="8",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("8"))
b2.place(x=80,y=80,height=50,width=50)

b3 = Button(root,text="7",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("7"))
b3.place(x=140,y=80,height=50,width=50)

b4 = Button(root,text="+",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("+"))
b4.place(x=200,y=80,height=50,width=50)

b5 = Button(root,text="6",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("6"))
b5.place(x=20,y=140,height=50,width=50)

b6 = Button(root,text="5",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("5"))
b6.place(x=80,y=140,height=50,width=50)

b7 = Button(root,text="4",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("4"))
b7.place(x=140,y=140,height=50,width=50)

b8 = Button(root,text="*",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("*"))
b8.place(x=200,y=140,height=50,width=50)

b9 = Button(root,text="3",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("3"))
b9.place(x=20,y=200,height=50,width=50)

b10 = Button(root,text="2",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("2"))
b10.place(x=80,y=200,height=50,width=50)

b11 = Button(root,text="1",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("1"))
b11.place(x=140,y=200,height=50,width=50)

b12 = Button(root,text="-",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("-"))
b12.place(x=200,y=200,height=50,width=50)

b13 = Button(root,text="Clear",font="bold 13",bg="grey",activebackground="grey", command = lambda: clearbtn(""))
b13.place(x=20,y=260,height=50,width=50)

b14 = Button(root,text="0",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("0"))
b14.place(x=80,y=260,height=50,width=50)

b15 = Button(root,text="=",font="bold 15",bg="grey",activebackground="grey",command = lambda : bt_equal())
b15.place(x=140,y=260,height=50,width=50)

b16 = Button(root,text="/",font="bold 15",bg="grey",activebackground="grey", command = lambda: btn_click("/"))
b16.place(x=200,y=260,height=50,width=50)



root.mainloop()