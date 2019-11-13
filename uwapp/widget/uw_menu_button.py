# -*- coding: utf-8 -*

import urwid

class UWMenuButton(urwid.Button):
    button_left = urwid.Text(' ')
    button_right = urwid.Text(' ')
    def __init__(self, label, on_press=None, user_data=None):
        super(UWMenuButton, self).__init__(label, on_press, user_data)
        
