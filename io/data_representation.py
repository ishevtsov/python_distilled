# Specify a bytes literal (note the b' prefix)
a = b'hello'

# Specify bytes from a list of integers
b = bytes([0x68, 0x65, 0x6c, 0x6c, 0x6f])

# Create and populate a bytearray from parts
c = bytearray()
c.extend(b'world')  # c = bytearray(b'world')
c.append(0x21)      # c = bytearray(b'world!')

# Access byte value
print(a[0])

for x in b:
	print(x)