"""
INSTALL Application
- Records all submitted user records as a an array of json objects in the file "users.json"

Created by: Nadeem Abdelkader on 3/4/2022
Last updated by Nadeem Abdelkader on 4/4/2022

GUI framework = Tkinter

This file contains the helper function to be called from main.py
"""

# importing the necessary libraries for working with csv, JSON, Tkinter and MySQL
import json
import os
from tkinter import Frame, Label, Entry, X, LEFT, RIGHT, YES, messagebox, Button, Tk, TOP

# declaring the constants to be used everywhere in the module
FIELDS = ('User Name', 'Group Name', 'Active Directory Name', 'Password', 'Re-enter Password', 'Host Name',
          'Interface Name', 'IP address', 'Network Name', 'Gateway', 'DNS')
USERS_FILENAME = os.getcwd() + "/tmp/users.json"
# print(USERS_FILENAME)


def make_form(root, fields):
    """
    This function created the actual GUI form using Tkinter Entry, Label, and Frames
    :param root: root Tkinter window
    :param fields: array of strings that include the field names to createb the form according to
    :return: an array of Tkinter entries
    """
    makeLabel(root)
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
    """
    This function adds the GUI heading
    :param root: root Tkinter window
    :return: void
    """
    txt_title = Label(root, width=0, font=(
        'arial', 24), text="Khwarizm Consulting")
    txt_title.pack(side=TOP, padx=5, pady=5)
    return


# def read_from_json(filename):
#     """
#     This function reads the previous users data from a .json file that can contain 0 or more json objects
#     (stored as an array of json objects)
#     :param filename: file to get the records from
#     :return: an array of json objects
#     """
#     input_file = open(filename)
#     json_array = json.load(input_file)
#     user_list = []
#
#     for user in json_array:
#         user_details = {FIELDS[0]: None, FIELDS[1]: None, FIELDS[2]: None, FIELDS[3]: None,
#                         FIELDS[4]: None, FIELDS[5]: None, FIELDS[6]: None, FIELDS[7]: None,
#                         FIELDS[8]: None, FIELDS[9]: None, FIELDS[10]: None, FIELDS[0]: user[FIELDS[0]],
#                         FIELDS[1]: user[FIELDS[1]], FIELDS[2]: user[FIELDS[2]],
#                         FIELDS[3]: user[FIELDS[3]], FIELDS[4]: user[FIELDS[4]],
#                         FIELDS[5]: user[FIELDS[5]], FIELDS[6]: user[FIELDS[6]],
#                         FIELDS[7]: user[FIELDS[7]], FIELDS[8]: user[FIELDS[8]],
#                         FIELDS[9]: user[FIELDS[9]], FIELDS[10]: user[FIELDS[10]]}
#
#         user_list.append(user_details)
#
#     return user_list


def submit(entries):
    """
    This function is executed when the user fills in all the inforamtion and clicks submit.
    It takes all the entered information an writes it to a .json file (users.json)
    :param entries: an array of entries that contain the entered information
    :return: void
    """
    cont = True
    for i in range(len((entries))):
        if entries[FIELDS[i]].get() == "":
            cont = False
            txt_result.config(
                text="Please complete the required field!", fg="red")
    if entries[FIELDS[3]].get() != entries[FIELDS[4]].get():
        cont = False
        txt_result.config(text="Passwords do not match!", fg="red")

    if cont:
        dict = {}
        for i in range(len(entries)):
            dict[FIELDS[i]] = entries[FIELDS[i]].get()
        #
        # users_list = []
        # if os.path.exists(USERS_FILENAME) and os.stat(USERS_FILENAME).st_size != 0:
        #     users_list = read_from_json(USERS_FILENAME)
        #     users_list.append(dict)
        # else:
        #     users_list.append(dict)

        # print(dict)

        # filename = str(entries[FIELDS[0]].get()).replace(" ", "") + ".json"
        # filename = "/Users/nadeem/Documents/Khwarizm/Alpine/alpine-install/records/" + filename
        filename = USERS_FILENAME
        with open(filename,
                  "w") as write_file:  # change "w" to "a" if you want to append instead of overwrite
            json.dump(dict, write_file, indent=4)

        # jsonString = json.dumps(users_list, indent=4)
        # jsonFile = open(USERS_FILENAME, "w")
        # jsonFile.write(jsonString)
        # jsonFile.close()

        txt_result.config(text="Successfully submitted data!", fg="green")

        clear(entries, True)

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
    return


def clear(entries, on_submit=False):
    """
    This function is executed when the users clicks the "clear" button.
    It resets the entire form
    :param entries: an array of entries to clear
    :return: void
    """
    for i in range(len(FIELDS)):
        entries[FIELDS[i]].delete(0, 'end')
    if not on_submit:
        txt_result.config(text="Cleared form!", fg="green")
    return


def quit():
    """
    This function is executed when the users clicks the "quit" button.
    It quits the entire application
    :return: void
    """
    result = messagebox.askquestion(
        'Khwarizm Consulting', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
    return


def text_alert():
    """
    This function creates the label where we will later add some alerts to the user like
    "please complete the required field" or "Submitted data successfully"
    :return: void
    """
    global txt_result
    txt_result = Label(root)
    txt_result.pack()
    return


def create_buttons():
    """
    This function creates 3 buttons (submit, clear, and quit) and associates them with the appropriate methods
    :return: void
    """
    top = Frame(root)
    top.pack(side=TOP)
    submit_button = Button(root, text="Submit", command=(lambda e=ents: submit(e)))
    clear_button = Button(root, text="Clear", command=(lambda e=ents: clear(e)))
    quit_button = Button(root, text="Quit", command=quit)
    submit_button.pack(in_=top, side=LEFT)
    clear_button.pack(in_=top, side=LEFT)
    quit_button.pack(in_=top, side=LEFT)
    return


def initialise_window():
    """
    This function initialises the Tkinter GUI window
    :return: root Tkinter window
    """
    global root, ents
    root = Tk()
    ents = make_form(root, FIELDS)
    # 800x465 - Alpine
    # 800x550 - Others
    root.geometry("800x550")
    root.title("Khwarizm Consulting")
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    return root


# calling function to initialise the GUI window
root = initialise_window()
