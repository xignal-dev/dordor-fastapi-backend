from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# with open("mykey.key", "wb") as mykey:
#    mykey.write(key)

with open("mykey.key", "rb") as mykey:
    key = mykey.read()

# print(key)


# 파일 암호화
def file_encryption(original_file_name, encryption_file_name):

    f = Fernet(key)

    with open(original_file_name, "rb") as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(encryption_file_name, "wb") as encrypted_file:
        encrypted = encrypted_file.write(encrypted)
        
    print("file_encryption: ", "success")     
    return "success"

# 파일 복호화
def file_decryption(encryption_file_name, decryption_file_name):

    f = Fernet(key)

    with open(encryption_file_name, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(decryption_file_name, "wb") as decrypted_file:
        decrypted = decrypted_file.write(decrypted)

    print("file_decrypted: ", "success")     
    return "success"

# 문자열 암호화
def str_encryption(original_str):

    f = Fernet(key)

    enctex = f.encrypt(original_str.encode())
        
    print("str_encryption: ", "success")     
    return enctex

# 문자열 복호화
def str_decryption(encryption_str):

    f = Fernet(key)

    decrypted = f.decrypt(encryption_str).decode()

    print("str_decryption: ", "success")     
    return decrypted