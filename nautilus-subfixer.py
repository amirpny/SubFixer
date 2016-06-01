# -*- coding: utf-8 -*-

import urllib
import os
from gi.repository import Nautilus
from gi.repository import GObject
from gi.repository import Gtk

class NautilusSubFixer(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if len(files) == 0:
            return None
        
        for f in files:
            if f.get_name()[-4:] != '.srt':
                return None    
        print files[0].get_name()

        menuitem = Nautilus.MenuItem(name='NautilusSubFixer::SubFixer',
                label='Fix subtitle file',
                tip='Fix subtitle file',
                icon='gtk-edit')
        menuitem.connect('activate', self.on_menuitem_activated, files)

        return menuitem,
    
    def on_menuitem_activated(self, menuitem, files):
        f_uri = ""
        for f in files:
            f_uri += "'%s' " % urllib.unquote(f.get_uri()[7:])
        os.system('subfixer %s' % f_uri)
