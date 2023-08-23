

def encode(strs):
    # write your code here
    encoded_string = ":;".join(strs)
    return encoded_string


def decode(str):
    # write your code here
    decoded_list = []
    while str and str.find(":;") != -1:
        index = str.find(":;")
        string = str[:index]
        str = str[index+2:]
        decoded_list.append(string)
    if str:
        decoded_list.append(str)
    return decoded_list


if __name__ == "__main__":
    encoded_string = encode(["lint","code","love","you"])
    print(encoded_string)
    print(encoded_string.index(":;"))
    print(decode(encoded_string))