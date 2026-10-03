alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         i = alphabet.index(letter) + shift_amount
#
#         i = i % len(alphabet)
#         encrypted_text += alphabet[i]
#     print(f"Here is the encrypted text {encrypted_text}")
#
#
# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for letter in original_text:
#         i = alphabet.index(letter) - shift_amount
#         i = i % len(alphabet)
#         decrypted_text += alphabet[i]
#     print(decrypted_text)

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            i = alphabet.index(letter) + shift_amount
            i = i % len(alphabet)
            output_text += alphabet[i]

    print(f"here is the {encode_or_decode}d result : {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)

    user_choice = input("Type 'yes' if you want to continue otherwise type 'No'\n").lower()
    if user_choice == "no":
        should_continue = False

