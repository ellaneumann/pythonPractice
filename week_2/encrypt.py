
the_file = open('trial.txt','r+')
while True:
    line = the_file.readline()
    for x in line:
        data = x.replace(x, chr(ord(x) - 2))
        the_file.write(data)
        print(x)
    if not line:
        break
        
the_file.close()
