# group words, based on same letters
# [tea, eat, ate, tan, bat, nat] => [[tea, ate, eat], [bat], [tan, nat]]

def group(array):
    if len(array) == 0:
        return array
    letterBasedList = []
    iList = []
    for i in array:
        if i not in iList:
            iList = []
            codeWord = i
            iList.append(i)
            array.remove(i)
            for j in array:
                trueList = []
                for k in i:
                    if k not in j:
                        trueList.append(False)
                if not False in trueList:
                    iList.append(j)
            letterBasedList.append(iList)
    return letterBasedList


print(group(['tea', 'eat', 'ate', 'tan', 'bat', 'nat', 'bred', 'derb', 'abracadabra']))





