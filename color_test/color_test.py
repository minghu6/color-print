# -*- coding:utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import

import os
import sys

color_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'color')
print(os.path.dirname(color_path))
sys.path.append(os.path.dirname(color_path))

import color

if __name__ == '__main__':
    import logging
    import logging.handlers
    import io

    color.print_dark_red('dark red')
    color.print_red('red')
    color.print_dark_green('dark green')
    color.print_green('green')
    color.print_dark_skyblue('dark skyblue')
    color.print_skyblue('skyblue')
    color.print_yellow('yellow')
    color.print_purple('purple')
    color.print_blue('blue')
    color.print_white('White Char')
    color.print_dark_gray('dark gray')

    color.print_normal('normal for normal words')
    color.print_italic('italic for comment and other like italic font usage')
    color.print_bold('bold use like bold font')
    color.print_ok('ok means that exec action succeed')
    color.print_warning('warning')
    color.print_warning('print_warning is too long')
    color.print_error('error')
    color.print_err('print_error is too long')
    
    with color.redirect_red():
        print('redirect red')

    with color.redirect_yellow():
        print('redirect yellow')

    with color.redirect_gray():
        print('redirect gray', end='')

    with color.redirect_gray():
        print('', end='\n')

    try:
        1 / 0
    except Exception as ex:
        import logging

        with color.redirect_red(sys.stderr):
            logging.error(ex)

    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)-15s [%(levelname)s] %(process)-8d %(message)s')

    if sys.version_info.major == 2:
        buffer = io.BytesIO()
    else:
        buffer = io.StringIO()
    sh = logging.StreamHandler(stream=buffer)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    logger.info('stream logger redirect yellow')
    color.print_yellow(buffer.getvalue())

    print('end1')
    print('end2')
    print('end3')
