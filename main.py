from functions import text_alert, create_buttons, root, ents

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

if __name__ == '__main__':
    root.geometry("800x550")
    root.title("Khwarizm Consulting")
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    text_alert()
    create_buttons()
    root.mainloop()
