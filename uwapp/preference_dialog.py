# -*- coding: utf-8 -*
import urwid
import json
import os

from uwapp.widget.uw_dialog import UWDialog
from uwapp.widget.uw_linebox import UWLineBox
import uwapp.util.logging as logging
from uwapp.widget.uw_theme import UWTheme

logger = logging.getLogger(__name__)

class PreferenceDialog(UWDialog):
    preferenceFilename = "./uwapp.json"
    @staticmethod
    def load_preference():
        if os.path.exists(PreferenceDialog.preferenceFilename):
            with open(PreferenceDialog.preferenceFilename, "r") as f:
                preference = json.loads(f.read())
        else:
            preference = {"theme":"turboVision"}
        return preference
    
    @staticmethod
    def save_preference(preference):
        with open(PreferenceDialog.preferenceFilename, "w") as f:
            f.write(json.dumps(preference))

    def __init__(self, app, title, width, height):
        self.app = app
        self.baseWindow = []
        self.width = width
        self.height = height
        self.title = title
        self.themes = ["TurboVision","RedHat","Console"]
        self.preference = PreferenceDialog.load_preference()
        self.define_dialog()
        
    def apply(self):
        theme = "turboVision"
        for o in self.options:
            if o.get_state() is True:
                theme = o.get_label()
                break
        theme = theme[0].lower()+ theme[1:]
        self.save_preference({"theme":theme})
        self.close()
        raise Exception("restart")

    def define_dialog(self):
        # align=center, only for fixed size dialog
        self.options = []
        
        applyButtonTitle = "Save and restart"
        padding = " " * ((self.width -6 - len(applyButtonTitle))//2)
        applyButton = urwid.Button(padding+applyButtonTitle+padding)
        urwid.connect_signal(applyButton, 'click', lambda button: self.apply())
        window = []
        
        radioButtonInstances = []
        for i in range(len(self.themes)):
            radioButtonName =  self.themes[i]
            selected = False
            if self.themes[i].lower() == self.preference["theme"].lower():
                selected = True
            radioButtonInstance = urwid.AttrMap(
                urwid.RadioButton(
                    self.options, 
                    radioButtonName,
                    selected
                ), 
                'radiobutton'
            )
            radioButtonInstances.append(radioButtonInstance)

        
        radioButtons = urwid.GridFlow(radioButtonInstances, self.width - 2, 3, 1, 'left')
        
        window.extend([
            urwid.AttrMap(urwid.Text("Themes\n"),'dialog.content'),
            urwid.AttrMap(radioButtons,'dialog.content'),
            urwid.AttrMap(urwid.Text("\n"),'dialog.content'),
            urwid.AttrMap(applyButton, 'button')
        ])
        self.widget = urwid.AttrMap(UWLineBox(
            urwid.AttrMap(urwid.Filler(urwid.Pile(window)), 'dialog'),
            title = self.title
        ), 'dialog')
        
        