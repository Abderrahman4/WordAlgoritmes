from django.shortcuts import render

from django.http import HttpResponse



def home(request):
    return HttpResponse("Hello, this is the words homepage")


def index(request, text):
    return HttpResponse("Hello, world. You're at the words index page.")




def highestFrequency(text):
    

    Text = text
    
     # haal leestekens eruit en maak alle letters klein

    for char in '-.,\n':
        Text=Text.replace(char,' ')
        Text = Text.lower()
    
    word_list = Text.split()

    # Initializing Dictionary
    d = {}


    # tel voor elke woord begin bij 0

    for w in word_list:
        d[w] = d.get(w, 0) + 1

    # zet de dictionary in een tuple
    
    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))

    # sorteer en keer om
    
    word_freq.sort(reverse=True) 

    return word_freq[0]
   
    

def specificWord(text, word):
    
    InputWord = word
    Text = text

    for char in '-.,\n':
        Text=Text.replace(char,' ')
        Text = Text.lower()
    
    word_list = Text.split()

    d = {}

    for w in word_list:
        d[w] = d.get(w, 0) + 1

    # omdat je alleen het aantal wil zoek je met het inputwoord
    # door de keys van de dictionary

    if InputWord in d.keys():
        return d[InputWord]
    else:
         return None

    
def withN(text, n):
    
    n = n
    Text = text

    for char in '-.,\n':
        Text=Text.replace(char,' ')
        Text = Text.lower()
    
    word_list = Text.split()

    d = {}


    for w in word_list:
        d[w] = d.get(w, 0) + 1
    
    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))
    
    word_freq.sort(reverse=True) 

    # num_fre =[]
    # new_array = []
    # for i, value in enumerate(word_freq[:12]):
    #     if word_freq[i][0] == word_freq[i+1][0]:
    #         print(value)
    #         print(word_freq[i][0],word_freq[i+1][0])
    #         num_fre.append(value)
    #         print(num_fre)
           
              
    #     print(num_fre)    
    #             print(sorted(num_fre, key=lambda  val :val[1]))
            
    #         print(value,i)
   
    
    return word_freq[:n]




def calculate(request):

    # highest frequency

    Text="""
        bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.  We hold these truths to be
        self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. """
    
    
    count = highestFrequency(Text) 


    # specific word
    # Text="""
    #     bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.  We hold these truths to be
    #     self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. """
    
    # Word = "the"
    # count = specificWord(Text, Word) 

    # print(word)
    
    # Text="""
    #     bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.  We hold these truths to be
    #     self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. """
    
    # n = 12
    
    # count = withN(Text, n) 


    
    


    

    return HttpResponse("het resultaat is:  " + str(count))
    

