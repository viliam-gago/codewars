def encode(st):
    encode_dict = {key:value for key, value in zip('aeiou', ('12345'))}
    return ' '.join([''.join([encode_dict[char] if char in encode_dict else char for char in word]) for word in st.split(' ')])

def decode(st):
    decode_dict = {key: value for key, value in zip(('12345'), 'aeiou')}
    return ' '.join([''.join([decode_dict[char] if char in decode_dict else char for char in word]) for word in st.split(' ')])

print(encode('How are you today?'))
print(encode('This is an encoding test.'))
print(decode('h2ll4'))