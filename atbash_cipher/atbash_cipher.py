


def get_message():
    message = input("please enter a message: ")
    return message


def encoding(message):
    txt = ""
    for word in message:
        if word.isalpha():
            if word.isupper():
                txt += chr(155 - ord(word))
            else:
                txt += chr(219 -  ord(word))
        else:
            txt += word
    return txt


def write_to_file(message):
    with open("secret.txt", "a") as f:
        f.write(message)
    return message

def print_original_message(encript):
    txt = ""
    for word in encript:
        if word.isalpha():
            if word.isupper():
                txt += chr(155 - ord(word))
            else:
                txt += chr(219 - ord(word))
        else:
            txt += word
    print(txt)

