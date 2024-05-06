#!/usr/bin/env python3


import argparse
from pathlib import Path

from const import IMAGE_EXTENSIONS


def main(directory: Path = '.'):
    images = [
        image
        for extension in IMAGE_EXTENSIONS
        for image     in directory.glob(f'*.{extension}')
    ]
    
    print(images)


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
        
        main(directory = Path(args.directory))

    except KeyboardInterrupt:
        print('Terminated...')

    except Exception as e:
        print(e)