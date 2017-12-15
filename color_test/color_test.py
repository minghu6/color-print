# -*- coding:utf-8 -*-

import os
import sys

color_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'color')
print(os.path.dirname(color_path))
sys.path.append(os.path.dirname(color_path))

import color

if __name__ == '__main__':
    # print('isLinux?%r' % color.islinux())
    # print('isWindows?%r' % color.iswin())

    color.print_dark_red({'a': 1, 'b': 2}, {'c': 3}, end='')
    color.print_dark_green([1, 2, 3], 4, sep='*', end='\n')
    color.print_dark_skyblue((1, 2, 3))
    color.print_dark_yellow({1, 2, 3})

    color.print_dark_pink('abc' + 'def')
    color.print_blue(print_blue)
    color.print_white('White Char')

    color.print_info('info')
    color.print_ok('ok means that exec action succeed')
    color.print_warning('warning')
    color.print_warning('print_warning is too long')
    color.print_error('error')
    color.print_err('print_error is too long')
