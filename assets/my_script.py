def my_age():
    command = input("""
    What do you want to do?
    > addition: +
    > subtraction: -
    > multiplication: *
    > division: /
    """)
    first = input("Enter your birth date: ")
    new_first = int(first)
    second = input("With what date")
    new_second = int(second)
    
    if command == '+':
        print(new_first + new_second)
my_age()