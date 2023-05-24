# Book Cipher Variation

This project implements a variation of the traditional book cipher. 

**How the cipher itself works**

The book cipher itself takes a message and encrypts each char in the message with a corresponding char in the book. My version of the book cipher uses encryption on bit level. I take advantage of the self inverse property of the bitwise xor operation to encrypt each byte of the message with a correspnding byte of the book. 
For example, when we xor the message "A" (01000001 in 8bit binary) with the key "t" (01110100 in 8bit binary), we get the char "5" (0110101 in 8bit binary). When we now take the encrypted message "5" and perform a bitwise xor with the same key ("t") as used for the encryption, we obtain the original message "A". To make the cipher even more complex and safe, I reversed the bits of each byte before encrypting/after decrypting the message. 
All in all, my cipher works as follows: For encryption, take the message byte by byte, reverse the bits of each byte and perform a bitwise xor with a corresponding byte of the book. To decrypt, take the encrypted message byte by byte, perform a bitwise xor with a corresponding byte of the book first, then reverse the bits of each byte to obtain the original message. Thus, a user that wants to decrypt a message must possess the same file that was used for the encryption of the message.

**How the program works**

I implemented the program so that it takes a .txt file as an input for a "book" (key). Thus, the user needs to provide the book or text he wants to use for the cipher in a .txt format. For that, the user enters the path to the file when prompted to do so by the script. It is important that the .txt file has at least as many chars as the message as the program reads exactly the same amount of bytes from the file as there are in the message (starting at the beginning of the file).
The user can perform as many encryptions or decryptions as he wants to.

**Example**

Below one can see the execution of the run_cipher program inside the "Scripts" directory. It calls the function run_cipher(), which implements the control flow and calls all the other functions that contain the logic of the cipher. 
The user is prompted to enter a certain key (on the keyboard) to indicate which option he wants to execute. After a message was entered, the user is asked to provide a filepath to the txt file that should be used as a key. Here, the "Test.txt" file is used as a key and it is located in the project folder.

```python
from Scripts import run_cipher as ciph

ciph.run_cipher()
```
Output: 
```
This is a variation of a book cipher. To use it, enter a message you want to encrypt/decrypt. 
Then provide a .txt file with some text to use as a key (at least as long as your message).
Type 'e' for encryption, 'd' for decryption, and 'q' to quit! r
This is not a valid option!
Type 'e' for encryption, 'd' for decryption, and 'q' to quit! e
Please enter the message you want to encrypt! Hello
Please provide a file to use as a key! ./Test.txt
Your encrypted message is: FÎ_EÖ
Type 'e' for encryption, 'd' for decryption, and 'q' to quit! d
Please enter the message you want to decrypt! FÎ_EÖ
Please provide a file to use as a key! ./Test.txt
Your decrypted message is: Hello
Type 'e' for encryption, 'd' for decryption, and 'q' to quit! q
Cipher closed
