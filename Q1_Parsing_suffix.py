import itertools
def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

fout = open("parsed_suffix_out.fa", "w")

with open('out.fa', 'r') as fp:
    for name, seq in read_fasta(fp):
        for word in itertools.permutations(seq):
            fout.write(name + '\n' + seq +'\n')

fout.close()
