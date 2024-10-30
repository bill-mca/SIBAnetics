from random import choice
from time import sleep

def generate_spoof_transcript():
    commands = [ "Bin", "Lay", "Place", "Set"]
    colours = [ "blue", "green", "red", "white"]
    prepositions = ["at", "by", "in", "with"]
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = [str(d) for d in range(10)]
    adverbs = ["again", "now", "please", "soon"]
    return ' '.join([choice(commands), choice(colours), choice(prepositions),
        choice(letters), choice(digits), choice(adverbs)])

if __name__ == '__main__':
    while True:
        with open('audio_transcript.txt', 'w') as file:
            file.write(generate_spoof_transcript())
        with open('lip_reading_transcript.txt', 'w') as file:
            file.write(generate_spoof_transcript())
        print('.')
        sleep(4)
