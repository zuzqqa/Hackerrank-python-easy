if __name__ == '__main__':
    N = int(input())
    result = list() # empty list
    
    for x in range(0, N):
        cmd = input()
        cmd = cmd.split(" ")
        if cmd[0] == "append":
            result.append(int(cmd[1]))
        elif cmd[0] == "insert":
            result.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove":
            result.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            result.sort()
        elif cmd[0] == "pop":
            result.pop()
        elif cmd[0] == "reverse":
            result.reverse()
        elif cmd[0] == "print":
            print(result)
