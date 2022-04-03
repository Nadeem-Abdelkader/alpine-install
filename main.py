import json
from tkinter import *
from tkinter import messagebox

fields = ('Username', 'Group', 'Active Directory Name', 'Password', 'Re-enter Password', 'Hostname', 'Interface name',
          'IP address', 'Network', 'Gateway', 'DNS')

def make_form(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "")
        row.pack(side=TOP, fill=X, padx=25, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def makeLabel(root):
    txt_title = Label(root, width=0, font=('arial', 24), text="Khwarizm Consulting")
    txt_title.pack(side=TOP,padx=5, pady=5)


def submit(entries):
    cont = True
    for i in range(len((entries))):
        if entries[fields[i]].get() == "":
            cont = False
            txt_result.config(text="Please complete the required field!", fg="red")
    if cont:
        dict = {}
        for i in range(len(entries)):
            dict[fields[i]] = entries[fields[i]].get()

        # print(dict)

        with open("output.json", "a") as write_file: # change "a" to "w" if you want to overwrite instead of append
            json.dump(dict, write_file, indent=4)

def quit():
    result = messagebox.askquestion('Khwarizm Consulting', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
    return

if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600")
    root.title("Khwarizm Consulting")
    makeLabel(root)
    ents = make_form(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    global txt_result
    txt_result = Label(root)
    txt_result.pack()
    b1 = Button(root, text='Submit', command=(lambda e=ents: submit(e)))
    b1.pack()
    b2 = Button(root, text='Quit', command= quit)
    b2.pack()
    root.mainloop()
