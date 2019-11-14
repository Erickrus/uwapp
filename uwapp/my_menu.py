# -*- coding: utf-8 -*
import urwid

from uwapp.widget.uw_menu import UWMenu
from uwapp.about_dialog import AboutDialog
from uwapp.preference_dialog import PreferenceDialog
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class MyMenu(UWMenu):
    menus = [{
        "title": u"File",
        "type": "menu",
        "subMenu": [
            {
                "title": u"Open",
                "type": "menuItem",
                "callback": None
            }, {
                "title": u"Save",
                "type": "menuItem",
                "callback": None
            }, {
                "title": u"Save As",
                "type": "menuItem",
                "callback": None
            },
            {
                "title": u"Recent",
                "type": "subMenu",
                "subMenu": [{
                        "title": u"uwapp.py",
                        "type": "menuItem",
                        "callback": None
                    }, {
                        "title": u"uw_menu.py",
                        "type": "menuItem",
                        "callback": None
                    },
                ]
            }, {
                "title": "", # 不可以缺少
                "type": "divider",
            }, {
                "title": "Exit",
                "type": "menuItem",
                "callback": "self.exit_program"
            }
        ]
    }, {
        "title": u"Edit",
        "type": "menu",
        "subMenu": [{
            "title": u"Preference",
            "type": "menuItem",
            "callback": "self.preference"
        }]
    }, {
        "title": u"Help",
        "type": "menu",
        "subMenu": [{
            "title": u"About",
            "type": "menuItem",
            "callback": "self.about"
        }]
        
    }]
    
    def __init__(self, app, menuData):
        super(MyMenu, self).__init__(app, menuData)

    def exit_program(self, button):
        raise urwid.ExitMainLoop()

    def about(self, button):
        self.app.clear_menu()
        
        aboutDialog = AboutDialog(
            self.app, 
            'About', 
            'UWApp 0.5\n\nTUI based on urwid library in Python 3\nHu, Ying-Hao (hyinghao@hotmail.com)\n', 
            46, 8)
        aboutDialog.show()
        
        self.app.set_focus_path(['body',1])
        
        
    def preference(self, button):
        self.app.clear_menu()
        
        preferenceDialog = PreferenceDialog(
            self.app, 
            'Preference', 
            46, 12)
        preferenceDialog.show()
        
        self.app.set_focus_path(['body',1])
