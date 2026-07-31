file = open("f1.txt")
print(file.read()) # Reads entire file
file.seek(0)           # Reset cursor to the beginning
print("First 5 char",file.read(5))
# Reset cursor to the beginning
file.seek(0)
# read file line by line
line=file.readline()
while line!="":
    print(line)
    line=file.readline()

file.seek(0)
# read lines in string array and print
print("Read all lines in a file at once and store in var, then print each line")
lines=file.readlines()
for x in lines:
    print(x)
file.close()
