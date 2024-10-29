#!/usr/bin/env python3


import argparse
from pathlib import Path
from PIL import Image

from const import IMAGE_EXTENSIONS


def main(input_directory: Path, output_directory: Path) -> None:
    if not input_directory:
        raise Exception('Specify input directory')
    
    if not output_directory.is_dir():
        output_directory.mkdir(parents = True, exist_ok = True)
    
    files = [
        image
        for extension in IMAGE_EXTENSIONS
        for image     in input_directory.glob(f'*.{extension}')
    ]
    
    for file in files:
        with Image.open(file) as image:
            image.save( output_directory / f'{file.stem}.pdf' )
            


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description = 'Converts all images in folder to PDF'
        )
        
        parser.add_argument(
            '--input', '-i', '-d',
            help    = 'Input Directory',
            default = None
        )
        
        parser.add_argument(
            '--output', '-o',
            help    = 'Output Directory',
            default = Path('output/')
        )
        
        args = parser.parse_args()
        
        main(
            input_directory  = Path(args.input),
            output_directory = Path(args.output)
        )

    except KeyboardInterrupt:
        print('Terminated...')

    except Exception as e:
        print(e)