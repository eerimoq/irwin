from .. import timeseries


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


def _do_plot(args):
    x, y = load_samples(args.path)

    timeseries.run_curses(args.path,
                          x,
                          y,
                          None,
                          'none',
                          None,
                          None,
                          None,
                          None,
                          1,
                          0,
                          10800,
                          1,
                          x[-1] - x[0])


def add_subparser(parser):
    parser = parser.add_parser(
        'plot',
        description='Plot samples from file.')

    parser.add_argument('path',
                        help='File with data to plot.')
    parser.set_defaults(func=_do_plot)
