from .. import timeseries


def _do_watch(args):
    interval = 1

    timeseries.run_curses(args.command,
                          [],
                          [],
                          timeseries.OsCommandProducer(args.command, interval),
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


def add_subparser(parser):
    parser = parser.add_parser(
        'watch',
        description='Run a command periodically and plot its output.')

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
    parser.add_argument('command',
                        help='Command to execute.')
    parser.set_defaults(func=_do_watch)
