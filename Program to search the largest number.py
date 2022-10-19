print("Find the maximum number from the list")
def max() -> int:
    a = 0
    for n in range(10):
        var = int(input("Enter the number :"))
        if var > a:
            a = var
    return a
print("Largest no is: ", max())
