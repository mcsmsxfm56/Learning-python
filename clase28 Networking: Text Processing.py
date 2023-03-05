print(ord('H'))#72
print(ord('e'))#101
print(ord('\n'))#10
#ord tells the value in the UNICODE dictionary
#UNICODE has 140k+ characters, so if we set it across the network
#it would be to large, so we use smallers versions like
#to represent the wide range of characters computers must handle we represent characters
#with more than one byte
#UTF-16 Fixed length Two bytes
#UTF-32 Fixed length Four bytes
#UTF-8 [1-4] bytes (dinamyc length)
##UTF-8 Upwards compatible with ASCII (if it is 1 byte long like ASCII)
##Automatic detection between ASCII and UTF-8
##UTF-8 is recommended practice for encoding data to be exchanged between systems


#python v2 uses ASCII strings as a default and the UNICODE are storaged in the UNICODE class (type str for ascii and type UNICODE for unicode)
#in python v3 all strings are UNICODE (class str for ALL)

#python v3 has the class bytes, bytes are an array of bytes
x = b'abc'
print(x)
print(type(x))

#when we talk to external resource like a network socket we sends bytes, so we need to encode python 3 strings into a given character encoding
#when we read data from external resource, we must decode it based on the character set so it is properly represented in python 3 as a string
