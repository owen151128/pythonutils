# -*- coding::utf-8 -*-

from pyfiglet import Figlet

import time
import argparse

class Constants:
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ValueError('Constants can\'t be re-assigned!')
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            raise ValueError('Constants can\' be removed!')


class EntryDescription:
    def __init__(self, application_name, version_name, example_message):
        self.application_name = application_name
        self.version_name = f' {application_name} {version_name} '
        self.example_message = f'example : python {__file__} {example_message}'

    def print_entry_description(self):
        result = Figlet(font='slant')
        print(result.renderText(self.application_name))
        print(f'{"=" * 80}\n{self.version_name:=^80}\n{"=" * 80}\n')
        time.sleep(0.01)


def main():
    entry_description = EntryDescription('Apks to Apk', 'v0.0.1', '-i absolute_apks_dir -o absolute_path.apk')
    entry_description.print_entry_description()

    arg_parser = argparse.ArgumentParser(description=entry_description.version_name, epilog=entry_description.example_message)
    arg_parser.add_argument('-i', metavar='absolute_apks_dir', required=True, help='apks dir path')
    arg_parser.add_argument('-o', metavar='merge_apk_path', required=True, help='merge apk path')
    args = arg_parser.parse_args()

    print('i : ' + args.i)
    print('b : ' + args.o)


if __name__ == '__main__':
    main()
