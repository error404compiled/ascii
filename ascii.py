n = list(map(int, input("Enter Ascii Value : ").split()))
res = "".join(chr(var) for var in n)
print(str(res))