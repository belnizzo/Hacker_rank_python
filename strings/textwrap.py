"""Textwrap

The textwrap module provides two convenient functions: wrap() and fill().

textwrap.wrap()
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most.
It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 

textwrap.fill()
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.

Task

You are given a string and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .


Output Format

Print the text wrapped paragraph.

Sample Input

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ  
"""
import textwrap


def wrap(string, max_width):
    ans = textwrap.fill(string,max_width)
    return ans


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)