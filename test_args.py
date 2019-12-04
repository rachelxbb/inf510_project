import argparse


def main(args):
    print(f'In main with name: {__name__}')
    print(f'These are the arguments as passed in: {args}')
    print("If you called this from the command, those arguments are from argparse")
    print("If you called this from a module, they're from sys.argv")
    print("Now here is where I'd actually do something...")


if __name__ == '__main__':
    print(f"We're in file {__file__}")
    parser = argparse.ArgumentParser(description='Test driver for argparse')
    parser.add_argument("required_arg",
                        type=str,
                        help='This is a required argument')
    parser.add_argument('-r',
                        '--req',
                        type=str,
                        required=True,
                        help='Required Keyworded argument')
    parser.add_argument('-o',
                        '--optional',
                        type=str,
                        default='Hi',
                        help='OPTIONAL: You do not need to incldue this [default = hi')
    parser.add_argument('-e',
                        '--extra',
                        type=str,
                        help='This is also optional, with no default value')
    args = parser.parse_args()

    print("Calling test_args.py -> main() ")
    main(args)
