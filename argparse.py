# -*- coding: utf-8 -*-


from pyfiglet import Figlet

import sys
import os
import argparse
import time

applicationName = 'APK Obfuscator'
versionName = ' APK Obfuscator v1.0.0 '
example = 'example : python apk_obfuscator.py -i absolute_input.apk -o absolute_obfuscated.apk'


def main(argv):
    result = Figlet(font='slant')
    print(result.renderText(applicationName))
    print(f'{"=" * 40}\n{versionName:=^40}\n{"=" * 40}\n')
    time.sleep(0.01)
    arg_parser = argparse.ArgumentParser(description=versionName, epilog=example)
    arg_parser.add_argument('-i', metavar='target_apk', required=True, help='obfuscate target apk path')
    arg_parser.add_argument('-o', metavar='obfuscated_apk', required=True, help='obfuscated output apk path')
    args = arg_parser.parse_args()

    print('i : ' + args.i)
    print('b : ' + args.o)


if __name__ == '__main__':
    main(sys.argv)
