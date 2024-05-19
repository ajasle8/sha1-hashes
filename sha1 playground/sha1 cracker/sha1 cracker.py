import hashlib

def crack_sha1_hash(hash_to_crack, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash_to_crack:
                return f"Password found: {password}"
    return "Password not found in the dictionary."

if __name__ == "__main__":
    hash_to_crack = input("Enter the SHA1 hash to crack: ").strip()
    dictionary_file = "passwords.txt"  # Using a file named "passwords.txt"

    result = crack_sha1_hash(hash_to_crack, dictionary_file)
    print(result)

a = int(input('click enter: '))
