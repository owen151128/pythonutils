# -*- coding::utf-8 -*-

from pyfiglet import Figlet

import time


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


if __name__ == '__main__':
    main()
