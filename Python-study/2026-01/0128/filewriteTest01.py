outfile = open("output.txt", "w")  # open

for i in range(1, 11):
    outfile.write(str(i) + "\n")  # use

outfile.close()  # close

infile = open("output.txt", "r")  # open

line = infile.readline()
while line != "":
    print(line)  # use
    line = infile.readline()

infile.close()  # close
