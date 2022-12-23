alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = False


def encode(text, shift):
    output = ""
    for i in range(len(text)):
        output += alphabet[(alphabet.index(text[i])+shift)%25]
    return output

def decode(text, shift):
    output = ""
    for i in range(len(text)):
        output += alphabet[(alphabet.index(text[i])-shift)%25]
    return output

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        print("The encoded message is: " + encode(text,shift))
    elif direction == "decode":
        print("The decoded message is: " + decode(text,shift))
    else:
        print("wrong option")
    restart = input("Type \"yes\" if you want to go again. Otherwise type \"no\"\n")
    if restart == "no":
        end = True