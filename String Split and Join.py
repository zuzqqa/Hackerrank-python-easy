def split_and_join(line):
    line = line.split(" ") #line is converted to a list of strings
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
