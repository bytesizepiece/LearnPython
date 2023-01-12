print('how many cats own?')
numCats = input()

try:
    if int(numCats) >= 4:
        print('thats a lot!')
    else:
        print('not many!')

except ValueError:
    print('not a number!')



eggs = 10

def spam(count):
        global eggs
        eggs = count + eggs

spam(eggs)

print(eggs)