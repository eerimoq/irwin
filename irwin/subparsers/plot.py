from .. import plot


def create_title(path, command):
    title = []

    if path is not None:
        title.append(path)

    if command is not None:
        title.append(command)

    return '; '.join(title)


def load_samples(path):
    x = []
    y = []

    with open(path, 'r') as fin:
        for sample in fin.read().split():
            xv, yv = sample.split(',')
            x.append(float(xv))
            y.append(float(yv))

    return x, y



def create_producer(command, interval):
    if command is None:
        return None
    
    return plot.OsCommandProducer(command, interval)


def _do_plot(args):
    x, y = load_samples(args.path)
    interval = 1
    
    plot.run_curses(args.type,
                    create_title(args.path, args.command),
                    x,
                    y,
                    create_producer(args.command, interval),
                    'none',
                    None,
                    None,
                    None,
                    None,
                    1,
                    0,
                    10800,
                    interval,
                    x[-1] - x[0])


def add_subparser(parser):
    parser = parser.add_parser(
        'plot',
        description='Plot samples from file.')

    parser.add_argument('-t', '--type',
                        choices=('line', 'scatter'),
                        default='line',
                        help='Plot type (default: %(default)s).')
    parser.add_argument('-c', '--command',
                        help='Command to execute periodically.')
    parser.add_argument('path',
                        help='File with data to plot.')
    parser.set_defaults(func=_do_plot)
