import pandas as pd
import argparse
import os.path

parser = argparse.ArgumentParser(description='Parse a BLAST result to a single columns dataframe.')
parser.add_argument('-i', '--input_fp', help='blast result file', required=True)
parser.add_argument('-o', '--output_fp', help='output file', required=True)
args = parser.parse_args()


if __name__ == '__main__':
    res_dict = {}
    marker = 0
    with open(args.input_fp) as f:
        for line in f:
            if line.startswith('# BLAST'):
                marker = 0
            else:
                marker += 1

            if marker == 5:
                content = line.strip().split('\t')
                query_id, cnt = content[0].split('-')
                target_id = content[1]
                identity = float(content[7])
                coverage = float(content[8])

                if target_id in res_dict:
                    res_dict[target_id] += int(cnt)
                else:
                    res_dict[target_id] = int(cnt)

    columns = [os.path.splitext(os.path.basename(args.input_fp))[0]]
    if len(res_dict) == 0:
        res_df = pd.DataFrame(columns=columns)
    else:
        res_df = pd.DataFrame.from_dict(res_dict, orient='index')
        res_df.columns = columns
    res_df.to_csv(args.output_fp, sep='\t')

