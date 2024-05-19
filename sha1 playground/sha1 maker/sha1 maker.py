
import hashlib

def generate_sha1_hash(text):
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    return sha1_hash

if __name__ == "__main__":
    text_to_hash = input("Enter the text to hash: ").strip()
    hashed_text = generate_sha1_hash(text_to_hash)

    with open("passwords.txt", "a") as file:
        file.write(f"{hashed_text}\n")
        file.write(f"{text_to_hash}\n")

    print("SHA1 Hash:", hashed_text)

a = int(input('done: '))
