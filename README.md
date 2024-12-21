# URL Discovery Script

This Python script is a tool for discovering potential URLs or directories within a target domain. It uses a wordlist to brute-force possible paths and checks for valid responses. This can be useful for web security testing or enumerating public directories.

## Features
- Sends HTTP GET requests to test URLs.
- Uses a wordlist file to generate potential paths.
- Displays discovered URLs with successful responses.

## Requirements
- Python 3
- The `requests` library (install it with `pip install requests`)
- A wordlist file containing potential directory or file names

## How to Use
1. Clone this repository or copy the script to your local machine.
2. Ensure you have a wordlist file ready (e.g., `common.txt`).
3. Run the script with the following parameters:

### Example Usage
```python
python url_discovery.py
```

- The script assumes the wordlist is located at `/root/Downloads/common.txt`. Adjust the path if necessary.

## Code Overview
1. **Target URL:**
   - Replace `target_URL` with the domain you want to scan (e.g., `www.example.com`).
2. **Wordlist File:**
   - Ensure the wordlist file path in the script matches the location of your wordlist.

### Example
```python
target_URL = "www.example.com/"
wordlist_file_path = "/root/Downloads/common.txt"
```

## Output
- Discovered URLs with successful HTTP responses are printed in the terminal.

### Example Output
```plaintext
[+] Discovered URL --> http://www.example.com/admin
[+] Discovered URL --> http://www.example.com/login
```

## Limitations
- Requires an internet connection to function.
- Only works with HTTP requests (can be modified for HTTPS).
- Limited by the quality and coverage of the wordlist.

## Disclaimer
This script is intended for educational and legal purposes only. Unauthorized scanning or enumeration of websites is illegal and unethical. Use this tool only on domains you own or have explicit permission to test.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

