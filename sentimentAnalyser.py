projectDataFile = open("files/project_twitter_data.csv","r")
resultingDataFile = open("files/resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words=[]

positiveFile = open("files/positive_words.txt")
for line in positiveFile:
	 if line[0]!= ';' and line[0]!='\n':
	 	positive_words.append(line.strip())
        
def get_pos(strSentences):
    strSentences = remove_punctuation(strSentences)
    listStr = strSentences.split()
    count = 0
    for word in listStr:
        for positive in positive_words:
            if word == positive: count += 1
    return count

negative_words=[]

negativeFile = open("files/negative_words.txt")
for line in negativeFile:
    if line[0]!= ';' and line[0]!='\n':
        negative_words.append(line.strip())

def get_neg(strSentences):
    strSentences = remove_punctuation(strSentences)
    listStr = strSentences.split()
    count = 0
    for word in listStr:
        for negative in negative_words:
            if word == negative: count += 1
    return count

def remove_punctuation(str):
    for charPunc in punctuation_chars:
        str.replace(charPunc, " ")
    return str

def writeInFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    lines = projectDataFile.readlines()
    #removing headers
    lines.pop(0)
    for line in lines:
        words = line.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(words[1], words[2], get_pos(words[0]), get_neg(words[0]), (get_pos(words[0])-get_neg(words[0]))))
        resultingDataFile.write("\n")

writeInFile(resultingDataFile)
projectDataFile.close()
resultingDataFile.close()