import random


while True:    
    current_number = 0

    if random.randint(0, 1) == 0:
        current_player = "Người chơi"
    else:
        current_player = "Máy tính"

    while current_number <= 21:
        print("Số tổng hiện tại là: " + str(current_number))
        
        if current_player == "Người chơi":

            player_choice = int(input("Bạn hãy chọn một số (1, 2 hoặc 3): "))

            while player_choice != 1 and player_choice != 2 and player_choice != 3:
                player_choice = int(input("Số không hợp lệ, vui lòng chọn lại một số (1, 2 hoặc 3): "))

            player_choice = int(player_choice)

            current_number = current_number + player_choice

            if current_number >= 21:
                print("Số tổng hiện tại là: " + str(current_number) + ". Bạn đã thua")
                break
            else:
                current_player = "Máy tính"

        else:

            computer_choice = random.randint(1, 3)
            print("Lượt của máy tính. Máy tính chọn số: " + str(computer_choice))
            current_number = current_number + computer_choice

            if current_number >= 21:
                print("Số tổng hiện tại là: " + str(current_number) + ". Bạn đã thắng!")
                break
            else:
                current_player = "Người chơi"

    play_again = input("Bạn có muốn chơi lại không? (Y/N) ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Kết thúc trò chơi!")
        break