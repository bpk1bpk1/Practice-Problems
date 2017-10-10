s = "opg"
operation = ['0 0 L','2 2 L','0 2 R']

for i in operation:
    string = list(s)
    f = i.split(' ')
    length = int(f[1]) - int(f[0])
    if(length == 0):
        if(f[2] == 'L'):
            string[int(f[1])] = chr(ord(string[int(f[1])]) - 3)
        if (f[2] == 'R'):
            string[int(f[1])] = chr(ord(string[int(f[1])]) + 3)
    else:
        for i in range(0,length + 1):
            if (f[2] == 'L'):
                string[i] = chr(ord(string[i]) - 3)
            if (f[2] == 'R'):
                string[i] = chr(ord(string[i]) + 3)

    print(string)





