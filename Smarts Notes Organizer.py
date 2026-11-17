sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample File 'class-notes.txt' created.")

print("\nPART 1: Preview With Read(40)")

print("\nPART 2: Readlines()")

print("\nPART 3: Loop Line By Line")

print("\nPART 4: Filter With A Condition")

print("\nPART 5: Copy Selected Lines To A New File")

print("\nPART 6: Organized Notes")