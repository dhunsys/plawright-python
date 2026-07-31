#with will open and close so no need to call close
with open("f1.txt","r") as file:# give any name with as
    content = file.readlines()
    with open("t.txt","w") as file1:
        for line in content:
            file1.write(line)