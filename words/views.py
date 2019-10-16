from django.shortcuts import render

from django.http import HttpResponse



def home(request):
    return HttpResponse("Hello, this is the words homepage")


def index(request, text):
    return HttpResponse("Hello, world. You're at the words index page.")




# def calculate(text):
    

#     Text = text

#     for char in '-.,\n':
#         Text=Text.replace(char,' ')
#         Text = Text.lower()
    
#     word_list = Text.split()

#     # Initializing Dictionary
#     d = {}


#     for word in word_list:
#         d[word] = d.get(word, 0) + 1

#     word_freq = []
#     for key, value in d.items():
#         word_freq.append((value, key))
    
#     word_freq.sort(reverse=True) 

    
#     return word_freq[0]



def calculateSpecificWord(text, word):
    
    InputWord = word
    Text = text

    for char in '-.,\n':
        Text=Text.replace(char,' ')
        Text = Text.lower()
    
    word_list = Text.split()

    # Initializing Dictionary
    d = {}


    for word in word_list:
        d[word] = d.get(word, 0) + 1

    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))
    
    word_freq.sort(reverse=True) 
    

    if InputWord in word_freq:
        print("ja hij zit erin")

    
    



    
    return word_freq



def calculateHighestFrequency(request):

    Text="""
        bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.  We hold these truths to be
        self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. """
    
    Word = "connected"
    word = calculateSpecificWord(Text, Word) 

    # print(word)
    


    
    

    # text
    # Text="""
    #     bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.  We hold these truths to be
    #     self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. """
    
    # for char in '-.,\n':
    #     Text=Text.replace(char,' ')
    #     Text = Text.lower()
    
    # word_list = Text.split()

    # # Initializing Dictionary
    # d = {}


    # for word in word_list:
    #     d[word] = d.get(word, 0) + 1

    # word_freq = []
    # for key, value in d.items():
    #     word_freq.append((value, key))
    
    # word_freq.sort(reverse=True) 

    # print(word_freq)

    # print(word_freq[0])


    

    return HttpResponse("the most frequent word is:  " + str(word))
    

