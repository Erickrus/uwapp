# -*- coding: utf-8 -*
import urwid
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)

class UWLineBox(urwid.LineBox):
    def __init__(self, original_widget, title="", title_align="center"):
        super(UWLineBox, self).__init__(
            original_widget, 
            title=title, 
            title_align=title_align,
            tlcorner=u'╔', 
            tline=u'═', 
            lline=u'║',
            trcorner=u'╗', 
            blcorner=u'╚', 
            rline=u'║',
            bline=u'═', 
            brcorner=u'╝')
        


