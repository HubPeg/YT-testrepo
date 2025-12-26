
print("hello world")

def write_name(name, surname):
    sentence = f"Hello my name is {name} {surname}"

    return sentence

def padel_position(position):
    position = position
    game = f"{x} and I play on the {position} side"

    return game


x = write_name("Arturo", "Coello")
y = padel_position("right")

print(x)
print(y)