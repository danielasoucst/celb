

def createArffFile(nameFile,vetFeatures,vetLabels,attLength,classes):

    file = open(nameFile+".arff", 'w')
    file.write("@RELATION estilo\n")

    for k in range(0,attLength):
        file.write("@ATTRIBUTE 'att"+str(k)+"' real\n")
    file.write("@ATTRIBUTE 'class' "+classes+" \n")
    file.write("@DATA\n")
    for i in range(0,len(vetFeatures)):
        for j in range(0,len(vetFeatures[i])):
            file.write(str(vetFeatures[i][j])+", ")
        file.write(str(vetLabels[i]) + "\n")
    file.close()

'''def read_csv_file(nameFile):
    file = open(nameFile,'r')
    line = file.readline()
    lstIdFrames = []
    while(line!=None):
        line = file.readline()
        if(len(line)<5 ):
            break
        line = line.split(',')
        #print(line, len(line))
        if(line[2]=='2:1' and line[3]==''):
            lstIdFrames.append(int(line[0]))

    return lstIdFrames'''

def  createArffFile2(nameFile,vetFeatures,vetLabels,classes):
    file = open(nameFile+".arff", 'w')
    file.write("@RELATION escolas\n")


    file.write("@ATTRIBUTE 'Document' string\n")
    file.write("@ATTRIBUTE 'class' "+classes+" \n")
    file.write("@DATA\n")

    for i in range(0,len(vetFeatures)):
        file.write('"')
        file.write(str(vetFeatures[i])+'", ')
        file.write(str(vetLabels[i]) + "\n")
    file.close()



