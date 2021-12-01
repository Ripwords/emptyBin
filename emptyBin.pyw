import os
import time
import winshell
from global_hotkeys import *
from winotify import Notification, audio

is_alive = True

dirname = os.path.dirname(__file__)
icon_path = os.path.join(dirname, 'bin.ico')


def empty_bin():
    try:
        msg = 'Your recycle bin has been emptied ლ(╹◡╹ლ)'
        winshell.recycle_bin().empty(
            confirm=False, 
            show_progress=False, 
            sound=False
        )

        toast = Notification(
            app_id='Recycle Bin',
            title='Empty recycle bin',
            msg=msg,
            icon=icon_path,
            duration="short"
        )

        toast.set_audio(audio.Mail, loop=False)


    except:
        msg = 'Bin is already empty ¯\_(ツ)_/¯'
        toast = Notification(
            app_id='Recycle Bin',
            title='Empty recycle bin',
            msg=msg,
            icon=icon_path,
            duration="short"
        )

        toast.set_audio(audio.Reminder, loop=False)


    toast.build().show()


bindings = [
    [["control", "shift", "D"], None, empty_bin]
]

register_hotkeys(bindings)
start_checking_hotkeys()

while is_alive:
    time.sleep(0.1)
