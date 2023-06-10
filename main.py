# -*- coding: utf-8 -*-
import operator

def extract(allwords):
    extracted=[]
    stopwords= ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
        'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
        'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
        'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
        'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
        'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
        'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
        'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
        'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
        'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
        'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
        'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
        'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
        'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
        'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
        'consequently', 'consider', 'considering', 'contain', 'containing',
        'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
        'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
        'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
        'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
        'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
        'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
        'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
        'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
        'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
        'following', 'follows', 'for', 'forever', 'former', 'formerly',
        'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
        'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
        'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
        'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
        'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
        'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
        'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
        'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
        'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
        'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
        'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
        'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
        'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
        'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
        'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
        'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
        'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
        'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
        'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
        'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
        'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
        'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
        'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
        'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
        'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
        'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
        'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
        'overall', 'own', 'particular', 'particularly', 'past', 'per',
        'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
        'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
        'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
        'regardless', 'regards', 'relatively', 'respectively', 'right',
        'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
        'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
        'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
        'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
        'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
        'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
        'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
        'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
        'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
        'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
        'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
        'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
        'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
        'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
        'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
        'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
        'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
        'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
        'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
        'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
        'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
        'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
        'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
        'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
        'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
        'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
        'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
        'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
        'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
        'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
        'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
        'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
        'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
        'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
        'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
        'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
        'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
        'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
        'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
        'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
        'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
        'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
        'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
        'importance', 'important', 'index', 'information', 'invention', 'itd',
        'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
        'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
        'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
        'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
        'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
        'readily', 'ref', 'refs', 'related', 'research', 'resulted',
        'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
        'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
        'similar', 'similarly', 'slightly', 'somethan', 'specifically',
        'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
        'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
        'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
        'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
        'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
        'world', 'youd', 'youre']

    for word in allwords:
        for stopword in stopwords:
            if stopword==word:
                word=word.replace(stopword,'')

        extracted.append(word)

    return extracted

def clean(allwords):
    notsembols=[]
    sembols="!'^+%&/()=?_<é>“|£—_#$½{[]}\-1234567”89*,.üşçğö:;~¨"
    for word in allwords:
        for sembol in sembols:
            if sembol in word:
                word = word.replace(sembol,'')
        if len(word)>0:
            notsembols.append(word)

    return notsembols

def order(allwords):
    counter = {}
    for word in allwords:
        if word in counter:
            counter[word] += 1
        else:
           counter[word] = 1
    return counter

def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):
    file = open(Book, 'r', encoding='utf-8')
    read = file.read()
    file.close()
    newallwords = []
    allwords = []
    all=[]
    wordslist = read.lower().split()


    for words in wordslist:
        allwords.append(words)

    allwords = clean(allwords)
    allwords = extract(allwords)

    for word in allwords:
        if word != '':
            all.append(word)


    for i in range(0, len(all) - 2):
        newallwords.append(all[i] + all[i + 1])


    words = []
    numbers = []
    if Word_Order==2:
        counter = order(newallwords)

    elif Word_Order==1:
        counter = order(all)

    else:
        print("error")

    for word, number in sorted(counter.items(), key=operator.itemgetter(1)):
        words.append(word)
        numbers.append(number)

    output = open(File_Output, 'w', encoding='utf-8')
    for i in range(len(counter)-1, 0, -1):
       output.write(words[i] + "  " +  str(numbers[i]) + '\n' )

    output.close()

def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):
    file1 = open(Book_1, 'r', encoding='utf-8')
    file2 = open(Book_2, 'r', encoding='utf-8')
    read1 = file1.read()
    read2 = file2.read()
    file1.close()
    file2.close()
    newallwords1 = []
    newallwords2 = []
    allwords1 = []
    allwords2 = []
    all1 = []
    all2=[]
    wordslist1 = read1.lower().split()
    wordslist2 = read2.lower().split()

    for words in wordslist1:
        allwords1.append(words)

    for words in wordslist2:
        allwords2.append(words)

    allwords1 = clean(allwords1)
    allwords1 = extract(allwords1)

    allwords2 = clean(allwords2)
    allwords2 = extract(allwords2)

    for word in allwords1:
        if word != '':
            all1.append(word)

    for word in allwords2:
        if word != '':
            all2.append(word)

    for i in range(0, len(all1) - 2):
        newallwords1.append(all1[i] + all1[i + 1])

    for i in range(0, len(all2) - 2):
        newallwords2.append(all2[i] + all2[i + 1])

    words1 = []
    numbers1 = []

    words2= []
    numbers2 = []

    if Word_Order==2:
        counter1 = order(newallwords1)
        counter2=order(newallwords2)
    elif Word_Order==1:
        counter1 = order(all1)
        counter2=order(all2)
    else:
        print("error")

    for word, number in sorted(counter1.items(), key=operator.itemgetter(1)):
        words1.append(word)
        numbers1.append(number)

    for word, number in sorted(counter2.items(), key=operator.itemgetter(1)):
        words2.append(word)
        numbers2.append(number)
    total=[]
    yazmac=[]
    output = open(File_Output, 'w', encoding='utf-8')
    for i in range(len(counter1)-1, 0, -1):
        for j in range(len(counter2) - 1, 0, -1):
            if words1[i]==words2[j]:
                total=numbers1[i] + numbers2[j]
                output.write(words1[i] + "  "+ str(numbers1[i]) + " " + str(numbers2[j]) + "  " + str(total) + '\n' )


    output.close()

Word_Order_Frequency_Two_Books('book_1.txt','book_2.txt',3,'output1.txt')