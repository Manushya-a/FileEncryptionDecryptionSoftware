import tkinter as tk
from tkinter import *
from TkinterDnD2 import DND_FILES, TkinterDnD
from cryptography.fernet import Fernet


def drop_inside_file_box(event):
    global file_loc

    file_loc = event.data
    filebox.insert("end", "File location : "+event.data)
    if event.data.endswith(".txt"):
        filebox.insert("end", "File content: ")
        with open(event.data, "r") as file:
            for line in file:
                line = line.strip()
                filebox.insert("end", f"{line}\n")


def encrypt():

    with open(file_loc, 'r+') as f:
        text = f.read()
        f.truncate(0)
        f.seek(0)

        key = Fernet.generate_key()
        fernet = Fernet(key)

        enc_text = fernet.encrypt(text.encode())

        f.write(enc_text.decode('utf-8'))

        tbox.insert(END, key.decode('utf-8'))

        f.close()

def decrypt():

    with open(file_loc, 'r+') as f:
        text = f.read()
        f.truncate(0)
        f.seek(0)

        key = tbox.get(1.0, END)
        fernet = Fernet(key)

        dec_message = fernet.decrypt(text).decode()

        f.write(dec_message)

        f.close()


def reset():
    tbox.delete(1.0, END)
    filebox.delete(1, END)

    file_loc = None


def main_screen():
    global filebox
    global tbox

    screen = TkinterDnD.Tk()
    screen.geometry('800x600')

    Label(screen, text="Selected File", font="arial", fg="white", bg="#00bd56").place(x=5, y=10)

    filebox = tk.Listbox(screen, selectmode=tk.SINGLE, background="#ffe0d6")
    filebox.place(x=10, y=40, height=200, width=780)
    filebox.drop_target_register(DND_FILES)
    filebox.dnd_bind("<<Drop>>", drop_inside_file_box)

    Label(screen, text="Encryption Key", font="arial", fg="white", bg="#00bd56").place(x=5, y=250)

    tbox = tk.Text(screen, background="#EA526F")
    tbox.place(x=10, y=280, height=200, width=780)

    Button(text="ENCRYPT", height="2", width="23", bg="#ed3833", fg="white", bd=0, command=encrypt, ).place(x=10, y=490)
    Button(text="DECRYPT", height="2", width="23", bg="#00bd56", fg="white", bd=0, command=decrypt, ).place(x=200, y=490)
    Button(text="RESET", height="2", width="50", bg="#1089ff", fg="white", bd=0, command=reset, ).place(x=10, y=530)

    screen.mainloop()


main_screen()
