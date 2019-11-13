# -*- coding: utf-8 -*
import urwid

from uwapp.widget.uw_dialog import UWDialog
from uwapp.widget.uw_linebox import UWLineBox
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class AboutDialog(UWDialog):
    def __init__(self, app, title, content, width, height):
        self.content = content
        super(AboutDialog, self).__init__(app, title, width, height)
        self.define_dialog()
        

    def define_dialog(self):
        # align=center, only for fixed size dialog
        closeButtonTitle = "Close"
        padding = " " * ((self.width -6 - len(closeButtonTitle))//2)
        closeButton = urwid.Button(padding+"Close"+padding)
        urwid.connect_signal(closeButton, 'click', lambda button: self.close())
        window = []
        window.extend([
            urwid.AttrMap(urwid.Text(self.content),'dialog.content'),
            urwid.AttrMap(closeButton, 'button')
        ])
        self.widget = urwid.AttrMap(UWLineBox(
            urwid.AttrMap(urwid.Filler(urwid.Pile(window)), 'dialog'),
            title = self.title
        ), 'dialog')