import argparse
import sys

parser = argparse.ArgumentParser(description="Strip forward and reverse primer")
parser.add_argument('-f', '--forward_primer', help='forward primer', required=True)
parser.add_argument('-r', '--reverse_primer', help='reverse primer', required=True)
parser.add_argument('-i', '--input_fp', help='input file path', required=True)
parser.add_argument('-o', '--output_fp', help='output file path', required=True)
args = parser.parse_args()

def strip_primer(in_fp, out_fp, head_len, tail_len):
    read = ''
    with open(in_fp) as fi, open(out_fp, 'w') as fo:
        for line in fi:
            if line.startswith('>'):
                if read != '':
                    fo.write('%s\n' % read[head_len:-tail_len])
                fo.write('%s\n' % line.strip())
                read = ''
            else:
                read += line.strip()
        fo.write('%s\n' % read[head_len:-tail_len])

if __name__ == '__main__':
    strip_primer(args.input_fp, args.output_fp,
            len(args.forward_primer), len(args.reverse_primer))
