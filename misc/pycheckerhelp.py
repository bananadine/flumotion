# lots of little imports done before anything else so that
# we don't get weird stray module errors

from flumotion.common import boot

boot.init_gobject()
boot.init_gst()

import gst
import gst.interfaces
e = gst.element_factory_make('fakesrc')

from twisted.internet import gtk3reactor
gtk3reactor.install(useGtk=True)

import pyexpat

# fake out pychecker
import gobject
import gtk
import gtk.glade
loop = gobject.MainLoop()
gtk.main_iteration()

m = pyexpat
