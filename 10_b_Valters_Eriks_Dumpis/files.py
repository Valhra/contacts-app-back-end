file = open("data.txt", "w")
for i in range(1,101):
    file.write(f"Name{i}\n")

file.close()
