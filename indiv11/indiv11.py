#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from add_person import add_person
from list_people import list_people
from select_people import select_people
from show_help import show_help


def main():
    """
    Терминал.
    """
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            add_person(people)
        elif command == 'list':
            list_people(people)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            month = int(parts[1])
            select_people(people, month)
        elif command == 'help':
            show_help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
