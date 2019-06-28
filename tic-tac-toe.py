import gameGround as gG

game_ground = gG.GameGround()
gG.GameGround.__mro__

def try_game_manual():



    game_ground.create_playing_field()

    game_ground.make_turn((3, 1, 'X'))
    game_ground.make_turn((1, 3, 'X'))
    game_ground.make_turn((2, 2, 'X'))

    game_ground.make_turn((2, 3, 'Y'))
    game_ground.make_turn((3, 3, 'Y'))

    game_ground.make_turn((1, 1, 'Y'))
    game_ground.make_turn((1, 2, 'Y'))
    game_ground.make_turn((2, 1, 'Y'))
    game_ground.make_turn((3, 2, 'Y'))

    game_ground.print_grid()


    res = game_ground.check_win('X')
    print(res)

    res1 = game_ground.check_draft()
    print(res1)




def try_game():

    step = 1
    game_ground.create_playing_field()

    while True:

        if step % 2 == 0:
            player = 'O'  # players[1]
        else:
            player = 'X'  # players[0]

        print("Please enter 1st coordinate: ")
        m = int(input())
        #m=2

        print("Please enter 2nd coordinate: ")
        n = int(input())
        #n=3


        if game_ground.make_turn((m, n, player)) == False:
            print("Your coordinates is wrong. Please try again. ")
            continue

        game_ground.print_grid()
        #print(game_ground.playingField)

        if game_ground.check_win(player):
            print("winner is "+player)
            #print(game_ground.playingField)
            break

        if game_ground.check_draft():
            print("it's draft")
            break
        step += 1

try_game()