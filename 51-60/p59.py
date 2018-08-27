from itertools import product

def encrypt(message, secret_key):
    key_len = len(secret_key)
    message = [
        ord(char) ^ ord(secret_key[i % key_len])
        for i, char in enumerate(message)
    ]
    message = ''.join([chr(x) for x in message])
    return message

def decrypt(message, secret_key):
    return encrypt(message, secret_key)





with open("p059_cipher.txt", "r") as cipher_file:
    cipher = ''.join([chr(int(x)) for x in cipher_file.read().split(",")])

s_keys = product([chr(i) for i in range(97, 123)], repeat=3)
decrypted_messages = [decrypt(cipher, key) for key in s_keys]

message = decrypted_messages[0]
message_len = len(message)
candidates = []

#I'm just kind of guessing below, and looking for decreptyed messages that
#might be the actual one. There's no specific reason why looking for these substrings
#actually catches the right answer, but I just tried a few different english words
#to look for.

for message in decrypted_messages:
    if message.count(' an') and message.count(' is'):
        candidates.append(message)
        print(message)


#if you look at the messages as the print out above you'll see that
#the answer is candidates[2]

print(candidates[2])
print(sum(ord(x) for x in candidates[2]))