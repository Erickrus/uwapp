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
urwid.MainLoop(app, palette=[('reversed', 'standout', '')]).run()



