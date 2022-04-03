import json
from tkinter import *
from tkinter import messagebox

fields = ('User Name', 'Group name', 'Active Directory Name', 'Password', 'Re-enter Password', 'Host Name',
          'Interface name', 'IP address', 'Network Name', 'Gateway', 'DNS')

"""
On Startup

Enable and run dbus for GUI
Disable lxdm
"""


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
    txt_title.pack(side=TOP, padx=5, pady=5)


def submit(entries):
    cont = True
    for i in range(len((entries))):
        if entries[fields[i]].get() == "":
            cont = False
            txt_result.config(text="Please complete the required field!", fg="red")
    if entries['Password'].get() != entries['Re-enter Password'].get():
        cont = False
        txt_result.config(text="Passwords do not match!", fg="red")

    if cont:
        dict = {}
        for i in range(len(entries)):
            dict[fields[i]] = entries[fields[i]].get()

        # print(dict)

        filename = str(entries['User Name'].get()).replace(" ", "") + ".json"
        with open(filename, "w") as write_file:  # change "w" to "a" if you want to append instead of overwrite
            json.dump(dict, write_file, indent=4)

        txt_result.config(text="Successfully submitted data!", fg="green")

        for i in range(len(fields)):
            entries[fields[i]].delete(0, 'end')
        

    """
    After submitting
    
    Enable and run lxdm
    """


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
    # root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    global txt_result
    txt_result = Label(root)
    txt_result.pack()
    b1 = Button(root, text='Submit', command=(lambda e=ents: submit(e)))
    b1.pack()
    b2 = Button(root, text='Quit', command=quit)
    b2.pack()
    root.mainloop()
