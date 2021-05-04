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
        print("왼손으로 컴퓨터 왼손 공격: 1, 왼손으로 컴튜터 오른손 공격: 2, 오른손으로 컴퓨터 왼손 공격: 3, 오른손으로 컴퓨터 오른손 공격: 4, 숫자 나누기: 5")
        player_choice = int(input("다음의 행동 중 어느 것을 취하시겠습니까?"))
        if player_choice == 1:
            if player_left < 5 and computer_left < 5:
                computer_left = player_left + computer_left
                print("플레이어의 왼손으로 컴퓨터의 왼손을 쳤습니다.")
                print("플레이어의 왼손:", player_left)
                print("플레이어의 오른손:", player_right)
                print("컴퓨터의 왼손:", computer_left)
                print("컴퓨터의 오른손:", computer_right)
            else:
                print("컴퓨터의 왼손 또는 플레이어의 왼손이 5 이상이므로 진행할 수 없습니다.")
                print("다시 지정해주십시오.")
                continue
        elif player_choice == 2:
            if player_left < 5 and computer_right < 5:
                computer_right = player_left + computer_right
                print("플레이어의 왼손으로 컴퓨터의 오른손을 쳤습니다.")
                print("플레이어의 왼손:", player_left)
                print("플레이어의 오른손:", player_right)
                print("컴퓨터의 왼손:", computer_left)
                print("컴퓨터의 오른손:", computer_right)
            else:
                print("컴퓨터의 오른손 또는 플레이어의 왼손이 5 이상이므로 진행할 수 없습니다.")
                print("다시 지정해주십시오.")
                continue
        elif player_choice == 3:
            if player_right < 5 and computer_left < 5:
                computer_left = player_right + computer_left
                print("플레이어의 오른손으로 컴퓨터의 왼손을 쳤습니다.")
                print("플레이어의 왼손:", player_left)
                print("플레이어의 오른손:", player_right)
                print("컴퓨터의 왼손:", computer_left)
                print("컴퓨터의 오른손:", computer_right)
            else:
                print("컴퓨터의 왼손 또는 플레이어의 오른손이 5 이상이므로 진행할 수 없습니다.")
                print("다시 지정해주십시오.")
                continue
        elif player_choice == 4:
            if player_right < 5 and computer_right < 5:
                computer_right = player_right + computer_right
                print("플레이어의 오른손으로 컴퓨터의 오른손을 쳤습니다.")
                print("플레이어의 왼손:", player_left)
                print("플레이어의 오른손:", player_right)
                print("컴퓨터의 왼손:", computer_left)
                print("컴퓨터의 오른손:", computer_right)
            else:
                print("컴퓨터의 오른손 또는 플레이어의 오른손이 5 이상이므로 진행할 수 없습니다.")
                print("다시 지정해주십시오.")
                continue
        elif player_choice == 5:
            while True:
                player_sum = player_left + player_right
                print("현재 왼손은", player_left, "오른손은", player_right, "입니다.")
                print("각 손의 수를 어떻게 지정하시겠습니까?")
                temp_left = int(input("왼손의 수:"))
                temp_right = int(input("오른손의 수:"))
                if temp_left == player_left or temp_right == player_right:
                    print("기존의 수와 같게 지정할 수 없습니다. 숫자를 다시 지정해주세요.")
                elif temp_left >= 5 or temp_right >= 5:
                    print("한 손의 수는 5를 넘어갈 수 없습니다. 숫자를 다시 지정해주세요.")
                elif temp_left + temp_right != player_sum:
                    print("기존에 가지고 있던 손의 수와 일치하지 않습니다. 숫자를 다시 지정해주세요.")
                else:
                    player_left = temp_left
                    player_right = temp_right
                    print("플레이어의 양손의 수를 왼손, 오른손 각각", player_left, player_right, "으로 분배했습니다.")
                    print("플레이어의 왼손:", player_left)
                    print("플레이어의 오른손:", player_right)
                    print("컴퓨터의 왼손:", computer_left)
                    print("컴퓨터의 오른손:", computer_right)
                    break
        sequence = 1
    else:
        computer_choice = random.randint(1,3)
        if computer_choice == 1:
            print("1번")
            # 컴퓨터의 왼손으로 플레이어 공격
            hand_choice = random.randint(1,2)
            if computer_left < 5:
                if hand_choice == 1:
                    if player_left < 5:
                        player_left = player_left + computer_left
                        print("컴퓨터의 왼손으로 플레이어의 왼손을 쳤습니다.")
                        print("플레이어의 왼손:", player_left)
                        print("플레이어의 오른손:", player_right)
                        print("컴퓨터의 왼손:", computer_left)
                        print("컴퓨터의 오른손:", computer_right)
                    else:
                        continue
                else:
                    if player_right < 5:
                        player_right = player_right + computer_left
                        print("컴퓨터의 왼손으로 플레이어의 오른손을 쳤습니다.")
                        print("플레이어의 왼손:", player_left)
                        print("플레이어의 오른손:", player_right)
                        print("컴퓨터의 왼손:", computer_left)
                        print("컴퓨터의 오른손:", computer_right)
                    else:
                        continue
            else:
                continue
        elif computer_choice == 2:
            print("2번")
            #컴퓨터의 오른손으로 플레이어 공격
            hand_choice = random.randint(1, 2)
            if computer_left < 5:
                if hand_choice == 1:
                    if player_left < 5:
                        player_left = player_left + computer_right
                        print("컴퓨터의 오른손으로 플레이어의 왼손을 쳤습니다.")
                        print("플레이어의 왼손:", player_left)
                        print("플레이어의 오른손:", player_right)
                        print("컴퓨터의 왼손:", computer_left)
                        print("컴퓨터의 오른손:", computer_right)
                    else:
                        continue
                else:
                    if player_right < 5:
                        player_right = player_right + computer_right
                        print("컴퓨터의 오른손으로 플레이어의 오른손을 쳤습니다.")
                        print("플레이어의 왼손:", player_left)
                        print("플레이어의 오른손:", player_right)
                        print("컴퓨터의 왼손:", computer_left)
                        print("컴퓨터의 오른손:", computer_right)
                    else:
                        continue
            else:
                continue
        else:
            #컴퓨터의 양손 수 나누기
            if computer_left < 5 and computer_right < 5:
                computer_sum = computer_left + computer_right
                while True:
                    temp_left = random.randint(0,computer_sum)
                    temp_right = computer_sum - temp_left
                    if temp_right < 5 or temp_left < 5:
                        if temp_left != computer_left or temp_right != computer_right:
                            computer_left = temp_left
                            computer_right = temp_right
                            print("컴퓨터는 양손의 수를 왼손:", computer_left, "과 오른손:", computer_right, "으로 나눴습니다.")
                            break
            else:
                continue
        sequence = 0
    if computer_left >= 5 and computer_right >= 5:
        break
    if player_left >= 5 and player_right >= 5:
        break


if computer_count == 2:
    print("플레이어의 승리")
elif player_count == 2:
    print("컴퓨터의 승리")
