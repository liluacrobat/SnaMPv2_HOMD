# HOMD 14.5

## Download
Download from [FTP](ftp://www.homd.org/16S_rRNA_refseq/HOMD_16S_rRNA_RefSeq/), since `p9.fasta` is corresponding to `aligned.fasta`, we need to download the following files.

* HOMD 16S rRNA RefSeq Version 14.5 (Starts from position 9): `HOMD_16S_rRNA_RefSeq_V14.5.p9.fasta`
* HOMD 16S rRNA RefSeq Version 14.5 Taxonomy File for QIIME: `HOMD_16S_rRNA_RefSeq_V14.5.qiime.taxonomy`
* HOMD 16S rRNA RefSeq Version 14.5 Aligned FASTA File: `HOMD_16S_rRNA_RefSeq_V14.5.aligned.fasta`

## Basic info

* __889__ reference sequences
* For download files, the order is not matched
* Parsed file would be order matched and use index(start from 1) as sequence header
* Taxonomy file:
	* HOMD label separator: only `;`  
	* Parsed(GG) label separator: `;` followed by a __space__
	* The parsed format is compatible with GG, but taxonomy label may not be identical.


## Parse
```
$ python parse.py -h
usage: parse.py [-h] -a ALIGNED_FP -u UNALIGNED_FP -t TAXA_FP [-d TARGET_DIR]

Parse HOMD database to greengene format

optional arguments:
  -h, --help            show this help message and exit
  -a ALIGNED_FP, --aligned_fp ALIGNED_FP
                        aligned fasta file
  -u UNALIGNED_FP, --unaligned_fp UNALIGNED_FP
                        unaligned fasta file
  -t TAXA_FP, --taxa_fp TAXA_FP
                        taxaonomy file
  -d TARGET_DIR, --target_dir TARGET_DIR

python parse.py -a download/HOMD_16S_rRNA_RefSeq_V14.5.aligned.fasta -u download/HOMD_16S_rRNA_RefSeq_V14.5.p9.fasta -t download/HOMD_16S_rRNA_RefSeq_V14.5.qiime.taxonomy -d .
```
