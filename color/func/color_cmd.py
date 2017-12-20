# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""
################################################################################
Only for Windows CMD 、PowerShell

Can be compatibale with python2(>2.6)(Care: UniocoedEncodeError)
################################################################################
"""
from __future__ import print_function

import ctypes
import sys


STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12


# Windows CMD text colors
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_DARKBLUE = 0x01  # dark blue.
FOREGROUND_DARKGREEN = 0x02  # dark green.
FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
FOREGROUND_DARKRED = 0x04  # dark red.
FOREGROUND_DARKPINK = 0x05  # dark pink.
FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
FOREGROUND_DARKWHITE = 0x07  # dark white.
FOREGROUND_DARKGRAY = 0x08  # dark gray.
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_SKYBLUE = 0x0b  # skyblue.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_PINK = 0x0d  # pink.
FOREGROUND_YELLOW = 0x0e  # yellow.
FOREGROUND_WHITE = 0x0f  # white.

# Windows CMD background colors
BACKGROUND_DARKBLUE = 0x10  # dark blue.
BACKGROUND_DARKGREEN = 0x20  # dark green.
BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
BACKGROUND_DARKRED = 0x40  # dark red.
BACKGROUND_DARKPINK = 0x50  # dark pink.
BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
BACKGROUND_DARKWHITE = 0x70  # dark white.
BACKGROUND_DARKGRAY = 0x80  # dark gray.
BACKGROUND_BLUE = 0x90  # blue.
BACKGROUND_GREEN = 0xa0  # green.
BACKGROUND_SKYBLUE = 0xb0  # skyblue.
BACKGROUND_RED = 0xc0  # red.
BACKGROUND_PINK = 0xd0  # pink.
BACKGROUND_YELLOW = 0xe0  # yellow.
BACKGROUND_WHITE = 0xf0  # white.


# flag of start color print
def can_start_colorprint():
    if sys.stdout.isatty():  # should be shell or cmd
        return True
    else:
        return False


# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = True
    if can_start_colorprint():
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def reset_color():
    if can_start_colorprint():
        set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


###############################################################

class PrintColor:
    """
    __exit__:self, exc_type, exc_value, traceback
    """

    def __exit__(self, *args, **kwargs):
        reset_color()


# dark blue
class PrintDarkBlue(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKBLUE)


# dark green
class PrintDarkGreen(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKGREEN)


# dark sky blue
class PrintDarkSkyBlue(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKSKYBLUE)


# dark red
class PrintDarkRed(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKRED)


# dark pink
class PrintDarkPink(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKPINK)


# dark yellow
class PrintDarkYellow(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKYELLOW)


# dark white
class PrintDarkWhite(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKWHITE)


# dark gray
class PrintDarkGray(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_DARKGRAY)


# blue
class PrintBlue(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_BLUE)


# green
class PrintGreen(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_GREEN)


# sky blue
class PrintSkyBlue(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_SKYBLUE)


# red
class PrintRed(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_RED)


# pink
class PrintPink(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_PINK)


# yellow
class PrintYellow(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_YELLOW)


# white
class PrintWhite(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_WHITE)


##################################################

# white bkground and black text
class PrintWhiteBlack(PrintColor):
    def __enter__(self):
        set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)


# white bkground and black text
class PrintWhiteBlack_2(PrintColor):
    def __enter__(self):
        set_cmd_text_color(0xf0)


# white bkground and black text
class PrintYellowRed(PrintColor):
    def __enter__(self):
        set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)


# write origin text
class PrintBlank(PrintColor):
    def __enter__(self):
        pass


################################################################################
# Application layer encapsulation
#
# with print_color('xxx'):
#       print(xxx)
################################################################################
print_map = {'darkblue': PrintDarkBlue,
             'darkgreen': PrintDarkGreen,
             'darkskyblue': PrintDarkSkyBlue,
             'darkred': PrintDarkRed,
             'darkpink': PrintDarkPink,
             'darkyellow': PrintDarkYellow,
             'darkwhite': PrintDarkWhite,
             'darkgray': PrintDarkGray,

             'blue': PrintBlue,
             'green': PrintGreen,
             'skyblue': PrintSkyBlue,
             'red': PrintRed,
             'pink': PrintPink,
             'purple': PrintDarkPink,
             'yellow': PrintYellow,
             'white': PrintWhite,
             'gray': PrintDarkGray,
             'blank': PrintBlank}


def print_color(color='darkwhite'):
    """

    Args:
        color: default darkwhite/printDarkWhite

    Returns: an printColor instance

    """
    return print_map.get(color, PrintDarkWhite)()


if __name__ == '__main__':
    with print_color('darkblue'):
        print(u'printDarkBlue: dark blue\n')

    with print_color('darkgreen'):
        print(u'printDarkGreen: dark green\n')

    with print_color('darkred'):
        print(u'printDarkRed: dark red\n')

    with print_color('darkpink'):
        print(u'printDarkPink: dark pink\n')

    with print_color('darkyellow'):
        print(u'printDarkYellow: dark yellow\n')

    with print_color('darkwhite'):
        print(u'printDarkWhite: dark white\n')

    with print_color('darkgray'):
        print(u'printDarkGray: dark gray\n')

    with print_color('blue'):
        print(u'printBlue: blue\n')

    with print_color('green'):
        print(u'printGreen: green\n')

    with print_color('skyblue'):
        print(u'printSkyBlue: skyblue\n')

    with print_color('red'):
        print(u'printRed: red\n')

    with print_color('pink'):
        print(u'printPink: pink\n')

    with print_color('yellow'):
        print(u'printYellow: yellow\n')

    with print_color('white'):
        print(u'printWhite: white\n')

    with print_color('blank'):
        print(u'printBlank: origin')
    with PrintWhiteBlack():
        print(u'printWhiteBlack: white background and black character\n')

    with PrintWhiteBlack_2():
        print(u'printWhiteBlack_2: white background and black character（pass hex args）\n')

    with PrintYellowRed():
        print(u'printYellowRed: yellow background and red character\n')

