import argparse

from functions import print_payments


def main() -> None:
    parser = argparse.ArgumentParser(
        prog        = 'Relay Payments',
        description = 'Prints the trips and their total compensation'
    )

    parser.add_argument(
        '-f', '--file',
        type = str,
        help = 'Excel file to Process'
    )

    parser.add_argument(
        '-t', '--type',
        type    = str,
        choices = ['contract', 'spot'],
        help    = 'Type of the Excel report'
    )

    args, unknown = parser.parse_known_args()

    if args.file:
        file = args.file
    elif unknown:
        file, _ = unknown
    else:
        parser.error('Please, specify a file')

    print_payments(file, args.type.title())
    # print(f'File: {file}')
    # print(f'Type: {args.type.title()}')



if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was Terminated...')
