#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_replacer(replace_char):
    def replace_duplicates(string):
        new_string = ""
        previous_char = ""
        for char in string:
            if char != previous_char:
                new_string += char
            else:
                new_string += replace_char
            previous_char = char
        return new_string

    return replace_duplicates


def main():
    inp = input("Введите слово с повторяющимися буквами: ")
    repl_dup = create_replacer(
        input("Введите символ для замены повторяющихся букв: "))
    print(repl_dup(inp))


if __name__ == '__main__':
    main()
