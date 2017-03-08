# Snakemake Microbiome Pipeline

## Download pipeline
```bash
git clone https://github.com/vitmy0000/SnaMP.git
```

## Create environment

```bash
# cd Projects
conda create -c bioconda -m -p pyenvs/py35-snakemake python=3.5 pandas snakemake
```

## Load environment

```bash
# cd Projects
module load python/anaconda2-4.2.0
source activate pyenvs/py35-snakemake
```

## Remove environment 

```
source deactivate
```

## Workflow

  * Closed reference OTU picking 
  * BLAST agaist HOMD database

![workflow_0](./misc/dag.pdf)

### Usage

1. Prepare sequencing data

  Repalce the `$SOURCE_FILES` with the __zipped__ sequencing result, e.g. `WHI_Repo/RT530_Batch2/*.gz`

  ```bash
  cd input
  ln -s $SOURCE_FILES .
  cd ..
  ```

2. Launch jobs

  The pipeline will utilize CCR resource to parallel execution.
  OTU table and statisics about merge rate, filter rate, hit rate wiil be placed under _table_

  ```bash
  snakemake -p -j 100 --cluster-config cluster.json --cluster "sbatch --partition {cluster.partition} --time {cluster.time} --nodes {cluster.nodes} --ntasks-per-node {cluster.ntasks-per-node}"
  ```
  
## Clean

  To remove generated files:
  ```
  snakemake clean
  ```

## Known Issues

* empty sequence file
* cluster time limit
