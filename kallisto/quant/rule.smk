rule kallisto_quant:
    input:
        # Required input.
        index = 'reference/Homo_sapiens.GRCh38.transcriptome.kallisto_idx',
        fastq = ['data/{sample}.read1.fastq.gz', 'data/{sample}.read2.fastq.gz']
    output:
        # Required output.
        'result/{sample}/abundance.tsv',
        'result/{sample}/abundance.h5',
        'result/{sample}/run_info.json'
    params:
        # Required parameters for single-end reads.
        fragment_length = 75.0,
        standard_deviation = 10.0,
        # Optional parameters. It omitted, default value will be used.
        extra = '',
    threads: 8
    log: 'logs/kallisto_quant/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/kallisto/quant'
