def split_and_join(line):
    line = line.split(" ")
    result= "-".join(line)
    return result

line = input()
result = split_and_join(line)
print(result)