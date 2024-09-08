with open("./input/Names/invited_names.txt")as data:
    names = data.read().split()

with open("./input/Letters/starting_letter.txt") as letterFile:
    letter = letterFile.read()

for name in names:
    newLetter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")as output:
        output.write(newLetter)