
integer = int(input("Enter an integer: " ) )

for i in range(4):
    remainder = integer % 10
    print(int(remainder))
    integer -= remainder
    integer /= 10
