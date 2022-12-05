from Cipher_Module.cipher import encrypt, decrypt, get_message, get_filepath, read_txt


def run_cipher():
    """Runs the cipher program by providing a control flow."""

    print("This is a variation of a book cipher. To use it, enter a message you want to encrypt/decrypt. \n"
          "Then provide a .txt file with some text to use as a key (at least as long as your message).")

    running = True
    while running:

        mode = input("Type 'e' for encryption, 'd' for decryption, and 'q' to quit! ")

        if mode == "e":
            # get input from user
            message_to_encrypt = get_message(mode)
            filepath = get_filepath()

            # read contents from provided file
            key = read_txt(filepath, len(message_to_encrypt))

            # perform encryption
            message_encrypted = encrypt(message_to_encrypt, key)

            print("Your encrypted message is: " + message_encrypted)

        elif mode == "d":
            # get input from user
            message_to_decrypt = get_message(mode)
            filepath = get_filepath()

            # read contents from provided file
            key = read_txt(filepath, len(message_to_decrypt))

            # perform decryption
            message_decrypted = decrypt(message_to_decrypt, key)

            print("Your decrypted message is: " + message_decrypted)

        elif mode == "q":
            print("Cipher closed")
            running = False

        else:
            print("This is not a valid option!")

