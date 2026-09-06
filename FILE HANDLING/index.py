# - FILE HANDLING - My bucket list ----------------------
# Topics: open() | file modes r/w/a | read() | readlines() | write() | close()


# - PART 1: Write your bucket list to a file
# 'w' mode creates a file if it does not exist.
# if the file already exits, 'w' wipes the old content
file = open("bucket-list.txt", "w")
file.write("1. Visit the eiffel tower\n")
file.write("To learn to play the guiter\n")
file.write("3. code `my game\n")
file.close()
print("Bucket list saved to bucket-list.txt!")


file = open