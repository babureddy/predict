with open('Train.csv') as f:
    lines = f.readlines()
    firstLine=True
    for line in lines:
        if firstLine :
            firstLine = False
            continue
        fields = line.split(",")
        skills = fields[2].replace('"','').split(',')
        newline=''
        for skill in skills:
            newline = fields[0] + ',' + fields[1] + ',' + fields[2] #+ ',' + fields[3] + ',' + fields[4] + ',' + fields[5] + ',"' + skill + '",' + fields[6]
            print newline
            break
        #break

#for line in lines:
#    print line[7]
