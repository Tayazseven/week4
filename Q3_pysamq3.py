import pysam
from collections import Counter
import matplotlib.pyplot as plt

##Reading the bam file with pysam
bamfile = pysam.AlignmentFile("output_sorted.bam", "rb")
mapqua=pysam.AlignmentFile("mapqua.bam", "wb", template=bamfile)

mappingquality=[]
strands=[]

#Getting the map qualities
for read in bamfile.fetch():
     #if read.mapping_quality: to write the mapping quaility to another bam file
          #mapqua.write(read)
    mapquality = read.mapping_quality
    strand = read.is_reverse ##pysam function getting the reverse reads
    mappingquality.append(mapquality)
    strands.append(strand)

for pileupcolumn in bamfile.pileup():
    print ("\ncoverage at base %s = %s" %
                 (pileupcolumn.pos, pileupcolumn.n))
    for pileupread in pileupcolumn.pileups:
        if not pileupread.is_del and not pileupread.is_refskip:
                    # query position is None if is_del or is_refskip is set.
            print ('\tbase in read %s = %s' %
                pileupread.alignment.query_name,
                pileupread.alignment.query_sequence[pileupread.query_position])

    bamfile.close()

plt.hist(mappingquality)

plus_strand= 0.0
for strand in strands:
	if strand == False: plus_strand += 1
fract = plus_strand/len(strands)
print "%f of the reads are on the + strand"%(fract)

mapqua.close()
bamfile.close()
