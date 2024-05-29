player1 = input("player1 가위, 바위, 보 입력\n")
player2 = input("player2 가위, 바위, 보 입력\n")

if player1 == '가위':

elif player1 == "바위":
	if player2 == "바위":
		print("player1, player2 비김!!")
	elif player2 == "가위":
		print("player1 승리")
	else:
		print("player2 승리")

else: