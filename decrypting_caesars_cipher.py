import string 
# Note: this decryption function is designed to decrypt messages encrypted by encryption function i wrote(avaliable in this repo)

def concat_elements(n):
    res = ""
    for i in n:
        res += i 
    return res


def decrypt(message, key):
    string_chars = list(string.ascii_uppercase) + list(string.ascii_lowercase) +  list(string.digits) + list(string.punctuation) + [" "]
    try:
        splitted_message = list(message)
    except TypeError:
        return "Expected an string for text!"
        
    for char in splitted_message:
        try:
            tmp = string_chars[string_chars.index(char) - key]
        except IndexError:
            tmp_key = (string_chars.index(char) + key) +  len(string_chars)
            tmp = string_chars[tmp_key]
        splitted_message[splitted_message.index(char)] = tmp
        
    final = concat_elements(splitted_message)
    return final 
    

def decrypt_generator(message, n):
    # range(0, 96) because len(string_chars) == 95
    for i in range(0, n + 1):
        case = decrypt(message, i)
        yield case 
# Changed By Remoted example python

# Test 
test_case = "lq01Ir1I2xyI1ncrn2*"
result = decrypt(test_case, 9)
print("Decrypted Text: " + result, "\n")

_result = list(decrypt_generator(test_case, 95))
for res in _result:
    print("Possible text: " + res)
# Look at ninth result
