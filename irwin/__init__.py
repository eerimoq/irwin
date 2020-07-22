import sys
import argparse
import logging

from .canvas import Canvas
from .version import __version__


def do_main(args):
    pass


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
