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
        print('{} is not 1, 2, or 3.'.format(ret_val))
        input()
        menu()
        ret_val = input(prompt_msg).lower()
    return ret_val


def computer_choice():
    choice = str(random.randint(1, 3))
    if choice == '1':
        return 'Rock'
    elif choice == '2':
        return 'Paper'
    else:
        return 'Scissors'


def selections():
    clear()
    print('You picked: {}'.format(user_choice()))
    print('The computer picked: {}'.format(computer_choice()))


def win():
    selections()
    print('You win!')


def lose():
    selections()
    print('You lose!')


def draw():
    selections()
    print('Draw!')


def game(u_choice, c_choice):
    if u_choice == 'Rock':
        if c_choice == 'Rock':
            draw()
        elif c_choice == 'Paper':
            lose()
        else:
            win()
    elif u_choice == 'Paper':
        if c_choice == 'Rock':
            win()
        elif c_choice == 'Paper':
            draw()
        else:
            lose()
    elif u_choice == 'Scissors':
        if c_choice == 'Rock':
            lose()
        elif c_choice == 'Paper':
            win()
        else:
            draw()
    else:
        pass


def run():
    menu()
    game(user_choice(), computer_choice())


if __name__ == '__main__':
    run()
