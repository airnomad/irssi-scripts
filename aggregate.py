import irssi
import os

settings='/home/tomic/.irssi/aggregate-mute'

def print_to_aggregate(dest, text, stripped):
    win = irssi.window_find_item('aggregate')

    if not dest.server or \
       not dest.target or \
       not dest.server.ischannel(dest.target):
        return

    msg = '%s %s' %(dest.target, text)

    if is_valid_msg ( msg ):
        win.prnt(dest.target + ' ' + text, irssi.MSGLEVEL_CLIENTCRAP)


def command_agregate(command, server, channel):
    if not command:
        print "/aggregate mute add regexp"
        print "/aggregate mute list"
        return

    commands = command.split(" ")

    if commands[0] == 'mute':
        if ( commands[ 1 ] == 'list' ):
            for rule in get_mute_rules():
                print rule

        elif commands [ 1 ] == 'add':
            add_mute_rule ( commands[ 2 ] )


def add_mute_rule( rule ):
    with open(settings, 'a+') as f:
        f.write( rule + '\n')

    mutes = get_mute_rules()

def get_mute_rules():
    if os.path.exists( settings ) :
        with open ( settings, 'r+' ) as f:
            return f.read().splitlines()

    return []


def is_valid_msg( msg ):
    import re
    for mute in mutes:
        if re.search(r'%s' %(mute), msg, re.IGNORECASE):
            return False
    return True

mutes = get_mute_rules()

irssi.command_bind('aggregate', command_agregate)
irssi.signal_add('print text', print_to_aggregate)

