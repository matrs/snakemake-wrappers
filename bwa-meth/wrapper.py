__author__ = "Dohoon Lee"
__copyright__ = "Copyright 2018, Dohoon Lee"
__email__ = "dohlee.bioinfo@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

# Extract log.
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Define exception classes.
class RuleInputException(Exception):
    pass

# Extract parameters.
extra = snakemake.params.get('extra', '')

# Extract required inputs.
reads = snakemake.input.reads
mates = snakemake.input.get('mates', '')
if isinstance(reads, str):
    reads = [reads]
if isinstance(mates, str):
    mates = [mates]
if len(reads) < 1:
    raise RuleInputException('You should give at least one reads and mates. Given: %d' % len(reads))
if len(reads) != len(mates):
    raise RuleInputException('The number of reads and their pairs should match. Given: %d reads, %d mates' % (len(reads), len(mates)))

reads, mates = ','.join(reads), ','.join(mates)

reference = snakemake.input.reference

# Extract required outputs.
output = snakemake.output[0]

pipe_command = ''
# bwa-mem output defaults to sam. Convert sam to bam with samtools.
# TODO: Use sambamba with appropriate number of threads.
if output.endswith('.bam'):
    pipe_command = '| samtools view -Sb -'

# Execute shell command.
shell(
    "("
    "bwameth.py "
    "{extra} "
    "-t {snakemake.threads} "
    "--reference {reference} "
    "{reads} "
    "{mates} "
    "{pipe_command} > "
    "{output}) "
    "{log}"
)
