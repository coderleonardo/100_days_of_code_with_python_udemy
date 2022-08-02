
## lesson 01 - Data Types

### String

print("Hello"[0])
# H e l l o
# 0 1 2 3 4
print("Hello"[4])

print("123" + "345")

### Integer

print(123 + 345)
print(123_456_789) # 123,456,789

### Float

print(3.1415)

### Boolean

print(True, False)

## lesson 02

print(type(123))
print( type( str(123) ) ) # convert int to str

a = 123
print(type(a))
print(type(float(a)))
print(type(str(a)))

## lesson 03 - mathematical operators

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3 (type float)
# 2 ** 3 (exponent)

# PEMDAS
# ()
# **
# * /
# + -

## lesson 04

print(round(8 / 3, 2))
print(round(2.666666666666666666666666666, 2))
print(type(8 // 3))

result = 4 / 2
result /= 2
print("result: " + str(result))
### f-string
print(f"result: {result}")