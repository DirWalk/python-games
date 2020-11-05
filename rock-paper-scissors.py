import random
import os
import platform


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    clear()
    print('Rock Paper Scissors')
    print('----------------------')
    print('1. Rock.')
    print('2. Paper.')
    print('3. Scissors')


def user_choice():
    choice = bool_prompt('Please make your selection: ')
    if choice == '1':
        return 'Rock'
    elif choice == '2':
        return 'Paper'
    else:
        return 'Scissors'


def bool_prompt(prompt_msg):
    ret_val = input(prompt_msg)
    while ret_val not in ['1', '2', '3']:
        input('{} is not 1, 2, or 3.'.format(ret_val))
        menu()
        ret_val = input(prompt_msg).lower()
    return ret_val


def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])


def win():
    return 'You win!'


def lose():
    return 'You lose!'


def draw():
    return 'Draw!'


def game(u_choice, c_choice):
    clear()
    print('You picked: {}'.format(u_choice))
    print('The computer picked: {}'.format(c_choice))
    if u_choice == 'Rock':
        if c_choice == 'Rock':
            outcome = draw()
            print(outcome)
        elif c_choice == 'Paper':
            outcome = lose()
            print(outcome)
        else:
            outcome = win()
            print(outcome)
    elif u_choice == 'Paper':
        if c_choice == 'Rock':
            outcome = win()
            print(outcome)
        elif c_choice == 'Paper':
            outcome = draw()
            print(outcome)
        else:
            outcome = lose()
            print(outcome)
    elif u_choice == 'Scissors':
        if c_choice == 'Rock':
            outcome = lose()
            print(outcome)
        elif c_choice == 'Paper':
            outcome = win()
            print(outcome)
        else:
            outcome = draw()
            print(outcome)
    else:
        pass

    choice = input('Would you like to play again? [y/n] ').lower()
    while choice not in ['y', 'n']:
        input('{} is not y or n'.format(choice))
        clear()
        print('You picked: {}'.format(u_choice))
        print('The computer picked: {}'.format(c_choice))
        print(outcome)
        choice = input('Would you like to play again? [y/n] ').lower()
    if choice == 'n':
        exit(0)


def run():
    while True:
        menu()
        game(user_choice(), computer_choice())


if __name__ == '__main__':
    run()
