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


constants: Constants = Constants()


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
    global constants
    constants.APP = 'Trading View BackTest'
    constants.VERSION = 'v0.0.1'
    constants.KEY_OPTION = '-k'
    constants.INPUT_OPTION = '-i'
    constants.KEY_OPTION_META = 'binance_api_keys yaml file path'
    constants.INPUT_OPTION_META = 'Trading view transaction history csv file path'

    entry_description = EntryDescription(constants.APP, constants.VERSION,
                                         f'{constants.KEY_OPTION} [{constants.KEY_OPTION_META}] '
                                         f'{constants.INPUT_OPTION} [{constants.INPUT_OPTION_META}]')
    entry_description.print_entry_description()
    arg_parser = argparse.ArgumentParser(description=entry_description.version_name,
                                         epilog=entry_description.example_message)
    arg_parser.add_argument(constants.KEY_OPTION, metavar=f'[{constants.KEY_OPTION_META}]', required=True,
                            help=constants.KEY_OPTION_META.replace('_', ''))
    arg_parser.add_argument(constants.INPUT_OPTION, metavar=f'[{constants.INPUT_OPTION_META}]', required=True,
                            help=constants.INPUT_OPTION_META.replace('_', ''))
    args = arg_parser.parse_args()

    print('k : ' + args.k)
    print('i : ' + args.i)


if __name__ == '__main__':
    main()
