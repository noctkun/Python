import random

stages = ['''
  +---+
  |   |
  😵  |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  😵  |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  😵  |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  😵  |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  😵  |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  😵  |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
print("WELCOME TO theHANGMAN!!! 😵")
z = 0
wordlist = ["l a n c e l o t", "c z e c h s l o v a k i a", "a l p h o n s o", "b o u l e v a r d", "z e p h y r u s",
            "f l o c c i n a u c i n i h i l i p i l i f i c a t i o n"]
n = 5
A = ''
while True:
    random.shuffle(wordlist)
    a = wordlist[0]
    c = a.split()
    b = a.split()
    for i in range(n):
        n2 = random.randint(0, 4)
        b[n2] = '_'
    for i in range(len(b)):
        print(b[i], end="")
    break
print("\nThe word you have to find>>>")
print(A)
print("Please guess the letters from left to right")

while True:
    x = b.index('_')
    c1 = input("\nPlease enter your letter: ")

    if z == 6:
        print("You have ", 6 - z, " chances left!")
        print(stages[0])
        print("THE GUY IS DEAD")
        break
    else:
        pass

    if c1 == c[x]:
        x = b.index('_')
        print("Perfecto!!!")

        b[x] = c1
        for i in range(len(b)):
            print(b[i], end="")
        if b == c:
            print("\nYou WIN")
            print("The guy Lives")
            break
        else:
            pass

    else:
        z += 1
        if z == 6:
            print("You have ", 6 - z, " chances left!")
            print(stages[0])
            print("THE GUY IS DEAD")
            break
        print("Nah!")
        print("You have ", 6 - z, " chances left!")
        print(stages[6 - z])
        pass
