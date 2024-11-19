import struct  
import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

def decode_morse(morse_code):
    words = morse_code.split('   ')
    decoded_message = []

    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '') for letter in letters)
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    data = s.recv(1024)
    print(data)

    s.send(b'levelx11')

    data2 = s.recv(1024)
    print(data2)
    data3 = data2.decode()
    data4 = decode_morse(data3)

    s.send(data4.encode())
    data5 = s.recv(1024)
    print(data5)
