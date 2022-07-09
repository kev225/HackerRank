'''
Task

Given n names and phone numbers, assemble a phone book that maps
friends' names to their respective phone numbers. You will then be given
an unknown number of names to query your phone book for. For each name
queried, print the associated entry from your phone book on a new line
in the form name=phoneNumber; if an entry for name is not found, print Not
found instead.
'''


n = int(input())
phonebook = dict(input().split() for _ in range(n))


find = []
try:
    for i in range(n):
        i = input()
        if i != "":
            find.append(i)
        else:
            break
except:
    pass


for i in find:
    if i in phonebook:
       print(f'{i}={phonebook[i]}')
    else:
       print(f'Not found')
