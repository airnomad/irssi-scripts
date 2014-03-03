import irssi
import re


def command_go(command, server, channel):

    if len ( command ) == 0:
        return

    for win in irssi.windows():
        if win.get_active_name():
            name = re.sub(r'[^a-zA-Z0-9]+', '', win.get_active_name())
            if len ( name ) > 0:
                if re.search(r'^%s' %(command), name, re.IGNORECASE ):
                    win.set_active()
                    return True

    return None

irssi.command_bind('g', command_go)

