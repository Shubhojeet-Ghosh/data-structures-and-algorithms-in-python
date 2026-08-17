def encode(strs) -> str:
    encoded_strs_list = []
    for str in strs:
        new_str_list = []
        for s in str:
            new_ch = chr(ord(s) + 1)
            new_str_list.append(new_ch)

        new_str = "".join(new_str_list)  
        encoded_strs_list.append(new_str)

    return encoded_strs_list

def decode(s: str):
    new_list_str = []
    for ch in s:
        new_ch = chr(ord(ch) - 1)
        new_list_str.append(new_ch)

    decoded_str = "".join(new_list_str)    
    return decoded_str

strs = ["Hello","World"]

encoded_strings = encode(strs)
print(encoded_strings)

print(decode(encoded_strings[0]))