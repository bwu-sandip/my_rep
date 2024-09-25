n = int(input("Enter a two-digit number: "))
def pal(n):
    num_str = str(n)
    return num_str == num_str[::-1]

if pal(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
