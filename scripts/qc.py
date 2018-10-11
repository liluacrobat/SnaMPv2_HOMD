import argparse
import os.path
import numpy as np
import pandas as pd
from collections import OrderedDict


parser = argparse.ArgumentParser(description="Make QC table based by counting")
parser.add_argument('-r', '--raw_files', nargs='+', help='raw fastq files', required=True)
parser.add_argument('-j', '--joined_files', nargs='+', help='joined fastq files', required=True)
parser.add_argument('-f', '--filtered_files', nargs='+', help='filted fastq files', required=True)
parser.add_argument('-b', '--blast_files', nargs='+', help='parsed BLAST result files', required=True)
parser.add_argument('-o', '--output_fp', help='output file path', required=True)
args = parser.parse_args()

def count_fq(fp):
    cnt = 0
    with open(fp) as f:
        for line in f:
            cnt += 1 
    cnt = cnt/4
    return cnt

if __name__ == "__main__":
    sample_ids = pd.Series([os.path.splitext(os.path.basename(x))[0] for x in args.blast_files])
    raw_cnts = pd.Series([count_fq(x) for x in args.raw_files])
    joined_cnts = pd.Series([count_fq(x) for x in args.joined_files])
    joined_rate = pd.Series(["{:.2f}".format(x) for x in np.array(joined_cnts).astype(float)/np.array(raw_cnts) * 100])
    filtered_cnts = pd.Series([count_fq(x) for x in args.filtered_files])
    filtered_rate = pd.Series(["{:.2f}".format(x) for x in np.array(filtered_cnts).astype(float)/np.array(joined_cnts) * 100])
    blast_cnts = pd.Series([pd.read_csv(x, sep='\t', index_col=0).iloc[:, 0].sum() for x in args.blast_files])
    blast_rate = pd.Series(["{:.2f}".format(x) for x in np.array(blast_cnts).astype(float)/np.array(filtered_cnts) * 100])

    df = pd.DataFrame(OrderedDict((
        ("#SampleID", sample_ids),
        ("Raw_count", raw_cnts),
        ("Joined_count", joined_cnts),
        ("Pass_count", filtered_cnts),
        ("Hit_count", blast_cnts),
        ("Merge_rate(%)", joined_rate),
        ("Pass_rate(%)", filtered_rate),
        ("Hit_rate(%)", blast_rate))))

    df.to_csv(args.output_fp, sep='\t', index=False)

