#!/usr/bin/env python3


import argparse
from pathlib import Path


def main(directory = Path('.')):
    print(f'Passed Directory: `{directory}`')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description = 'Converts all images in folder to PDF'
        )
        
        parser.add_argument(
            '--directory', '--dir', '-d',
            help    = 'Directory Path',
            default = Path('.')
        )
        
        args = parser.parse_args()
        
        main(directory = args.directory)

    except KeyboardInterrupt:
        print('Terminated...')

    except Exception as e:
        print(e)