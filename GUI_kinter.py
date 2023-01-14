from tkinter import*

root = Tk()
root.geometry("1029x500+180+50")
root.configure(bg='#00202e')
root.title("difference calculator")

#________________Creat a Frame_________________
frame1 = LabelFrame(root,
    text='Celsius to Fahrenheit', 
    borderwidth=1, 
    font=('Andalus',16,"bold italic"), 
    padx=35, 
    pady=5,
    bg="#00202e", 
    fg="#c7d9df")

frame2 = LabelFrame(root, 
    text='Fahrenheit to Celsius',
    borderwidth=1, 
    font=('Andalus',16,"bold italic"), 
    padx=35, 
    pady=5, 
    bg="#00202e", 
    fg="#c7d9df")

frame1.grid(row=0,column=0, columnspan=2, rowspan=2,)
frame2.grid(row=0,column=3, columnspan=2, rowspan=2,)

#______________record Section_______________
record_frame = LabelFrame(root, 
    borderwidth=0, 
    font=('Andalus',16,"bold italic"), 
    padx=80,
    pady=5, 
    bg="#00202e", 
    fg="#c7d9df")

record_frame.grid(row=3,column=0,columnspan=5, rowspan=2,)
Label(record_frame,bg="#00202e").pack()

#Entry function_______________________________


def entry_1():
    get_entry1= float(entry1.get())
    F = (get_entry1* 9/5)+32  
    global a
    a=" "  
    Label(frame1, 
        text= f"{get_entry1}°C {a} = {a} {F}°F" ,
        bg="#00202e",
        fg="#fff", 
        font=('Franklin Gothic Demi',16,"bold"),
        pady=17).grid(row=3, column=0)

    #____record
    Label(record_frame, 
        text= f"{get_entry1}°C {a} = {a} {F}°F",
        font=('Franklin Gothic Demi',14),
        bg="#00202e",
        fg="#fff").pack()  

a=" "
Label(frame1, 
    text= f"0.00°C {a} = {a} 0.00°F", 
    bg="#00202e",
    fg="#fff", 
    font=('Franklin Gothic Demi',16,"bold"),
    pady=17).grid(row=3, column=0)

def entry_2():
    get_entry2= float(entry2.get())
    c = 5/9*(get_entry2 - 32)
    b=" "
    Label(frame2, 
        text= f"{ get_entry2 }°F {b} = {b} {c}°C", 
        bg="#00202e",
        fg="#fff", 
        font=('Franklin Gothic Demi',16,"bold"), 
        pady=17).grid(row=3, column=1)
    
    #____record
    Label(record_frame, 
        text=f"{ get_entry2 }°F {b} = {b} {c}°C",
        font=('Franklin Gothic Demi',14),
        bg="#00202e",
        fg="#fff").pack()
        
b=" "
Label(frame2,
    text= f"0.00°F {b} = {b} 0.00°C", 
    bg="#00202e",
    fg="#fff", 
    font=('Franklin Gothic Demi',16,"bold"), 
    pady=17).grid(row=3, column=1)    







#_____________Frame one Section________________
entry1 = Entry(frame1,width=35, font=('Arial',"16","bold"), borderwidth=10, bg="#01394a", fg="#fff", relief="groove", )
entry1.grid(row=0, column =0)
entry1.focus_set()

Label(frame1,bg="#00202e").grid(row=1, column=0)
#____Frame1 button_____
btn1 = Button(frame1, 
              text="convert",
              fg="#fff",bg="#00394a",
              borderwidth=0,
              padx=60,
              pady=3,
              font=('Franklin Gothic Demi',13,"bold italic"),
              command=entry_1 )

btn1.grid(row=2, column =0)


#_____________Frame Two Section________________
entry2 = Entry(frame2,width=35, font=('Arial',"16","bold"), borderwidth=10, bg="#01394a", fg="#fff", relief="groove",)
entry2.grid(row=0, column =1)

Label(frame2,bg="#00202e").grid(row=1, column=1)
#____Frame2 button_____
btn2 = Button(frame2,
              text="convert",
              fg="#fff",
              bg="#00394a",
              borderwidth=0,
              padx=60,
              pady=3,
              font=('Franklin Gothic Demi',13,"bold italic"),
              command=entry_2)
btn2.grid(row=2, column =1)

root.mainloop()


