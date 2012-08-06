#coding: utf-8
#
# Ailurus is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ailurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ailurus; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

def gray_bg(widget):
    import gtk
    if not isinstance(widget, gtk.Entry) and not isinstance(widget, gtk.TextView): raise TypeError
    
    def event(widget, e):
        if widget.base_color_changed==False:
            color = widget.style.bg[gtk.STATE_NORMAL]
            widget.modify_base(gtk.STATE_NORMAL, color)
            widget.base_color_changed = True
    widget.base_color_changed = False
    widget.connect('expose-event', event)
    widget.connect('map-event', event)
    
def image_stock_button(stock, text):
    import gtk
    box = gtk.HBox(False, 3)
    box.pack_start(gtk.image_new_from_stock(stock, gtk.ICON_SIZE_BUTTON), False, False)
    l = gtk.Label()
    l.set_text_with_mnemonic(text)
    box.pack_start(l, False, False)
    button = gtk.Button()
    button.add(box)
    return button

def stock_image_only_button(stock):
    import gtk
    image = gtk.image_new_from_stock(stock, gtk.ICON_SIZE_BUTTON)
    button = gtk.Button()
    button.add(image)
    return button

def exception_happened(etype, value, tb):
    if etype == KeyboardInterrupt: return

    import traceback, StringIO, platform, gtk
    
    msg = StringIO.StringIO()
    traceback.print_tb(tb, file=msg)
    print >>msg, etype, ':', value
    print >>msg, platform.dist()

    textview_traceback = gtk.TextView()
    gray_bg(textview_traceback)
    textview_traceback.set_wrap_mode(gtk.WRAP_WORD)
    textview_traceback.get_buffer().set_text(msg.getvalue())
    textview_traceback.set_cursor_visible(False)

    scroll_traceback = gtk.ScrolledWindow()
    scroll_traceback.set_shadow_type(gtk.SHADOW_IN)
    scroll_traceback.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    scroll_traceback.add(textview_traceback)
    scroll_traceback.set_size_request(-1, 300)
    
    vbox = gtk.VBox(False, 5)
    vbox.pack_start(scroll_traceback)

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title('Error')
    window.set_border_width(10)
    window.add(vbox)
    window.show_all()
