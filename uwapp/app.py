# -*- coding: utf-8 -*
import urwid
from uwapp.my_menu import MyMenu
from uwapp.widget.uw_application import UWApplication

import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class Application(UWApplication):
    def __init__(self, menuClass):
        super(Application, self).__init__(menuClass) 

app = Application(MyMenu)

loop = urwid.MainLoop(app, palette=[
    ('dialog', 'white', 'light gray'),
    ('dialog.content', 'white', 'dark blue'),
    
    ('menubar', 'black', 'light gray'),
    ('menu', 'black', 'light gray'),
    ('button', 'black', 'light green'),
    ('background', 'dark blue', 'light gray'),
    ('reversed', 'standout', '')
]).run()
#loop.screen.set_terminal_properties(colors=256)


