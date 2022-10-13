
def isbn13(isbn):
    if len(isbn) == 10:
        return  convert_isbn_10_to_13(isbn)
    if len(isbn) == 13:
        return validate_isbn_13(isbn)
    else:
        print("Incorrect ISBN length, try again")


# Validate ISBN 10
def validate_isbn_10(isbn):
    isbn_sum = 0
    for index in range(9):
    
        isbn_sum += int(isbn[index])*(10 - index)

    if isbn[-1] == "x" or isbn[-1] == "X":
        isbn_sum += 10
    else:
        isbn_sum += int(isbn[-1])

    return (isbn_sum % 11 == 0)

# Validate ISBN 13
def validate_isbn_13(isbn):
    isbn_sum = 0
    for index in range(13):

        if index % 2 != 0:
            isbn_sum += int(isbn[index])*3
        else:
            isbn_sum += int(isbn[index])

    return (isbn_sum % 10 == 0)

# Covert ISBN 10 to ISBN 13
def convert_isbn_10_to_13(isbn):
    
    if validate_isbn_10(isbn):
        isbn_13 = str("978" + isbn)

        last = 0
        if isbn_13[-1] == "x" or isbn_13[-1] == "X":
            isbn_13 = isbn_13.replace(isbn_13[-1], "0")
        last = int(isbn_13[-1])

        for _ in range(10):
            if not validate_isbn_13(isbn_13):                   #   if the current ISBN 13 is not valid
                isbn_13 = isbn_13[:-1:]                         #   remove the last digit
                
                isbn_13 = isbn_13 + str(last)
                last+=1                                       
                if last == 10:
                    last = 0
                

        print(isbn_13)
        return validate_isbn_13(isbn_13)

    else:
        return validate_isbn_10(isbn)
    

isbn = input("Enter ISBN number: ")

if isbn13(isbn):
    print("Valid")
else:
    print("Invalid")
