num = input(" Type a Number ")

def isPalindrome( num ): 
    words = list(num)
    invertedWords=[]
    for i in range(len(words) -1, -1, -1):
        print(words[i])
        invertedWords.append(words[i])
    if invertedWords == words:
        return True
    else:
        return False

print(isPalindrome(num))