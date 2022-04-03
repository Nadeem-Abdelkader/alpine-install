import json
from tkinter import *
from tkinter import messagebox

fields = ('Username', 'Group', 'Active Director Name', 'Password', 'Re-enter Password', 'Hostname', 'Interface name',
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
    print(entries)
    for i in range(len(entries)-1):
        print(entries[fields[i]].get())
    # with open("student.json", "w") as write_file:
    #     json.dump(entries, write_file, indent=4)

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
    b1 = Button(root, text='Submit', command=(lambda e=ents: submit(e)))
    b1.pack()
    b2 = Button(root, text='Quit', command= quit)
    b2.pack()
    root.mainloop()
