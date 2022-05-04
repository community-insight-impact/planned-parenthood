""" 
1.txt requirements:



"""
import re
import string
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('stopwords')
# necessary installs:
# pip install --user -U nltk
# pip install pyspellchecker  
# and the regex library


def main():
    f = open("1.txt", "r")
    content = f.read()
    # -------------- getting rid of the increasing numbers in the text ---------------------
    content_arr = content.split()
    indexer=[]
    for ind in range(len(content_arr)):
        curWord = content_arr[ind]
        if(curWord.isdigit()):
            curInt = int(curWord)
            indexer.append([curInt,ind])
    collector = []
    for i in range(len(indexer)):
        curNum = indexer[i]
        seqNum = curNum[0]
        buffer = []
        if seqNum == -1:
            continue
        for j in range(i,len(indexer)):
            nextNum = indexer[j][0]
            if nextNum == seqNum + 1:
                buffer.append([nextNum,indexer[j][1]])
                indexer[j][0] = -1
                seqNum = nextNum
        curNum[0] = -1
        collector.append(buffer)
    # get rid of the empty arrays
    for x in collector:
        if not x:
            collector.remove(x)
    for seq in collector:
        for ind in seq:
            curIndex = ind[1]
            content_arr[curIndex] = -1

    res = [i for i in content_arr if i != -1]

    mystr = ""
    for ele in res:
        mystr += ele + " "
    # -------------- getting rid of the increasing numbers in the text ends here ---------------------


    # ----------- spellchecker - optional -----------
    spelling = SpellChecker()
    def spelling_checks(text):
        correct_result = []
        typo_words = spelling.unknown(text.split())
        for word in text.split():
            if word in typo_words:
                correct_result.append(spelling.correction(word))
            else:
                correct_result.append(word)
        return " ".join(correct_result)

    mystr = spelling_checks(mystr)
    # -------------- end of spellchecker --------------


    # set up which punctuations to remove -------------
    # punctuations = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"       # these are all the punctuations
    punctuations = "#$%&*+,-./:;<=>?@[\]^_`{|}~"            # I excluded the () and "" from this one 


    mystr = mystr.lower()                                   # turn everything lowercase
    # removing page numbers
    mystr = re.sub("page \d+. \d+", "", mystr)
    
    # removing punctuations
    mystr = mystr.translate(str.maketrans('', '', punctuations))


    stopwordslist = stopwords.words('english')
    stop_words = set(stopwords.words('english')) 
    tokenwords = word_tokenize(mystr) 
    result = [w for w in tokenwords if not w in stop_words] 
    result = [] 
    for w in tokenwords: 
        if w not in stop_words: 
            result.append(w) 

    mystr = ""
    for ele in result:
        mystr += ele + " "

    mystr = re.sub(' +', ' ', mystr)
    mystr = re.sub(" +", " ", mystr)
    mystr = re.sub("`` ", "", mystr)
    mystr = re.sub(" ``", "", mystr)
    # mystr = re.sub("[(] \d+ [)]", "\d+", mystr)
    mystr = re.sub("page \d+", "", mystr)
    mystr = re.sub("\( \d+ \)", "", mystr)
    mystr = re.sub(r"\s+", " ", mystr)

    print(mystr)
    
    nf = open("new.txt", "w+")
    nf.write(mystr)

    




main()