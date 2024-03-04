import requests
from random import choice
newList=[]

def random_5_letter_word():
    base_url = 'https://random-word-api.herokuapp.com/word'
    
    params = {
        'number': 10000,
        'length': 5,
        'lang': 'en'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
    
        for word in data:
            if word[-1] == 's' and word[-2] != 's':
                pass
            else:
                newList.append(word)
        data=newList
            
        if response.status_code == 200 and isinstance(data, list) and len(data) > 0:
            return choice(data)
        else:
            print(f"Failed to retrieve a 5-letter word. Status code: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error during API request: {e}")
        return None


random_word = random_5_letter_word()

crackList=newList[:]

uselessWords=""
Letterneed=""

for i in range(6):
    print("Write a 5 letter word")
    while(True):
        a=input()
        if a in crackList:
            break
        print("Word not in dictionary")

    input_string = input("Write index of which the letter assigned to a word")
    indexneed = [int(x) for x in input_string.split()]
    
    print("useless letters = ")
    uW=input()
    uselessWords=uselessWords+uW
    
    print("Needed letters = ")
    ln=input()
    Letterneed=Letterneed+ln

    input_string1 = input("Write index of which the letter are not assigned to a word")
    indexnotneed = [int(x) for x in input_string1.split()]

    ULW=sorted(set(uselessWords))
    LN=sorted(set(Letterneed))
    
    for new_word in newList:
        contains_unused_letters = any(letter in ULW for letter in new_word)
        contains_only_letters = all(letter in new_word for letter in LN )
        if len(indexneed) > 0:
            for i in indexneed:
                if(new_word[i]==a[i]):
                    index_condition=True
                else:
                    index_condition = False
                    break
            if len(indexnotneed) > 0:    
                for j in indexnotneed:
                    if(new_word[j]!=a[j]):
                        Noindex_condition=True
                        pass
                    else:
                        Noindex_condition = False
                        break
                if Noindex_condition==False:
                    newList.remove(new_word)
                elif contains_unused_letters==False and contains_only_letters==True and index_condition==True and Noindex_condition==True:               
                    print("Try this word", new_word, len(newList))
                    newList.remove(new_word)
                    break
                elif contains_unused_letters==True:
                    newList.remove(new_word)
                else:
                    pass
                
            elif contains_unused_letters==False and contains_only_letters==True and index_condition==True:               
                print("Try this word", new_word, len(newList))
                newList.remove(new_word)
                break
            elif contains_unused_letters==True:
                newList.remove(new_word)
            else:
                pass
        
        else:
            if len(indexnotneed) > 0:    
                for i in indexnotneed:
                    if(new_word[i]!=a[i]):
                        Noindex_condition=True
                        pass
                    else:
                        Noindex_condition = False
                        break
                if Noindex_condition==False:
                    newList.remove(new_word)
                elif contains_unused_letters==False and contains_only_letters==True and Noindex_condition==True:               
                    print("Try this word", new_word, len(newList))
                    newList.remove(new_word)
                    break
                elif contains_unused_letters==True:
                    newList.remove(new_word)
                else:
                    pass
            elif contains_unused_letters==False and contains_only_letters==True:               
                print("Try this word", new_word, len(newList))
                newList.remove(new_word)
                break
            elif contains_unused_letters==True:
                newList.remove(new_word)
            else:
                pass
    
    


