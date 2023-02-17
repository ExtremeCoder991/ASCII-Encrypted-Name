from tkinter import * 

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = 'blue')

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="light yellow", fg="black")
unlabel = Label(root, text = "Encrypted Name: ", bg="light yellow", fg="black")

def asciiConvertor(): 
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        encrypted = int(ord(letter))
        asciiname = encrypted - 1
        unlabel["text"] += str(chr(asciiname))
        
btn=Button(root, text="Show name in Ascii", command=asciiConvertor, bg='gold', fg = 'black')
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)
unlabel.place(relx=0.5, rely = 0.7, anchor=CENTER)


root.mainloop()
