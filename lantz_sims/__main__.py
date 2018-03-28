

def main(args=None):
    """Run simulators.
    """
    import argparse
    import logging

    from .instrument import SIMULATORS

    parser = argparse.ArgumentParser(description='Run Lantz simulators.')
    parser.add_argument('simulator', choices=list(SIMULATORS.keys()))
    args, pending = parser.parse_known_args(args)
    print('Dispatching ' + args.simulator)

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%Y-%d-%m %H:%M:%S')

    SIMULATORS[args.simulator](pending)


if __name__ == '__main__':
    main()
