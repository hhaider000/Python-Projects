alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("WELCOME TO CAESER CYPHER!")
# Functions for encrypting and decrypting
def encode(msg,shifter):
    encrypt = ''
    for letter in msg:
        if letter == ' ':
            encrypt += ' '
            continue
        index = alphabet.index(letter)
        new_index = index + shifter
        # print(new_index)
        encrypt += alphabet[new_index]
    print(f"Here's the encoded result: {encrypt}")
def decode(msg,shifter):
    decrypt = ''
    for letter in msg:
        if letter == ' ':
            decrypt += ' '
            continue
        index = alphabet.index(letter)
        new_index = index - shifter
        # print(new_index)
        decrypt += alphabet[new_index]
    print(f"Here's the encoded result: {decrypt}")

# Main Loop
redo = "yes"
while redo == "yes":
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    msg = input("Type your message:\n").lower()
    shifter = int(input("Type the shift number:\n"))
    if selection == "encode":
        encode(msg,shifter)
    elif selection == "decode":
        decode(msg,shifter)
    else:
        print("Wrong input")
    redo = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
