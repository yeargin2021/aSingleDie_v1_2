from random import randint

i = randint(0,5)

with open("/Users/tommy/PycharmProjects/aSingleDie_v1.2/Dice-faces", "r") as file:
    dice_faces = [char for char in file.read() if not char.isspace()]
print(dice_faces[i])
