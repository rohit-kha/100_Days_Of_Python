# #8.1
# #greet function
# def greet():
#     print("Hello")
#     print("Mr.")
#     print("Rohit")

# greet()

# # parameters
# def greet(name):
#     print("Hello")
#     print("Mr.")
#     print(f"{name}")

# greet("Rohit")

# #8.2.
# # multiple parameters

# def greet(name, location):
#     print("Hello")
#     print("Mr.")
#     print(f"{name}")
#     print(f"Do you live in {location}?")


# greet("Rohit","Sarlahi")

# #8.2
# #paint calculator
# import math

# def paint_cal(h,w,c):
#     no_of_cans = (h*w)/c
#     no_of_cans = math.ceil(no_of_cans)
#     print(f"The number of cans needed to paint this wall is {no_of_cans}")

# he = int(input("Enter height: "))
# wi = int(input("Enter width: "))
# co = int(input("Enter coverage: "))


# paint_cal(he,wi,co)

# #8.4
# #Prime number checker 

# def prime_checker(num):
#     is_prime = True
#     for i in range(2,num,-1):
#         if num % i == 0:
#             is_prime = False
            
#     if is_prime:
#         print("It is a prime number ")
#     else:
#         print("It is not a prime number")

# # number = int(input("Enter the number to be tested: "))
# prime_checker(8)

#8.5
#caeser cipher
print("???????????????????????????")
print("CAESER CIPHER")
print("?????????????????????????????")
print()
print()
print()
      

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25
    

    def ceaser (start_text, a_shift, cipher_direction):
      end_text =""
      if cipher_direction == "decode":
        a_shift *= -1
      for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + a_shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    # for letter in start_text:
    #     position = alphabet.index(letter)
    #     if cipher_direction == "decode":
    #        new_position = position - a_shift
    #     else:
    #         new_position = position + a_shift
    #     if letter in alphabet:
    #       end_text += alphabet[new_position]
    #     else:
    #        end_text += letter
      print(f"the {cipher_direction} text is {end_text}")  


    ceaser(start_text=text,a_shift=shift,cipher_direction=direction)

    # result = input("Do you still want to continue encoding or decoding?").lower
    # if result == "no": 
    #    should_continue = False
    #    print("goodbye")
     




# def encrypt (p_text,a_shift):
#     cipher_text = ""
#     for letter in p_text:
#         position = alphabet.index(letter)
#         new_position = position + a_shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, a_shift):
#     p_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - a_shift
#         new_letter = alphabet[new_position]
#         p_text += new_letter
#     print(f"The decrypted text is {p_text}")




# if direction == "encode":
#     encrypt(p_text=text,a_shift=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, a_shift=shift)
