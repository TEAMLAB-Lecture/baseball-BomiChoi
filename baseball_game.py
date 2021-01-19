# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    try:
        int(user_input_number)
        result = True
    except:
        result = False
    return result


def is_between_100_and_999(user_input_number):
    i = int(user_input_number)
    if i >= 100 and i < 1000:
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):
    t = three_digit
    if t[0] == t[1] or t[0] == t[2] or t[1] == t[2]:
        result = True
    else:
        result = False
    return result


def is_validated_number(user_input_number):
    u = user_input_number
    if is_digit(u) and is_between_100_and_999(u) and not is_duplicated_number(u):
        result = True
    else:
        result = False
    return result


def get_not_duplicated_three_digit_number():
    while True:
        result = get_random_number()
        if is_validated_number(str(result)):
            break
    return result


def get_strikes_or_ball(user_input_number, random_number):
    u = user_input_number
    r = random_number
    result = [0, 0]

    for i in range(3):
        for j in range(3):
            if u[i] == r[j]:
                if i == j:
                    result[0] += 1
                else:
                    result[1] += 1
    return result


def is_yes(one_more_input):
    o = one_more_input.lower()
    if o == 'y' or o == 'yes':
        result = True
    else:
        result = False
    return result


def is_no(one_more_input):
    o = one_more_input.lower()
    if o == 'n' or o == 'no':
        result = True
    else:
        result = False
    return result


def main():
    print("Play Baseball")
    def play_game():
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)

        while True:
            user_input = input('Input guess number : ')
            if is_validated_number(user_input):
                result = get_strikes_or_ball(user_input, random_number)
                print('Strikes :' , result[0] , ', Balls :', result[1])
                if result[0] == 3:
                    break
            elif user_input == '0':
                return
            else:
                print("Wrong Input, Input again")

        while True:
            ans = input("You win, one more(Y/N) ?")
            if is_yes(ans):
                play_game()
                break
            elif is_no(ans):
                break
            else:
                print("Wrong Input, Input again")

    play_game()

    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
