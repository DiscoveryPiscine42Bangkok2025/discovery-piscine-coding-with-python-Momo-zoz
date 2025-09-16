def add_one(x):
    x += 1
    return x

if __name__ == "__main__":
    num = 5
    print("Before calling add_one:", num)
    num = add_one(num)
    print("After calling add_one:", num)
