# -*- coding: utf-8 -*
import urwid

from uwapp.widget.uw_menu import UWMenu
from uwapp.about_dialog import AboutDialog
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
            "title": u"Copy",
            "type": "menuItem",
            "callback": None
        }, {
            "title": u"Cut",
            "type": "menuItem",
            "callback": None
        }, {
            "title": u"Paste",
            "type": "menuItem",
            "callback": None
        }, {
            "title": u"Delete",
            "type": "menuItem",
            "callback": None
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
        
        aboutDialog = AboutDialog(self.app, 'About', 'UWApp 0.2, \nbased on urwid\n', 25, 8)
        aboutDialog.popup()
        
        self.app.set_focus_path(['body',1])
