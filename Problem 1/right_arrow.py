def right_arrow():
   
    ''' Type your code here. '''

    base = input("")
    head = input("")

    row1 = ('      ' + head)
    row2 = (base + base + base + base + base + base + head)
    row3 = (base + base + base + base + base + base + head + head + head)

    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()