"""Module that let you play a game name Alka by Alan Baljeu."""
import os
from capture_version import capture_classic,capture_continu,capture_ambush


def alka():
    #initialisation
    rules()
    n,player = board_size_and_player_select()
    version = choose_game_version()
    board = new_board(n)
    removed = []
    display(board, n, removed)
    #tour
    while again(board, n, removed):
        i = select(board, n, player, removed)
        board = put(board, player, i)
        if version == 1:
            removed = capture_classic(board, n, player, i)
        elif version == 2:
            removed = capture_continu(board, n, player, i)
        else:
            removed = capture_ambush(board, n, player, i)
        board = remove_captured(board,removed,n)
        display(board, n,removed)
        player = change_player(player)
    win (board,n,player,removed)


def board_size_and_player_select():
    #board size
    n = 0
    while n < 4:
        try:
            n = int(input("taille du plateau? "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    #player selection
    player = 0
    while player not in [1,2]:
        while True:
            try:
                player=int(input("qui commence,joueur 1 ou 2?"))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    return(n,player)


def choose_game_version():
    print("Choisir la version du jeu.")
    print("(1) La version classique. Un joueur peut placer un pion ")
    print("et constituer un groupe de pions adjacents sans cases adjacentes vides, ")
    print("sans que ce groupe de pions soit capturé.")
    print("(2)La version continue. La première et la dernière case du plateau sont connectées.")
    print("(3)La version embusquée. Si un joueur place un pion ")
    print("et constitue un groupe de pions adjacents sans cases adjacentes vides,")
    print("alors ce groupe sera capturer par l'adversaire.")

    while True:
        try:
            version = int(input("quel version vous souhaiter jouer"))
            if version in [1,2,3]:
                return version
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def new_board(n):
    board = [0]*n
    return board


def display(board, n, removed):
    os.system('cls' if os.name == 'nt' else 'clear')
    displayed_board = ""
    board_number = ""
    removed_board = ""
    for index in range(0,n):
        if index >= 10:
            displayed_board += " "
            removed_board += " "
        #afficher les pion enlever
        if index in removed:
            removed_board += " X"
        else:
            removed_board += " ."
        #afficher les pion
        if board[index] == 0:
            displayed_board += " ."
        elif board[index] == 1:
            displayed_board += " X"
        else:
            displayed_board += " O"
        #afficher les position des pion
        board_number += " "+str((index+1))
    print("pion retier\n",removed_board,"\nEtat actuel\n",displayed_board,"\n",board_number)


def again(board, n, removed):
    tf_var=False
    for index in range(0,n):
        if board[index] == 0 and index not in removed:
            tf_var = True
    return tf_var


def select(board, n, player, removed):
    print("joueur ",player)
    while True:
        while True:
            try:
                i = int(input("Où placer ton pion? "))-1
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        if possible(board,n,removed,i) is True:
            return i
        else:
            print("Placement illegale",i+1)


def possible(board,n,removed,i):
    if i>=0 and i<=(n-1) and board[i] == 0 and i not in removed:
        return True
    else:
        return False


def put(board, player, i):
    board.pop(i)
    board.insert(i,player)
    return board


def remove_captured(board,removed,n):
    for index in range(0,n):
        if index in removed:
            board[index] = 0
    return board


def change_player(player):
    if player==1:
        return 2
    elif player==2:
        return 1


def win(board,n,player,removed):
    print("le joueur ",player,"ne peut plus placer de pion")
    display(board, n,removed)
    scr_plr1 = board.count(1)
    scr_plr2 = board.count(2)
    print("le score est de ",scr_plr1,"pour le 1er joueur et de ",scr_plr2,"pour le 2nd joueur")
    if scr_plr1<scr_plr2:
        print("le joueur 2 a gagner")
    elif scr_plr1>scr_plr2:
        print("le joueur 1 a gagner")
    else:print("les deux joueur sont a égaliter")
    #proposer au joueur de rejouer une partie
    replay =""
    replay=input("voulez vous rejouer?")
    if replay in ["oui","o","yes","y"]:
        alka()


def rules():
    print("1:Un joueur ne peut placer un pion que sur une")
    print(" case vide  et  qui n'a pas ete capturer au tour precedant.")
    print("2:Si un joueur ne peut plus placer de pion la partie est terminée.")
    print("3:Si après qu’un joueur ait placé un pion. Un groupe de pions adverse")
    print("n’a plus de cases adjacentes vides.Ceux-ci sont capturés et retirés du plateau.")
    input()



if __name__ == "__main__":
    alka()
