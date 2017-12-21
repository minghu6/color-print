# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""
################################################################################
Establish a Unified Color print across all kinds of os

However, you should care about that
         we only implemented 8^1=8 kind of basic color in color_sh
################################################################################
"""

from __future__ import print_function
from __future__ import absolute_import

import sys
import platform
import io
from contextlib import contextmanager


__all__ = ['color_map',
           'print_italic',
           'print_bold',
           'print_normal',
           'print_warn', 'print_warning',
           'print_err', 'print_error',
           'print_dark_red',
           'print_red',
           'print_dark_green',
           'print_green',
           'print_dark_skyblue',
           'print_skyblue',
           'print_yellow',
           'print_purple',
           'print_blue',
           'print_gray',
           'redirect_darkred',
           'redirect_red',
           'redirect_darkgreen',
           'redirect_green',
           'redirect_darkskyblue',
           'redirect_skyblue',
           'redirect_yellow',
           'redirect_purple',
           'redirect_blue',
           'redirect_gray']


def iswin():
    return platform.platform().upper().startswith('WIN')


def islinux():
    return platform.platform().upper().startswith('LINUX')


if islinux():
    from color.func import color_sh as sh
elif iswin():
    from color.func import color_cmd as cmd


def _remove_key(dic, keys):
    return {_key: dic[_key] for _key in dic if _key not in set(keys)}


@contextmanager
def _redirect_color(color, stream=sys.stdout):
    origin_stdout, origin_stderr = sys.stdout, sys.stderr
    if sys.version_info.major == 2:
        buffer = io.BytesIO()
    else:
        buffer = io.StringIO()
    
    try:
        if stream == sys.stdout:
            sys.stdout = buffer
        elif stream == sys.stderr:
            sys.stderr = buffer
        yield None
    finally:
        content = buffer.getvalue()
        
        if stream == origin_stdout:
            sys.stdout = stream
        elif stream == origin_stderr:
            sys.stderr = stream

        if content and content[-1] == '\n':
            content = content[:-1]
            end = '\n'
        else:
            end = ''

        _print_color(content, color=color, end=end)


def redirect_red(*args, **kwargs):
    return _redirect_color('red', *args, **kwargs)


def redirect_darkred(*args, **kwargs):
    return _redirect_color('darkred', *args, **kwargs)


def redirect_green(*args, **kwargs):
    return _redirect_color('green', *args, **kwargs)


def redirect_darkgreen(*args, **kwargs):
    return _redirect_color('darkgreen', *args, **kwargs)


def redirect_darkskyblue(*args, **kwargs):
    return _redirect_color('darkskyblue', *args, **kwargs)


def redirect_skyblue(*args, **kwargs):
    return _redirect_color('skyblue', *args, **kwargs)


def redirect_yellow(*args, **kwargs):
    return _redirect_color('yellow', *args, **kwargs)


def redirect_blue(*args, **kwargs):
    return _redirect_color('blue', *args, **kwargs)


def redirect_gray(*args, **kwargs):
    return _redirect_color('gray', *args, **kwargs)


def redirect_purple(*args, **kwargs):
    return _redirect_color('purple', *args, **kwargs)


def _print_color(*objs, **kwargs):
    _end = kwargs.get('end', '\n')
    _sep = kwargs.get('sep', ' ')
    _color = kwargs.get('color', 'blank')
    kwargs = _remove_key(kwargs, ['end', 'sep', 'color'])

    if iswin():
        with cmd.print_color(color=_color):
            [print(obj, end=_sep, sep='', **kwargs) for obj in objs]
            print(end=_end, **kwargs)

    elif islinux():
        [print(sh.use_style(obj, fore=_color), end=_sep, sep='', **kwargs)
         for obj in objs]

        print(end=_end, **kwargs)

    else:
        [print(obj, end=_sep, sep='', **kwargs) for obj in objs]
        print(end=_end)


def print_white(*objs, **kwargs):
    _print_color(*objs, color='white', **kwargs)


def print_dark_gray(*objs, **kwargs):
    _print_color(*objs, color='darkgray', **kwargs)


def print_gray(*objs, **kwargs):
    _print_color(*objs, color='gray', **kwargs)


def print_dark_pink(*objs, **kwargs):
    _print_color(*objs, color='darkpink', **kwargs)


def print_purple(*objs, **kwargs):
    _print_color(*objs, color='purple', **kwargs)


def print_blue(*objs, **kwargs):
    _print_color(*objs, color='blue', **kwargs)


def print_dark_red(*objs, **kwargs):
    _print_color(*objs, color='darkred', **kwargs)


def print_red(*objs, **kwargs):
    _print_color(*objs, color='red', **kwargs)


def print_dark_skyblue(*objs, **kwargs):
    _print_color(*objs, color='darkskyblue', **kwargs)


def print_skyblue(*objs, **kwargs):
    _print_color(*objs, color='skyblue', **kwargs)


def print_dark_green(*objs, **kwargs):
    _print_color(*objs, color='darkgreen', **kwargs)


def print_green(*objs, **kwargs):
    _print_color(*objs, color='green', **kwargs)


def print_yellow(*objs, **kwargs):
    _print_color(*objs, color='yellow', **kwargs)


def print_blank(*objs, **kwargs):
    _print_color(*objs, color='blank', **kwargs)


################################################################################
# Application layer encapsulation
#
# 6 Kind of Print:
# default color theme:
#   print_italic   gray
#   print_bold     skyblue
#   print_normal   white
#   print_ok       darkgreen
#   print_warn     yellow
#   print_err      red
# You can also configure them with color_dict and print_map
################################################################################
DARKRED = 'darkred'
RED = 'red'
DARKGREEN = 'darkgreen'
GREEN = 'green'
DARKSKYBLUE = 'darkskyblue'
SKYBLUE = 'skyblue'
YELLOW = 'yellow'
PURPLE = 'purple'
BLUE = 'blue'
GRAY = 'gray'
WHITE = 'white'


color_map = {'italic': GRAY,
             'bold': PURPLE,
             'normal': WHITE,
             'ok': DARKGREEN,
             'warning': YELLOW,
             'error': RED}


def print_italic(*objs, **kwargs): _print_color(color=color_map['italic'], *objs, **kwargs)


def print_bold(*objs, **kwargs): _print_color(color=color_map['bold'], *objs, **kwargs)


def print_normal(*objs, **kwargs): _print_color(color=color_map['normal'], *objs, **kwargs)


def print_ok(*objs, **kwargs):  _print_color(color=color_map['ok'], *objs, **kwargs)


def print_warning(*objs, **kwargs):  _print_color(color=color_map['warning'], *objs, **kwargs)


def print_warn(*objs, **kwargs):  _print_color(color=color_map['warning'], *objs, **kwargs)


def print_error(*objs, **kwargs):
    if 'file' not in kwargs:
        kwargs['file'] = sys.stderr
    _print_color(color=color_map['error'], *objs, **kwargs)


def print_err(*objs, **kwargs):  _print_color(color=color_map['error'], *objs, **kwargs)  # print_error is too long
