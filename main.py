import json
import os
from tkinter import *
from tkinter import messagebox

fields = ('User Name', 'Group Name', 'Active Directory Name', 'Password', 'Re-enter Password', 'Host Name',
          'Interface Name', 'IP address', 'Network Name', 'Gateway', 'DNS')

"""
On Startup

Enable and run dbus for GUI

# rc-service dbus start
# rc-update add dbus

Disable lxdm - replace with our script

# rc-service lxdm stop
# rc-update remove lxdm

import os

cmd = 'rc-service dbus start'
os.system(cmd)

cmd = 'rc-update add dbus'
os.system(cmd)

cmd = 'rc-service lxdm stop'
os.system(cmd)

cmd = 'rc-update remove lxdm'
os.system(cmd)

"""

users_file_name = "users.json"


def make_form(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        if field == "Password" or field == "Re-enter Password":
            ent = Entry(row, show="*")
        else:
            ent = Entry(row)
        ent.insert(0, "")
        row.pack(side=TOP, fill=X, padx=25, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def makeLabel(root):
    txt_title = Label(root, width=0, font=(
        'arial', 24), text="Khwarizm Consulting")
    txt_title.pack(side=TOP, padx=5, pady=5)


def read_from_json(filename):
    input_file = open(filename)
    json_array = json.load(input_file)
    user_list = []

    for user in json_array:
        user_details = {fields[0]: None, fields[1]: None, fields[2]: None, fields[3]: None,
                        fields[4]: None, fields[5]: None, fields[6]: None, fields[7]: None,
                        fields[8]: None, fields[9]: None, fields[10]: None, fields[0]: user[fields[0]],
                        fields[1]: user[fields[1]], fields[2]: user[fields[2]],
                        fields[3]: user[fields[3]], fields[4]: user[fields[4]],
                        fields[5]: user[fields[5]], fields[6]: user[fields[6]],
                        fields[7]: user[fields[7]], fields[8]: user[fields[8]],
                        fields[9]: user[fields[9]], fields[10]: user[fields[10]]}

        user_list.append(user_details)

    return user_list


def submit(entries):
    cont = True
    for i in range(len((entries))):
        if entries[fields[i]].get() == "":
            cont = False
            txt_result.config(
                text="Please complete the required field!", fg="red")
    if entries[fields[3]].get() != entries[fields[4]].get():
        cont = False
        txt_result.config(text="Passwords do not match!", fg="red")

    if cont:
        dict = {}
        for i in range(len(entries)):
            dict[fields[i]] = entries[fields[i]].get()

        users_list = []
        if os.path.exists(users_file_name) and os.stat(users_file_name).st_size != 0:
            users_list = read_from_json(users_file_name)
            users_list.append(dict)
        else:
            users_list.append(dict)

        # print(dict)

        filename = str(entries[fields[0]].get()).replace(" ", "") + ".json"
        filename = "/Users/nadeem/Documents/Khwarizm/Alpine/alpine-install/records/" + filename
        filename = users_file_name
        # with open(filename,
        #           "w") as write_file:  # change "w" to "a" if you want to append instead of overwrite
        #     json.dump(dict, write_file, indent=4)

        jsonString = json.dumps(users_list, indent=4)
        jsonFile = open(users_file_name, "w")
        jsonFile.write(jsonString)
        jsonFile.close()

        txt_result.config(text="Successfully submitted data!", fg="green")

        clear(entries)

    """
    After submitting
    
    Enable and run dbus for GUI
    
    # rc-service dbus start
    # rc-update add dbus
    
    Enable and run lxdm
    
    # rc-service lxdm start
    # rc-update add lxdm
    
    import os

    cmd = 'rc-service dbus start'
    os.system(cmd)
    
    cmd = 'rc-update add dbus'
    os.system(cmd)
    
    cmd = 'rc-service lxdm start'
    os.system(cmd)
    
    cmd = 'rc-update add lxdm'
    os.system(cmd)
    """


def clear(entries):
    for i in range(len(fields)):
        entries[fields[i]].delete(0, 'end')
    txt_result.config(text="Cleared form!", fg="green")


def quit():
    result = messagebox.askquestion(
        'Khwarizm Consulting', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
    return


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x550")
    root.title("Khwarizm Consulting")
    makeLabel(root)
    ents = make_form(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    global txt_result
    txt_result = Label(root)
    txt_result.pack()
    top = Frame(root)
    top.pack(side=TOP)
    b = Button(root, text="Submit", command=(lambda e=ents: submit(e)))
    c = Button(root, text="Clear", command=(lambda e=ents: clear(e)))
    d = Button(root, text="Quit", command=quit)

    b.pack(in_=top, side=LEFT)
    c.pack(in_=top, side=LEFT)
    d.pack(in_=top, side=LEFT)

    root.mainloop()
