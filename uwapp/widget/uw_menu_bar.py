# -*- coding: utf-8 -*
import urwid
from urwid.monitored_list import MonitoredList, MonitoredFocusList
from uwapp.widget.uw_menu_button import UWMenuButton
import uwapp.util.logging as logging

logger = logging.getLogger(__name__)


class UWMenuBar(urwid.Columns):
    def __init__(self, widget_list):
        newWidgetList = []
        for widget in widget_list:
            widgetSize = 0
            if "text" in dir(widget):
                widgetSize = len(widget.text)
            elif "label" in dir(widget):
                widgetSize = len(widget.label)

            newWidgetList.append((widgetSize+4, widget))
        #newWidgetList.append(('weight',99, urwid.Text(' ')))
        super(UWMenuBar, self).__init__(
            newWidgetList,
            dividechars=0
        )