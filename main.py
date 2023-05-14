
def getBmi():
    w = float(input("Weight (kg): "))
    h = float(input("Height (m): "))
    return round(w / h ** 2, 2)

def divide() -> object:
    n = float(input("Numerator: "))
    d = float(input("Denominator: "))
    try:
        ans = round(n / d, 2)
        return ans
    except ZeroDivisionError:
        return "Error! You cannot divide by zero because it's illegal in every state but Texas."

if __name__ == '__main__':
    # Part 1
    print("BMI Calculator.")
    print(getBmi())

    # Part 2
    print("Divide Two Numbers.")
    print(divide())

    # Part 3
    print("File IO.")

    write = open("demo.txt", "w")
    write.write('This is the text written to the file.\n')
    write.close()

    read = open("demo.txt", "r")
    print(read.read())
    read.close()

    append = open("demo.txt", "a")
    append.write("This is the new text.\n")
    append.close()

    # Part 4
    print("Product Pricing.")
    products = {"book": 5.60, "food": 18.54, "bike": 249, "computer": 1400, "car": 6899}
    name = input("Name: ")
    if name in products:
        price = products[name]
        print(price)
    else:
        print("This product does not exist in the catalog.")

    # Part 5
    print("Odd Numbers.")
    odd = list()
    for x in range(1, 101):
        if x % 2 != 0:
            odd.append(x)
            print(x)
