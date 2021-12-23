import world
from player import Player
level = 1

def play():
    world.load_tiles(level)
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    if player.victory == True and level == 1:
        print("\n")
        print("                        Col.Rodes got you location in desert\n")
        print("Helicopter hovering over desert..... Tony stark secured ... Col.Rodes, Buddy next time you going to travel with me.\n")
        print("                     *******************Level- 1 ends ***********\n")
        player.levell += 1
    elif player.victory == True and level == 2:
        print("\n")
        print("         Tony proposes to Pepper and asks her to take over Stark Industries\n")
        print("                    *******************Level- 2 ends ***********\n")
        player.levell += 2
    elif player.victory == True and level == 3:
        print("\n")
        print("               All suits of iron man rests back \n")
        print("************* Happy Christmas and Happy New Year to Prof.Oakes *****************  \n")
        print("                     *******************Level- 3 ends ***********")

    else:
        print("Play Again level")
    global level_cleared
    global level_var
    level_cleared = player.victory
    level_var = player.levell

if __name__ == "__main__":
      play()
      while level_cleared == True:
        level = level_var
        play()
        if level == 3 : break
