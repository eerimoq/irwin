import sys
import argparse
import logging

from .canvas import Canvas
from .version import __version__
from . import timeseries


def plot(x, y, width=80, height=40):
    """Plot given x-y values, connected with lines.

    """
    
    return ''


def create_title(path, command):
    title = []

    if path is not None:
        title.append(path)

    if command is not None:
        title.append(command)

    return '; '.join(title)


def load_samples(path):
    timestamps = []
    values = []

    if path is not None:
        with open(path, 'r') as fin:
            for sample in fin.read().split():
                timestamp, value = sample.split(',')
                timestamps.append(float(timestamp))
                values.append(float(value))

    return timestamps, values


def create_producer(command, interval):
    if command is None:
        return None

    return timeseries.OsCommandProducer(command, interval)


def do_main(args):
    timestamps, values = load_samples(args.path)
    interval = 1

    timeseries.run_curses(create_title(args.path, args.command),
                          timestamps,
                          values,
                          create_producer(args.command, interval),
                          args.algorithm,
                          args.y_min,
                          args.y_max,
                          args.y_min,
                          args.y_max,
                          args.scale,
                          args.offset,
                          10800,
                          interval,
                          60)


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
    parser.add_argument('path',
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
