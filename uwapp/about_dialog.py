# -*- coding: utf-8 -*
import urwid

from uwapp.widget.uw_dialog import UWDialog
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class AboutDialog(UWDialog):
    def __init__(self, app, title, content, width, height):
        self.content = content
        super(AboutDialog, self).__init__(app, title, width, height)
        self.define_dialog()
        

    def define_dialog(self):
        closeButton = urwid.Button("Close")
        urwid.connect_signal(closeButton, 'click', lambda button: self.close())
        window = self.baseWindow[:2]
        window.extend([
            urwid.Text(self.content),
            closeButton
        ])
        self.widget = urwid.LineBox(
            urwid.Filler(urwid.Pile(window))
        )