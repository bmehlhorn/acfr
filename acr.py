import itertools as it
import io 
import numpy as np

def main() -> None:
    '''This function is called when the script is explicitly executed'''
    # Parse Arguments given by the user
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputfile",    help="Input *.dat filename")
    parser.add_argument("-o", "--outputfile",   help="Output filename")
    args = parser.parse_args()
    run(
            outputfile = args.outputfile,
            inputfile  = args.outputfile,
            )

def run(
        inputfile: str,
        outputfile:str,
        ):
    data = read(inputfile)
    data = correct_angle(data)
    write(data)


def read(
        filename: str,
        encoding: str = 'utf8',
        ):
    with open(filename, 'r') as file:
        lines = file.read()
    lines = lines.strip().split('\n')
    lines = it.dropwhile(lambda line: not '[Data]' in line, datlines)
    next(lines)                 # [Data]
    columns = next(lines)       # columns header
    columns = columns.split(',')
    indexes, names = list(zip(*[
            (idx, name)
            for idx, name in enumerate(columns)
            if name in ['Rotation Angle (deg)', 'DC Moment Free Ctr (emu)'] 
            ]))
    data = np.genfromtxt(
        io.StringIO('\n'.join(lines)), 
        comments = '#', 
        delimiter = ',', 
        deletechars = '',
        replace_space = ' ',
        names = names,
        usecols = indexes,
        encoding = encoding,
        )
    return data
data = correct_angle(data)
write(data)
