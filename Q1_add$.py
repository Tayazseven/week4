fi = open("my_genome.fa","r")
fo = open("out.fa","w")
while True:
    line = fi.readline()
    if len(line) ==0:
        break
    sline = fi.readline()
    newsline = sline + '$'
    fo.write(newsline)

fi.close()
fo.close()