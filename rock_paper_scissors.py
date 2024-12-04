def rock_paper_sc (player1, player2):
    if player1 == player2:
        return "!!!TIE!!!"
    if player1 == "Paper":
        if player2 == "Rock":
            return "Player1 WON!!!"
        elif player2 == "Scissors":
            return "Player2 WON!!!"
    elif player1 == "Rock":
        if player2 == "Paper":
            return "Player2 WON!!!"
        elif player2 == "Scissors":
            return f"Player1 WON!!!"
    elif player1 == "Scissors":
        if player2 == "Rock":
            return "Player2 WON!!!"
        elif player2 == "Paper":
            return "Player1 WON!!!"


print(rock_paper_sc("Rock", "Paper"))
c = 0
pl1 = 0
pl2 = 0
while c < 3:
    player1 = input("Player1, Enter 'Rock', 'Paper' or 'Scissors': ")
    player2 = input("Player2, Enter 'Rock', 'Paper' or 'Scissors': ")
    print(rock_paper_sc(player1, player2))
    c+=1