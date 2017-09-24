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

__all__ = ['color_dict',
           'print_map',
           'print_info',
           'print_warn', 'print_warning',
           'print_err', 'print_error']


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


def print_color(*objs, **kwargs):
    _end = kwargs.get('end', '\n')
    _sep = kwargs.get('sep', ' ')
    _color = kwargs.get('color', 'blank')
    kwargs = _remove_key(kwargs, ['end', 'sep', 'color'])

    if iswin():
        with cmd.print_color(color=_color):
            [print(obj, end=_sep, sep='', **kwargs) for obj in objs]
            print(end=_end, **kwargs)

    elif islinux():
        [print(sh.UseStyle(obj, fore=_color), end=_sep, sep='', **kwargs)
         for obj in objs]

        print(end=_end, **kwargs)

    else:
        [print(obj, end=_sep, sep='', **kwargs) for obj in objs]
        print(end=_end)


def print_white(*objs, **kwargs):
    print_color(*objs, color='white', **kwargs)


def print_dark_pink(*objs, **kwargs):
    print_color(*objs, color='darkpink', **kwargs)


def print_blue(*objs, **kwargs):
    """
    Belive it ,It's an ugly print-color.
    Blue makes you blue :(
    :param obj:
    :return:
    """
    print_color(*objs, color='blue', **kwargs)


def print_dark_red(*objs, **kwargs):
    print_color(*objs, color='darkred', **kwargs)


def print_dark_skyblue(*objs, **kwargs):
    print_color(*objs, color='darkskyblue', **kwargs)


def print_dark_green(*objs, **kwargs):
    print_color(*objs, color='darkgreen', **kwargs)


def print_dark_yellow(*objs, **kwargs):
    print_color(*objs, color='darkyellow', **kwargs)


def print_blank(*objs, **kwargs):
    print_color(*objs, color='blank', **kwargs)


################################################################################
# Application layer encapsulation
#
# 4 Kind of Print:
#
# print Common Information         : print_info
# print Succeed Information        : print_ok
# print Warinng Information        : print_warn or print_warning
# print Error Information          : print_err or print_error
#
# You can also configure them with color_dict and print_map
################################################################################
color_dict = {'green': print_dark_green,
              'darkskyblue': print_dark_skyblue,
              'yellow': print_dark_yellow,
              'red': print_dark_red,
              'blue': print_blue,
              'white': print_white,
              'purple': print_dark_pink}

print_map = {'info': color_dict['darkskyblue'],
             'ok': color_dict['green'],
             'warning': color_dict['yellow'],
             'error': color_dict['red']}


def print_info(*objs, **kwargs): print_map['info'](*objs, **kwargs)


def print_ok(*objs, **kwargs): print_map['ok'](*objs, **kwargs)


def print_warning(*objs, **kwargs): print_map['warning'](*objs, **kwargs)


def print_warn(*objs, **kwargs): print_warning(*objs,
                                               **kwargs)  # print_warning is too long


def print_error(*objs, **kwargs):
    if 'file' not in kwargs:
        kwargs['file'] = sys.stderr
    print_map['error'](*objs, **kwargs)


def print_err(*objs, **kwargs): print_error(*objs,
                                            **kwargs)  # print_error is too long


if __name__ == '__main__':
    print('isLinux?%r' % islinux())
    print('isWindows?%r' % iswin())

    print_dark_red({'a': 1, 'b': 2}, {'c': 3}, end='')
    print_dark_green([1, 2, 3], 4, sep='*', end='\n')
    print_dark_skyblue((1, 2, 3))
    print_dark_yellow({1, 2, 3})

    print_dark_pink('abc' + 'def')
    print_blue(print_blue)
    print_white('White Char')

    print_info('info')
    print_ok('ok means that exec action succeed')
    print_warning('warning')
    print_warning('print_warning is too long')
    print_error('error')
    print_err('print_error is too long')
