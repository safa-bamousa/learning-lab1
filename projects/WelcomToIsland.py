wich_door = input("""
☠️
Welcom to my Island!
There are two doors in front of you. 🚪 a red door and 🚪 a blue door
wich door do you want to open?
""").lower()
if wich_door == "blue":
    print("""You chose the crocodile door.
          Game over!🐊🐊🐊
          """)
elif wich_door == "red":
    wich_color = input("""Great! now you entered a room.
          you found three boxes: 🎁 white, 🎁 black, 🎁 green
          Which bow do you open?
          """).upper()
    if wich_color == "WHITE" :
        print("Oops! You opened a box filled woth snakes🐍🐍🐍")
    elif wich_color == "BLACK":
        print("Oops! You opened a box filled with spiders🕷️🕷️🕷️")
    elif wich_color == "GREEN":
        print("Congratulation! You found the treasure!🪙🪙🪙")
    else:
        print("Invalide choice!❌❌❌")
else:
    print("Invalide choice!❌❌❌")