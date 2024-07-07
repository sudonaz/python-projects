#define a function that checks uppercase
def uppercase(password):
    uppercases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for character in password:
        for i in uppercases:    
            if character == i:  #we check if the character in password and i in uppercases are the same
                return True
    return False

#define a function that checks lowercase
def lowercase(password):
    lowercases = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for character in password:
        for i in lowercases:
            if character == i:
                return True
    return False

#define a function that checks special characters
def specialCharacter(password):
    specialCharacters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?"]
    for character in password:
        for i in specialCharacters:
            if character == i:
                return True
    return False

#define a function that checks numbers
def number(password):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for character in password:
        for i in numbers:
            if character == i:    
                return True
    return False

#define a function that checks length of the password
def length(password):
    if 8 <= len(password) <= 16:
        return True
    else:
        return False

#define a function that checks the password is power enough
def pswCheck(password):
    uppc = uppercase(password)
    lowc = lowercase(password)
    spc = specialCharacter(password)
    num = number(password)
    lng = length(password)

    if uppc and lowc and spc and num and lng:
        print("Your password is strong.")
    else:
        print("Your password is not strong enough.")

password = input("Please enter your password: ")
pswCheck(password)
