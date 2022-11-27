alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("WELCOME TO CAESER CYPHER!")
# Functions for encrypting and decrypting
def encode():
    msg = input("Type your message:\n").lower()
    shifter = int(input("Type the shift number:\n"))
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
def decode():
    msg = input("Type your message:\n").lower()
    shifter = int(input("Type the shift number:\n"))
    encrypt = ''
    for letter in msg:
        if letter == ' ':
            encrypt += ' '
            continue
        index = alphabet.index(letter)
        new_index = index - shifter
        # print(new_index)
        encrypt += alphabet[new_index]
    print(f"Here's the encoded result: {encrypt}")

# Main Loop
redo = "yes"
while redo == "yes":
    selection = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if selection == "encode":
        encode()
    elif selection == "decode":
        decode()
    else:
        print("Wrong input")
    redo = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
