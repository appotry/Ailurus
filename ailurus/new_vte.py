#coding:utf8

import os, sys, gtk, thread

class Textbox(gtk.VBox):
    def use_monospace_font(self, textview):
        import pango
        font = pango.FontDescription('Monospace')
        textview.modify_font(font)
    def uneditable(self, textview):
        textview.set_cursor_visible(False)
        textview.set_editable(False)
    def get_scroll(self):
        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        return scroll
    def scroll_to_end(self):
        pos = self.textbuffer.get_insert()
        self.textview.scroll_to_mark(pos, 0)
    def __init__(self):
        self.textbuffer = gtk.TextBuffer()
        self.textview = gtk.TextView(self.textbuffer)
        self.use_monospace_font(self.textview)
        self.uneditable(self.textview)
        scroll = self.get_scroll()
        scroll.add(self.textview)
        gtk.VBox.__init__(self, False, 0)
        self.pack_start(scroll)
    def write(self, string):
        enditer = self.textbuffer.get_end_iter()
        self.textbuffer.insert(enditer, string)
        self.scroll_to_end()
        self.do_gtk_pending_events()
    def clear(self):
        startiter = self.textbuffer.get_start_iter()
        enditer = self.textbuffer.get_end_iter()
        self.textbuffer.delete(startiter, enditer)
        self.do_gtk_pending_events()
    def do_gtk_pending_events(self):
        while gtk.events_pending():
            gtk.main_iteration(False)

class Terminal(gtk.VBox):
    def __init__(self):
        self.current_task = None
        gtk.VBox.__init__(self, False, 0)
        self.textbox = Textbox()
        self.pack_start(self.textbox)
    def run(self, commandline, env=None, cwd=None):
        import subprocess
        import select
        task = subprocess.Popen(commandline,
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE, stderr = subprocess.PIPE,
                                shell = True, cwd = cwd, env = env)
        self.current_task = task
        # display output while the task is running
        while self.current_task.poll() == None:
            read_ready = select.select([task.stdout, task.stderr], [], [])[0]
            for f in read_ready:
                line = f.readline() # do not use read(1), utf-8 issue.
                self.textbox.write(line)
        # display remaining output text
        string = task.stdout.read()
        self.textbox.write(string)
        string = task.stderr.read()
        self.textbox.write(string)
        # return
        return task.returncode
        
import unittest
class TestTextbox:#(unittest.TestCase):
    def setUp(self):
        textbox = Textbox()
        dialog = gtk.Dialog(buttons = (gtk.STOCK_OK, gtk.RESPONSE_OK))
        dialog.set_default_size(400, 300)
        dialog.vbox.pack_start(textbox)
        dialog.vbox.show_all()
        self.textbox = textbox
        self.dialog = dialog
    
    def tearDown(self):
        self.dialog.run()
        self.dialog.destroy()
    
    def testClear(self):
        for i in range(3):
            self.textbox.write('abcde\n')
            self.textbox.clear()
            self.textbox.write('abcde\n')

    def testMonospaceFont(self):
        self.textbox.write('1234567890w\n')
        self.textbox.write('w1234567890\n')
        
    def testUnicodeFont(self):
        self.textbox.write('1234567890\n')
        self.textbox.write('中文中文中\n')
    
    def testScrollToBottom(self):
        for i in range(1000):
            self.textbox.write(str(i))
            self.textbox.write('\n')
        
class TestTerminal(unittest.TestCase):
    def setUp(self):
        terminal = Terminal()
        window = gtk.Window()
        window.set_position(gtk.WIN_POS_CENTER)
        window.add(terminal)
        window.set_default_size(400, 300)
        window.show_all()
        window.connect('delete-event', gtk.main_quit)
        self.terminal = terminal
        self.window = window
        while gtk.events_pending(): gtk.main_iteration(False)
    
    def tearDown(self):
        gtk.main()

    def testRunFail(self):
        ret = self.terminal.run("false")
        self.assertEqual(ret, 1)
        
    def testRunSimple(self):
        ret = self.terminal.run("ls -l")
        self.assertEqual(ret, 0)

    def testRunSimple2(self):
        ret = self.terminal.run("date")
        self.assertEqual(ret, 0)

    def testRunOutputNoNewline(self):
        # "a.py" does not output newline
        with open('/tmp/a.py', 'w') as f:
            f.write('import sys\n'
                    'sys.stdout.write("a")')
        ret = self.terminal.run("python /tmp/a.py")
        self.assertEqual(ret, 0)

    def testRunALongProcess(self):
        # "a.py" outputs a line every second. lasts 10 seconds.
        with open('/tmp/a.py', 'w') as f:
            f.write('for i in range(10):\n'
                    '    print i\n'
                    '    import time\n'
                    '    time.sleep(1)')
        ret = self.terminal.run("python -u /tmp/a.py")
        self.assertEqual(ret, 0)

if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestTerminal('testRunALongProcess'))
    unittest.TextTestRunner(verbosity=2).run(suite)
