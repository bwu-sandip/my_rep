import string
input_str = input("Enter the String : ")
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

clean_str = remove_punctuation(input_str)
print(clean_str)
