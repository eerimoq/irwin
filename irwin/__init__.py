import sys
import argparse
import logging

from .canvas import Canvas
from .version import __version__
from . import timeseries


def do_main(args):
    timeseries.run_curses(args.file,
                          args.command,
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
    parser.add_argument('-y', '--y-min',
                        type=float,
                        help='Minimum value on the y-axis.')
    parser.add_argument('-Y', '--y-max',
                        type=float,
                        help='Maximum value on the y-axis.')
    parser.add_argument('-s', '--scale',
                        type=float,
                        default=1,
                        help='Value scale (default: %(default)s).')
    parser.add_argument('-o', '--offset',
                        type=float,
                        default=0,
                        help='Value offset (default: %(default)s).')
    parser.add_argument('-c', '--command',
                        help='Command to run periodically.')
    parser.add_argument('file',
                        nargs='?',
                        help='File with data to plot.')

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
