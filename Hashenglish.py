import hashlib

def generate_hashes(data):
    algorithms = {
        "MD5": hashlib.md5,
        "SHA-1": hashlib.sha1,
        "SHA-256": hashlib.sha256,
        "SHA-512": hashlib.sha512
    }
    
    hash_results = {}
    for name, func in algorithms.items():
        hash_results[name] = func(data.encode()).hexdigest()
    return hash_results

def crack_hash(hash_to_crack, algorithm, wordlist):
    if algorithm not in hashlib.algorithms_guaranteed:
        return "Unsupported algorithm."
    
    try:
        with open(wordlist, 'r') as file:
            for word in file:
                word = word.strip()
                hashed_word = hashlib.new(algorithm, word.encode()).hexdigest()
                if hashed_word == hash_to_crack:
                    return f"Hash cracked: {word}"
    except FileNotFoundError:
        return "Wordlist file not found."
    
    return "Hash not found in the wordlist."

def main():
    print("Hash Tool")
    print("1. Generate hash")
    print("2. Crack hash")
    
    choice = input("Please make a selection (1/2): ")
    
    if choice == "1":
        user_input = input("Enter the text you want to hash: ")
        
        if not user_input.strip():
            print("Please enter a valid text.")
            return
        
        print("\nHash results:")
        hashes = generate_hashes(user_input)
        for algorithm, hash_value in hashes.items():
            print(f"{algorithm}: {hash_value}")
    
    elif choice == "2":
        hash_to_crack = input("Enter the hash to crack: ")
        algorithm = input("Choose hash algorithm (MD5, SHA-1, SHA-256, SHA-512): ").upper()
        wordlist = input("Enter the path to the wordlist file (e.g., wordlist.txt): ")
        
        print("\nCracking process starting...")
        result = crack_hash(hash_to_crack, algorithm, wordlist)
        print(result)
    
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
