
import random

def Hangman():
    print ('Игра "Виселица"')
    wordlist =['привет', 'дело', 'калашников', 'автомат', 'сыр']
    secret = random.choice(wordlist)
    guesses = 'еиваро'
    turns = 10

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print (letter,end=' ')
            else:
                print ('_',end=' ')
                missed= missed + 1

        print()

        if missed == 0:
            print ('\nВы угадали слово!', secret)
            break

        guess = input('\nвведите букву: ')
        guesses += guess

        if guess not in secret:
            turns = turns - 1
            print ('\nне та буква')
            print ('\n',turns, 'попытки осталось')
            if turns == 9:print ('\n|\n|\n|\n|\n|  ')
            if turns == 8:print (' ______\n|\n|\n|\n|\n|')
            if turns == 7:print (' ______\n|/\n|\n|\n|\n|')
            if turns == 6:print ('______\n|/ |\n|\n|\n|\n|')
            if turns == 5:print ('______\n|/ |\n|  o\n|\n|\n|')
            if turns == 4:print ('______\n|/ |\n|  o\n|  |\n|  |\n|')
            if turns == 3:print ('______\n|/ |\n|  o\n| /|\n|  |\n|')
            if turns == 2:print ('______\n|/ |\n|  o\n| /|\ \n|  |\n|')
            if turns == 1:print ('______\n|/ |\n|  o\n| /|\ \n|  |\n| /')
            if turns == 0:
                print ('______\n|/ |\n|  o\n| /|\ \n|  |\n| / \ ')
                print ('\n\nВы проиграли!')
        
playagain = 'да'
while playagain == 'да': 
    Hangman()
    print('Хотите поиграть ещё?? (да или нет)')
    playagain = input()