# https://www.w3schools.com/python/python_file_write.asp

# a = append
# w = write
# r = read
# x = create, or error if already exists

# (NOTE: you can only use one at a time!)

def write(file_name, text):
    f = open(file_name, "w")
    f.write(text)
    f.close()


def read(file_name):
    f = open(file_name, "r")
    print(f.read())


if __name__ == '__main__':
    f = open("write_file_demo.txt", "w")
    f.write("Some content (replaces any existing).")
    f.close()

    f = open("write_file_demo.txt", "r")
    print(f.read())
