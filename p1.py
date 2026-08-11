def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

text = input("Enter text: ")
choice = input("Enter encode or decode: ").lower()
shift = int(input("Enter shift key: "))

if choice == "decode":
    shift = -shift
elif choice != "encode":
    print("Invalid choice!")
    exit()

print("Result:", caesar_cipher(text, shift))