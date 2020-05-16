def encrypt():
    filename = input("Please enter file name: ")
    password = input("Please enter password: ")
    with open(filename, "rb") as f:
        stuff = list(f.read())
        bin_pos = 0
        pass_pos = 0
        while bin_pos < len(stuff):
            char_int = ord(password[pass_pos])
            pass_pos += 1
            if pass_pos == len(password):
                pass_pos = 0 
            stuff[bin_pos] = (stuff[bin_pos] + char_int)%256
            bin_pos += 1
        with open(filename, "wb") as fb:
            fb.write(bytearray(stuff))
            print("File encrypted successfully!")

def decrypt():
    filename = input("Please enter file name: ")
    password = input("Please enter password: ")
    with open(filename, "rb") as f:
        stuff = list(f.read())
        bin_pos = 0
        pass_pos = 0
        while bin_pos < len(stuff):
            char_int = ord(password[pass_pos])
            pass_pos += 1
            if pass_pos == len(password):
                pass_pos = 0 
            stuff[bin_pos] = (stuff[bin_pos] - char_int)%256
            bin_pos += 1
        with open(filename, "wb") as fb:
            fb.write(bytearray(stuff))
            print("File decrypted successfully!")

def main():
    choice = input("What do you want to do?\n1+ENTER: Encrypt a file\n2+ENTER: Decrypt a file\nENTER: Exit\n")
    if choice == "1":
        encrypt()
        main()
    elif choice == "2":
        decrypt()
        main()

main()
