n = int(input("How Many Characters To Preview?"))
file = open("class-notes.txt", "r")\
print(file.read(n))
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("Total Lines :", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Skip Lines Starting With:")
file = open("class-notes.txt", "r")
for line in file:
    if line.startwith(word):
        print("Skip ->", line.strip())
    else:
        print("Keep ->", line.strip())
file.close()
print()

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd Lines Saved To odd-lines.txt")