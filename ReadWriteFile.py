FilePath = r'C:\Users\dhql\Documents\0_Study\Python\UsefulScripts\111.txt'

file = open(FilePath, "w")
file.write('hello world in the new file\n')
file.write("and another line\n")
#lines_of_text = ["a line of text", "another line of text", "a third line"]
#fh.writelines(lines_of_text)
file.close()

file = open(FilePath, "a")
for i in range(1, 100):
	file.write((str(i) + ', ')*10 + '\n')
file.close()

file = open(FilePath, "r")
#print file.read()
#print file.read(100) #read first 100 characters
#print file.readlines()[4]
#print file.readlines()
#print len(file.readlines())
#print file.readline()
#for line in file:
#	print line
file.close()

with open("newfile.txt") as f:
    for line in f:
        print line
