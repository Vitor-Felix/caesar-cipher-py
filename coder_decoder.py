#!/usr/bin/env python3

import argparse


def coder(phrase, rotations=3):
    
    coded_phrase = ""

    for letter in phrase:
        if ord(letter) > 96 and ord(letter) < 123: 
            if (ord(letter) + rotations) > 122:
                coded_phrase += chr((ord(letter) + rotations) - 26)
            else:
                coded_phrase += chr(ord(letter) + rotations)
        else:
            coded_phrase += letter

    return coded_phrase


def decoder(phrase, rotations=3):
    
    decoded_phrase = ""

    for letter in phrase:
        if ord(letter) > 96 and ord(letter) < 123: 
            if (ord(letter) - rotations) < 97:
                decoded_phrase += chr((ord(letter) - rotations) + 26)
            else:
                decoded_phrase += chr(ord(letter) - rotations)
        else:
            decoded_phrase += letter

    return decoded_phrase


def main():
    roles = {'code': coder, 'decode': decoder}
    parser = argparse.ArgumentParser(description='Code/Decode a Rot-N Cipher')
    parser.add_argument('role', choices=roles, 
                        help='Choose between code or decode the phrase')
    parser.add_argument('phrase', help='Message to be coded or decoded. Use Quotes!')
    parser.add_argument('-r', '--rotations', default=3, help='Number of shifts.\n' 
                        'Default is the Caesar\'s cipher (Rot-3)')
    args = parser.parse_args()
    function = roles[args.role]

    print('\n', function(args.phrase.lower(), int(args.rotations)), '\n')


if __name__ == '__main__':
    main()