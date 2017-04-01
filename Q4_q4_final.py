import matplotlib.pyplot as plt
import pysam

#myFastq = open("chrall.fa")

dict={}
with open("my_genome.fa", 'r') as f:
    for line in f:
        if line !='\n': #skips empty lines and
            line = line.strip()
        if line.startswith(">"):
            seqname = line[1:]
            if seqname  not in dict:
                dict[seqname] = []
            continue
        sequence = line
        dict[seqname].append(sequence)

	bamfile = pysam.AlignmentFile("output_sorted.bam", "rb")

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


