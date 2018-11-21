

def main(args=None):
    """Run simulators.
    """
    import argparse
    import logging

    from .instrument import SIMULATORS

    parser = argparse.ArgumentParser(description='Run Lantz simulators.',
                                     add_help=False)

    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('simulator',
                        choices=list(SIMULATORS.keys()),
                        nargs='?')
    args, pending = parser.parse_known_args(args)

    if args.simulator is None:
        if args.help:
            parser.print_help()
        else:
            parser.print_usage()
    else:
        if args.help:
            pending += ['--help', ]

        print('Dispatching ' + args.simulator)

        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(message)s',
                            datefmt='%Y-%d-%m %H:%M:%S')

        SIMULATORS[args.simulator](pending)


if __name__ == '__main__':
    main()
