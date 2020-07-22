import sys
import argparse
import logging

from .canvas import Canvas
from .version import __version__
from . import timeseries


def do_main(args):
    if args.file:
        command = None
        path = args.cmdorfile
    else:
        command = args.cmdorfile
        path = None

    timeseries.run_curses(command,
                          path,
                          args.algorithm,
                          args.y_min,
                          args.y_max,
                          args.scale,
                          args.offset)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-l', '--log-level',
                        default='error',
                        choices=[
                            'debug', 'info', 'warning', 'error', 'critical'
                        ],
                        help='Set the logging level (default: %(default)s).')
    parser.add_argument('--version',
                        action='version',
                        version=__version__,
                        help='Print version information and exit.')
    parser.add_argument('-a', '--algorithm',
                        default='none',
                        choices=('none', 'delta'),
                        help='Algorithm (default: %(default)s).')
    parser.add_argument('--y-min',
                        type=float,
                        help='Y minimum.')
    parser.add_argument('--y-max',
                        type=float,
                        help='Y maximum.')
    parser.add_argument('--scale',
                        type=float,
                        default=1,
                        help='Value scale (default: %(default)s).')
    parser.add_argument('--offset',
                        type=float,
                        default=0,
                        help='Value offset (default: %(default)s).')
    parser.add_argument('-f', '--file',
                        action='store_true',
                        help='Read data from a file.')
    parser.add_argument('cmdorfile', help='Command or file.')

    args = parser.parse_args()

    level = logging.getLevelName(args.log_level.upper())
    logging.basicConfig(level=level, format='%(asctime)s %(message)s')

    if args.debug:
        do_main(args)
    else:
        try:
            do_main(args)
        except BaseException as e:
            sys.exit(f'error: {e}')
