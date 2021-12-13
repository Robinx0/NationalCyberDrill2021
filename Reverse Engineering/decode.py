import base64, binascii

encoded_string = input('Encoded Strings Here: ')


decode_string=binascii.unhexlify(encoded_string)

ascii_string=bytearray(decode_string)
ascii_string.reverse()

decode_string=list(ascii_string)

ascii_arr=[]
a = int(len(encoded_string)/2)

for i in range(0,a):
	if (i == 0):
		ascii_arr.append(decode_string[i] ^ 85)
	else:
		ascii_arr.append(ascii_arr[i-1] ^ decode_string[i])

ascii_arr.reverse()

flag = (binascii.a2b_base64(bytearray(ascii_arr))).decode('utf-8')
print(f"Here is your flag : {flag}")
