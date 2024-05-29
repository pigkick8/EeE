player1 = input("player1 가위, 바위, 보 입력\n")
player2 = input("player2 가위, 바위, 보 입력\n")

if player1 == '가위':
	if player2 == '가위':
		print("무승부")
	elif player2 == "바위":
		print("player2이김")
	else:
		print("player1이김")

elif player1 == "바위":
	if player2 == "바위":
		print("player1, player2 비김!!")
	elif player2 == "가위":
		print("player1 승리")
	else:
		print("player2 승리")

else:
    if player 2 == '바위':
        print("player 1 win")
    elif player 2 == '보':
        print("tie")
    else:
        print("player 2 win")
    
