duration = int( input("Enter the dduration in seconds: ") )
print(f"The duration is: {duration // 3600}, {(duration % 3600) // 60}, {((duration % 3600) % 60)}")