'''# Ez az első módosítás

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('VM')
'''

import p022

a = 10
b = 26

eredmeny = p022.negyszog(a, b)
print (f"A {eredmeny[2]} kerület =", eredmeny[0])
print (f"A {eredmeny[2]} terület =", eredmeny[1])
