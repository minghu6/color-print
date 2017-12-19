# -*- coding:utf-8 -*-

import os
import sys

color_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'color')
print(os.path.dirname(color_path))
sys.path.append(os.path.dirname(color_path))

from color import color

if __name__ == '__main__':
    print('isLinux %r' % color.islinux())
    print('isWindows %r' % color.iswin())

    color.print_dark_red('dark red')
    color.print_red('red')
    color.print_dark_green('dark green')
    color.print_green('green')
    color.print_dark_skyblue('dark skyblue')
    color.print_skyblue('skyblue')
    color.print_dark_yellow('dark yellow')
    color.print_yellow('yellow')
    color.print_dark_pink('dark pink')
    color.print_pink('pink')
    color.print_dark_blue('dark blue')
    color.print_blue('blue')
    color.print_white('White Char')
    color.print_dark_gray('dark gray')

    # color.print_info('info')
    # color.print_ok('ok means that exec action succeed')
    # color.print_warning('warning')
    # color.print_warning('print_warning is too long')
    # color.print_error('error')
    # color.print_err('print_error is too long')
    
    with color.redirect_color('red'):
        print('redirect red')

    with color.redirect_color('yellow'):
        print('redirect yellow')

    with color.redirect_color('gray'):
        print('redirect gray', end='')
    
    with color.redirect_color('gray'):
        print('', end='\n')

    try:
        1 / 0
    except Exception as ex:
        import logging

        with color.redirect_color('red', sys.stderr):
            logging.error(ex)

    print('end1')
    print('end2')
    print('end3')
