import string,random
letters=random.choice(list(string.ascii_lowercase))
numbers=str(random.randrange(1,10))
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
n_letters=int(input("Enter number of letters: "))
n_numbers=int(input("Enter number of numbers: "))
n_symbols=int(input("Enter number of symbols: "))
password=[]
for i in range(n_letters):
    password.append(letters)
for i in range(n_numbers):
    password.append(numbers)
for i in range(n_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
print("Your password is",''.join(password))

