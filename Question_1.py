n = int(input("Enter number of rows: "))
print()
def upper_rows (number, spaces = 0) :
    if number > 0 :
        print ("* " * number + " " * spaces + "* " * (number))
        upper_rows (number - 1, spaces + 2 * 2)
    else :
        return

def lower_rows (number, spaces = n * 2 + (n - 4) * 2):
    if number < n + 1:
        print ("* " * number + " " * spaces + "* " * (number))
        lower_rows (number + 1, spaces - (2 * 2))
    else :
        return print()

upper_rows(n)
lower_rows(2)