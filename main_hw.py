from tkinter import *
window = Tk()
window.title("Distance calculator")
window.geometry("800x400")
window.config(background="white")

def convert():
    speed = enter.get()
    time = enter2.get()
    distance = int(speed)*int(time)
    label4.config(text="Distance: {}m".format(distance),fg="black")

label1 = Label(window,text="Distance calculator",font=("times",14))
label1.pack()

speed = Label(window,text="Enter speed in m/s:",bg="light grey",font=("times",16)).place(x=150,y=100)
enter = Entry(window,width=30)
enter.place(x=315,y=100,height=27)

time = Label(window,text="Enter time in seconds:",bg="light grey",font=("times",16)).place(x=150,y=150)
enter2 = Entry(window,width=30)
enter2.place(x=350,y=150,height=27)

label4 = Label(window,bg="dark orange",font=("times",16))
label4.place(x=200,y=200)
button = Button(window,text="Convert",height=1,width=25,bg="green",font=("times",14,),command=convert).place(x=265,y=300)




window.mainloop()