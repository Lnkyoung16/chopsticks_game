import random
sequence = 0
player_right = 1
player_left = 1
computer_right = 1
computer_left = 1

while True:
    number_player = int(input('1과 2중 숫자 중 하나를 고르시오:'))
    number_computer = random.randint(1,2)
    if number_computer != number_player:
        sequence = 1
        print("컴퓨터는", number_computer, "을(를), 플레이어는", number_player, "(울)를 불렀습니다. 플레이어가 숫자를 맞추지 못하였으므로 컴퓨터의 선공입니다.")
        break
    else:
        sequence = 0
        print("컴퓨터는", number_computer, "을(를), 플레이어는", number_player, "(울)를 불렀습니다. 플레이어가 숫자를 맞췄으므로 플레이어의 선공입니다.")
        break

while True:
    if sequence == 0:
        print("")
    else:
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            # 컴퓨터의 왼손으로 플레이어 공격
            hand_choice = random.randint(1,2)
            if hand_choice == 1:
                if player_left < 5:
                    player_left = player_left + computer_left
                else:
                    continue
            else:
                player_right = player_right + computer_left
        elif computer_choice == 2:
            #컴퓨터의 오른손으로 플레이어 공격
            hand_choice = random.randint(1, 2)
            if hand_choice == 1:
                player_left = player_left + computer_right
            else:
                player_right = player_right + computer_right
        else:
            #컴퓨터의 양손 수 나누기
            computer_sum = computer_left + computer_right
            while True:
                temp_left = random.randint(1,computer_sum)
                temp_right = computer_sum - temp_left
                if temp_right < 5 or temp_left < 5:
                    if temp_left != computer_left or temp_right != computer_right:
                        break

