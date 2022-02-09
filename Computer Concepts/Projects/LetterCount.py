def count(s, ch):
    count = 0
    for i in range(len(s)):
        if s[i] == ch:
            count += 1
    return count

s = input("Enter a string: ")
ch = input("Enter a character: ")

print(ch + " appears in " + s + " " + str(count(s, ch)) + " times")