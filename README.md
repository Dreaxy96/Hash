# Hash
This Python tool allows users to generate text hashes using algorithms like MD5, SHA-1, SHA-256, and SHA-512. It also enables hash cracking by using a provided wordlist file to attempt to match and crack the given hash.

# Network Hash Cracker

This Python tool allows you to generate hashes for any given text using popular hashing algorithms (MD5, SHA-1, SHA-256, SHA-512). It also provides functionality to crack hashes by using a wordlist to attempt to find the original text from the hash.

## Features
- Generate hashes using MD5, SHA-1, SHA-256, and SHA-512 algorithms.
- Crack a given hash using a wordlist.
- Supports both hash generation and hash cracking functionality in one script.

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/YourUsername/Hash-Cracker.git
    cd Hash-Cracker
    ```

2. Install required libraries (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Generate a Hash:**
   - Choose option `1` to generate a hash for any given text.
   - The program will provide the generated hashes for MD5, SHA-1, SHA-256, and SHA-512.

2. **Crack a Hash:**
   - Choose option `2` to crack a hash.
   - Provide the hash, the algorithm used, and the path to your wordlist file.
   - The program will attempt to match the hash using the wordlist provided.

Example of usage:

```bash
python Hash.py
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

