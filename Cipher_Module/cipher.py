def encrypt(message, file):
    """Encrypts a message by reversing the bits of each byte in the message
        and then performing a bitwise xor operation with corresponding bytes in the file.

    Parameters
    ----------
    message : string
        String to encrypt with file.
    file : string
        String to encrypt message with.

    Returns
    -------
    encrypted_message : string
        String containing the encrypted message.
    """

    # check if file is large enough to perform encryption
    if len(message) > len(file):
        raise Exception("Size of the used file must be as least as large as the message!")

    encrypted_message = ""

    for char, key in zip(message, file):
        # get unicode value of char and key
        char_unicode = ord(char)
        key_unicode = ord(key)

        # convert the int value of char to an 8 bit binary value and reverse the order of the bits
        char_binary = format(char_unicode, '08b')[::-1]

        # xor char and key to perform encryption
        encrypted_value = int(char_binary, 2) ^ key_unicode

        # add encrypted char to the encrypted message
        encrypted_message = encrypted_message + chr(encrypted_value)

    return encrypted_message


def decrypt(encrypted_message, file):
    """Decrypts an encrypted message by performing a bitwise xor operation with corresponding bytes in the file
        and then reversing the bits of this byte.

    Parameters
    ----------
    encrypted_message : string
        String to decrypt with file.
    file : string
        String to decrypt encrypted message with.

    Returns
    -------
    decrypted_message : string
        String containing the decrypted message.
    """

    # check if file is large enough to perform deryption
    if len(encrypted_message) > len(file):
        raise Exception("Size of the used file must be as least as large as the message!")

    decrypted_message = ""

    for char, key in zip(encrypted_message, file):
        # get unicode value of char and key
        char_unicode = ord(char)
        key_unicode = ord(key)

        # xor char and key first to decrypt
        decrypted_value = char_unicode ^ key_unicode

        # lastly reverse the bitorder of the decrypted value to obtain original message
        old_message = format(decrypted_value, '08b')[::-1]

        # add char value of the decrypted value to the decrypted message
        decrypted_message = decrypted_message + chr(int(old_message, 2))

    return decrypted_message


def get_message(mode):
    """Reads in a users input.

    Parameters
    ----------
    mode : String
        String containing the mode indicating whether encryption or
        decryption is to be performed.

    Returns
    -------
    message : string
        String containing the message.
    """

    message = ""

    if mode == "e":
        message = input("Please enter the message you want to encrypt! ")

    elif mode == "d":
        message = input("Please enter the message you want to decrypt! ")

    # check for empty message
    if len(message) <= 0:
        raise Exception("Message cannot be empty!")
    else:
        return message


def get_filepath():
    """Reads in the filepath to a file provided by the user.

    Parameters
    ----------
    None

    Returns
    -------
    filepath : string
        String containing the filepath.
    """

    filepath = input("Please provide a file to use as a key! ")

    if len(filepath) <= 0:
        raise Exception("Filepath cannot be empty!")
    # making sure that user only reads in txt file
    elif filepath[-4:] != ".txt":
        raise Exception("File must be a .txt file!")
    else:
        return filepath


def read_txt(filepath, size):
    """Reads size bytes of the contents of a txt file passed as a filepath.

    Parameters
    ----------
    filepath : string
        String containing the absolute filepath of the txt file.
    size : integer
        Number of bytes to be read from txt file.

    Returns
    -------
    text : string
        String containing size bytes of the txt file.
    """

    # open the txt file
    file = open(filepath, "r")

    # read size bytes from file
    text = file.read(size)

    # raise error if the used file is too small to encrypt whole message
    if size > len(text):
        raise Exception("Size of the used file must be as least as large as the message!")
    else:
        # close txt file
        file.close()
        return text
