def count_word(word_input):
    w_count = word_input.split()
    count = len(w_count)
    print (f"Cantidad de plabras ingresadas: {count}")


def convertInputString(rawInput): 
    rawString = rawInput.lower()     
    rawList = list(rawString) 
    return rawList


def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return stripAnalphabetics(dirtyList)
    return dirtyList 

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "El texto ingresdo es un palindromo" 
    else: 
        return "El texto ingresado no es un palindromo" 

def main(originalList): 
    print("\nPalindromo checker") 
    originalList = convertInputString(originalList)  
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

