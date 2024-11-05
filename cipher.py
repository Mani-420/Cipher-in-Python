import ciper_art

print(ciper_art.ciper)
ciper_art.greet()

def cypher(message, shift_number, choice):
    final_text = ""
    for letter in message:
        if (letter in ciper_art.alphabets):
            position = ciper_art.alphabets.index(letter)
            if choice == "encode":
                new_position = position + shift_number
            elif choice == "decode":
                new_position = position - shift_number
            else:
                print("Invalid input.\nPlease try again.")
            new_letter = ciper_art.alphabets[new_position]
            final_text += new_letter
        else:
            final_text += letter
    print(f"The {choice} message is: {final_text}")

resume = True
while resume == True:
    direction = input("Enter 'Encode' to encript and 'Decode' to decript.\n").lower()
    text = input("Enter your message:\n").lower()
    shift = int(input("Enter the shift amount:\n"))
    if (shift > 26):
        shift = shift%26
    cypher(message=text, shift_number=shift, choice=direction)
    again = input("Do you want to continue?\nType 'Yes' to continue or 'No' to exit\n").lower()
    if again == 'no':
        resume = False
        print("Thanks. Goodbye")