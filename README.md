# snakemake-wrappers
Snakemake wrappers for bioinformatics.

## Available wrappers

### Routine analysis

- DEG discovery
  - DESeq2
  - EBSeq
  - edgeR

### Variant calling

- freebayes

### File format handlers

- sambamba
  - index
  - sort
  - markdup
- samtools
  - index
  - sort

### Data retrieval

- sra-tools
  - prefetch
    - accession
- parallel-fastq-dump

### Preprocessing

- fastqc
- trim-galore
- fastp

### Aligner

- bismark
  - genome-preparation
- bsmap

### Gene expression quantification

- rsem
  - calculate-expression
    - pe
  - prepare-reference
- kallisto
  - index
  - quant
- salmon
  - index
  - quant

### Misc

- subsample-fastq
