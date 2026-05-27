counter = [0] * 26

infile = open("mobydick.txt", "r")
ch = infile.read(1)

while ch != "":
    ch = ch.upper()  # 대문자로 바꿈
    if "A" <= ch <= "Z":
        i = ord(ch) - ord("A")
        counter[i] += 1
    
ch = infile.read(1)

infile.close()
print(counter)
