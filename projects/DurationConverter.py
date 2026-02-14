duration = int( input("Enter the dduration in seconds: ") )
houres = duration // 3600
minutes = (duration % 3600) // 60
seconds = ((duration % 3600) % 60)
print(f"The duration is: {houres}, {minutes}, {seconds}")

duration = int( input("Enter the dduration in seconds: ") )
print(f"The duration is: {duration // 3600}, {(duration % 3600) // 60}, {((duration % 3600) % 60)}")