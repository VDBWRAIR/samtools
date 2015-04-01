
The pysam pysam/pysam project may be a good model. In fact we could re-use code like: 

    https://github.com/pysam-developers/pysam/blob/d67f1b5f62c32e69e381711d7a0f0f9947fdf61f/pysam/Pileup.py

    It may even be worth looking into replacing some fuctionality with PySam. The problem with that seems to be that we lose control over our samtools version.


    We want to be able to treat .sam and .bam files the same, but handle the cases where a lack of index causes problems

    # Needs to handle pipes as well?

# bamutils
def

@requires_index

class BamFile():

    def __init__(self, bam):


    #index & sort can wrap bam.indexbam...

   def get_contents(self):
       if self._type == file:
           return open(self.file_name, 'r').read()
       else:
           return self._contents

   def index(self):
       pass

   def sort(self):
       pass

   def get_view_iter(self, include_header=False):
       if self._type == BAM:
           in_stream = 
           #TODO: samtools view 
       else:
           # no need to convert samfile
           # skip the header?
           return (line for line in self.get_file() if not (line.starswith('@') or header))

       pass

   def get_pileup(self):
       pass

   def get_stats() #pileup stats
   def get_as_fastq()
   def to_sam()
   def to_bam()


