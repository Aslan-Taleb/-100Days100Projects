import pygame
import pyperclip

UNIT_OF_TIME = 0.2
LOGO = """
            ____
  |        | ___\          /~~~|
 _:_______|/'(..)`\_______/  | |
<_|``````  \__~~__/ AslaN ___|_|
  :\_____(=========,(*),--\__|_/
  |       \       /---'
           | (*) /
           |____/
          """

morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '!': '-.-.--',
    '"': '.-..-.',
    '#': '-..-.',
    '$': '...-..-',
    '%': '--..-.',
    '&': '.-...',
    '\'': '.----.',
    '(': '-.--.',
    ')': '-.--.-',
    '*': '-..-',
    '+': '.-.-.',
    ',': '--..--',
    '-': '-....-',
    '.': '.-.-.-',
    '/': '-..-.',
    ':': '---...',
    ';': '-.-.-.',
    '<': '.-...',
    '=': '-...-',
    '>': '-.-.--',
    '?': '..--..',
    '@': '.--.-.',
    '[': '-.--.',
    '\\': '-..-.',
    ']': '-.--.-',
    '^': '..--.-',
    '_': '..--.-',
    '`': '.----.',
    '{': '-.--.',
    '|': '-.--.-',
    '}': '-.--.-',
    '~': '.-..-.',
    ' ': '/'
}


def display_menu():
    print("Enter the conversion direction:\n")
    print("[1] Text to Morse code")
    print("[2] Morse code to Text")
    print("[3] Quit\n")


def get_input(message):
    return input(message).strip().lower()


def encode(text):
    """
    This Function take a Text and encode it to Morse
    :param a regular text:
    :return: a Morse Text:
    """
    encoded = []
    for word in text.split():
        for letter in word:
            if letter in morse_dict.keys():
                encoded += morse_dict[letter] + ' '
        encoded += '/'
    encoded = ''.join(encoded)
    if len(encoded) == 0:
        return "#"
    return encoded if encoded else "#"


def decode(morse):
    """
    This Function take a Morse Code and decode it to Regular Text
    :param a code morse:
    :return: a regular text:
    """
    decoded = []
    for symbol in morse.split():
        for key, value in morse_dict.items():
            if symbol == value:
                decoded += key
    decoded = ''.join(decoded).title()
    return decoded if decoded else "#"


def play_morse_code(morse):
    pygame.mixer.init()
    dot_sound = pygame.mixer.Sound("sounds/dot.mp3")
    dash_sound = pygame.mixer.Sound("sounds/dash.mp3")

    for symbol in morse:
        if symbol == '.':
            dot_sound.play()
            pygame.time.wait(int(0.2 * 1000))
        elif symbol == '-':
            dash_sound.play()
            pygame.time.wait(int(0.2 * 1000))
        elif symbol == ' ':
            pygame.time.wait(int(2 * 0.2 * 1000))
        elif symbol == '/':
            pygame.time.wait(int(3 * 0.2 * 1000))



