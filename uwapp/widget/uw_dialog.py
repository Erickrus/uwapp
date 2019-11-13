# -*- coding: utf-8 -*
import urwid
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)


class UWDialog:
    def __init__(self, app, title, width, height):
        self.app = app
        self.baseWindow = [urwid.Text(title),  urwid.Divider(u'─'), urwid.Text("")]
        self.width = width
        self.height = height
        self.define_dialog()

    def define_dialog(self):
        self.widget = urwid.LineBox(
            urwid.Filler(urwid.Pile(self.baseWindow))
        )
        
    def close(self):
        self.app.clear_popup()

    def popup(self):
        self.app.fill.original_widget = urwid.Overlay(
            self.widget,
            self.app.fill.original_widget,
            align='center', width=('relative', 0),
            valign='middle', height=('relative', 0),
            min_width=self.width,
            min_height=self.height,
            left=0,
            right = 0,
            top=0,
            bottom = 0
        )
