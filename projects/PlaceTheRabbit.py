plants =[
        ["🥬","🥬","🥬"],
        ["🥬","🥬","🥬"],
        ["🥬","🥬","🥬"] 
        ]
choice = input(f"""
Welcome to place the rabbit
{plants[0]}
{plants[1]}
{plants[2]}
Where should the rannbit go?🐇
Please choose a row and a colomn: 
""")
row = int(choice[0])-1
col = int(choice[1])-1
plants[row][col] = "🐇"
print(f"""
  Success ....
      
{plants[0]}
{plants[1]}
{plants[2]}
""")
