import itertools as it
import io 
import numpy as np
import argparse
Data = np.ndarray


def main() -> None:
    '''This function is called when the script is explicitly executed'''
    # Parse Arguments given by the user
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputfile",    help="Input *.dat filename")
    parser.add_argument("-o", "--outputfile",   help="Output filename")
    args = parser.parse_args()
    if run(
            inputfile  = args.inputfile,
            outputfile = args.outputfile,
            ):
        parser.print_help()
    

def run(
        inputfile: str,
        outputfile:str,
        ):
    if not inputfile:
        return 1
    if not outputfile:
        outputfile = f'{inputfile}.acr.dat'
        print(f'No outputfile specified. Using {outputfile}.') 
    data = read(inputfile)
    data = correct_angle(data)
    write(data, outputfile)


def read(
        filename: str,
        encoding: str = 'utf8',
        ):
    with open(filename, 'r') as file:
        lines = file.read()
    lines = lines.strip().split('\n')
    lines = it.dropwhile(lambda line: not '[Data]' in line, lines)
    next(lines)                 # [Data]
    columns = next(lines)       # columns header
    columns = columns.split(',')
    indexes, names = list(zip(*[
            (idx, name)
            for idx, name in enumerate(columns)
            if name in [
                'Temperature (K)', 
                'Magnetic Field (Oe)', 
                'Rotation Angle (deg)', 
                'DC Moment Fixed Ctr (emu)',
                'DC Moment Err Fixed Ctr (emu)',
                'DC Moment Free Ctr (emu)',
                'DC Moment Err Free Ctr (emu)',
                ] 
            ]))
    data = np.genfromtxt(
        io.StringIO('\n'.join(lines)), 
        comments = '#', 
        delimiter = ',', 
        deletechars = '',
        replace_space = ' ',
        #names = columns,
        names = names,
        usecols = indexes,
        encoding = encoding,
        )
    return data

def correct_angle(data: Data) -> Data:
    return data



def write(
        data: np.ndarray,
        outputfile: str,
        ):
    np.savetxt(outputfile, data,
            delimiter = ',',
            header = 'ACR Output file\n'+', '.join(data.dtype.names),
            )

if __name__=='__main__':
    main()
