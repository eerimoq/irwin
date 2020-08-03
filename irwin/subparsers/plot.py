from .. import plot


def load_samples(path):
    x = []
    y = []

    with open(path, 'r') as fin:
        for sample in fin.read().split():
            xv, yv = sample.split(',')
            x.append(float(xv))
            y.append(float(yv))

    return x, y


def _do_plot(args):
    x, y = load_samples(args.path)

    plot.run_curses(args.path,
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

    parser.add_argument('-t', '--type',
                        choices=('line', 'scatter'),
                        default='line',
                        help='Plot type (default: %(default)s).')
    parser.add_argument('path',
                        help='File with data to plot.')
    parser.set_defaults(func=_do_plot)
