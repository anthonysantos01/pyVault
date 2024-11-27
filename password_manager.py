import os
from crypto import encrypt_file, decrypt_file, encrypt_password, decrypt_password

def add_password(service, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.vlt", "a") as file:
        file.write(f"{service}:{encrypted_password}\n")
    encrypt_file("passwords.vlt")

def get_password(service):
    if not os.path.exists("passwords.vlt"):
        return None
    else:
        decrypt_file("passwords.vlt")  

        with open("passwords.vlt", "r") as file:
            for line in file.readlines():
                stored_service, encrypted_password = line.strip().split(":")
                if stored_service == service:
                    decrypted_pass= decrypt_password(encrypted_password)
                    encrypt_file("passwords.vlt")
                    return decrypted_pass

def list_services():
     
    if not os.path.exists("passwords.vlt"):
        return None
    else:
        decrypt_file("passwords.vlt") 
        with open("passwords.vlt", "r") as file:
            services = [line.split(":")[0] for line in file.readlines()]
        encrypt_file("passwords.vlt")
        return services

def delete_password(service):
    
    if not os.path.exists("passwords.vlt"):
        return False
    else:
        decrypt_file("passwords.vlt") 
        lines = []
        with open("passwords.vlt", "r") as file:
            lines = file.readlines()
        found = False
        with open("passwords.vlt", "w") as file:
            for line in lines:
                stored_service, _ = line.strip().split(":")
                if stored_service != service:
                    file.write(line)
                else:
                    found = True

    encrypt_file("passwords.vlt")
    return found
