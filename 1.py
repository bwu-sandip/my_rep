word = input("Enter a String : ")
symbol = "`~!@#$%^&*()_-=+{}[]\|;:',<.>/?"

for i in word:
    if i in symbol:
        word = word.replace(i, "")
        
print(word)
