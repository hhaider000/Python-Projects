from CaeserArt import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(msg,shifter,direction):
    crypt = ''
    for letter in msg:
        if letter not in alphabet:
            crypt += letter
            continue
        index = alphabet.index(letter)
        if direction == "encode":
            shift = shifter * 1
        elif direction == "decode":
            shift = shifter * -1
        new_index = index + shift
        if new_index > 26:
            new_index = new_index % len(alphabet)
        crypt += alphabet[new_index]
    print(f"Here's the encoded result: {crypt}")
redo = "yes"
while redo == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        msg = input("Type your message:\n").lower()
        shifter = int(input("Type the shift number:\n"))
        caeser(msg,shifter,direction)
    else:
        print("Wrong input")
    redo = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n"
