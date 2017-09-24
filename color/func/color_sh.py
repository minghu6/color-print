# /usr/bin/python
# -*- coding: utf-8 -*-

"""
################################################################################
Support for sh、bash (include cmd in win10) etc
Do not Support powershell

Can be compatibale with python2(>2.6)(Care: UniocoedEncodeError)
################################################################################
"""

from __future__ import print_function

#   format：\033[show;frontground;backgroundm
#   state:
#
#   frontground       background        color
#   ------------------------------------------
#     30                40              black
#     31                41              red
#     32                42              green
#     33                43              yellow
#     34                44              blue
#     35                45              purple
#     36                46              cyan
#     37                47              white
#
#     show           meaning
#   -------------------------
#      0           default terminal
#      1             high light
#      4            using underline
#      5              glint
#      7             inverse
#      8             invisiable
#
#   exp：
#   \033[1;31;40m    <!--1-high light 31-front backgroud red  40-background black-->
#   \033[0m          <!--unset color set (terminal default)-->]]]


STYLE = {
    'fore':
        {   # frontground
            'black': 30,

            'red': 31,
            'darkred': 31,

            'green': 32,
            'darkgreen': 32,

            'yellow': 33,
            'darkyellow': 33,

            'blue': 34,
            'darkblue': 34,

            'purple': 35,
            'darkpink': 35,

            'cyan': 36,
            'darkskyblue': 36,

            'white': 37,
            'blank': 0,
        },

    'back':
        {   # background
            'black': 40,
            'red': 41,
            'green': 42,
            'yellow': 43,
            'blue': 44,
            'purple': 45,
            'cyan': 46,
            'white': 47,
        },

    'mode':
        {   # show mode
            'mormal': 0,  # default terminal
            'bold': 1,  # highlight
            'underline': 4,  # use underline
            'blink': 5,  # glint
            'invert': 7,  # inverse
            'hide': 8,  # invisiable
        },

    'default':
        {
            'end': 0,
        },
}

# flag of start color print
import sys


def can_start_colorprint():
    """

    :return:bool
    """
    if sys.stdout.isatty():  # should be shell or cmd
        return True
    else:
        return False


def UseStyle(obj, fore='', mode='', back=''):
    mode = '%s' % STYLE['mode'][mode] if mode in STYLE['mode'] else ''

    fore = '%s' % STYLE['fore'][fore] if fore in STYLE['fore'] else ''

    back = '%s' % STYLE['back'][back] if back in STYLE['back'] else ''

    style = ';'.join([s for s in [mode, fore, back] if s])

    style = '\033[%sm' % style if style else ''

    end = '\033[%sm' % STYLE['default']['end'] if style else ''

    if can_start_colorprint():
        retobj = '%s%s%s' % (style, str(obj), end)
    else:
        retobj = obj

    return retobj


def test_color():
    print((UseStyle('normal show')))
    print('')

    print("test show normal")
    print((UseStyle('high-light', mode='bold')), end=' ')
    print((UseStyle('underline', mode='underline')), end=' ')
    print((UseStyle('glint', mode='blink')), end=' ')
    print((UseStyle('inverse', mode='invert')), end=' ')
    print((UseStyle('invisiable', mode='hide')), end=' ')
    print('')

    print("test frontground")
    print(UseStyle('black', fore='black'), end=' ')
    print(UseStyle('red', fore='red'), end=' ')
    print(UseStyle('green', fore='green'), end=' ')
    print(UseStyle('yellow', fore='yellow'), end=' ')
    print(UseStyle('blue', fore='blue'), end=' ')
    print(UseStyle('purple', fore='purple'), end=' ')
    print(UseStyle('cyan', fore='cyan'), end=' ')
    print(UseStyle('white', fore='white'))
    print(UseStyle('origin', fore='blank'))
    print('')

    print("test background")
    print(UseStyle('black', back='black'), end=' ')
    print(UseStyle('red', back='red'), end=' ')
    print(UseStyle('green', back='green'), end=' ')
    print(UseStyle('yellow', back='yellow'), end=' ')
    print(UseStyle('blue', back='blue'), end=' ')
    print(UseStyle('purple', back='purple'), end=' ')
    print(UseStyle('cyan', back='cyan'), end=' ')
    print(UseStyle('white', back='white'))
    print('')


if __name__ == '__main__':
    test_color()
    print(UseStyle([1, 2, 3], fore='green'))
