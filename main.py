from functions import text_alert, create_buttons, initialise_window, root

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
    text_alert()
    create_buttons()
    root.mainloop()
