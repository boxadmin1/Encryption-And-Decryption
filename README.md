# Multi-Layer Custom Encryption & Decryption in Pure Python
*Created by Boxadmin1*

This repository contains a pure Python implementation of a multi-layer encryption and decryption algorithm. The program uses a combination of classical and custom techniques to provide a more complex cipher than basic methods, while remaining fully self-contained and requiring **no external dependencies** or imports.

---

## Features

- **Multi-layer encryption** combining:
  - Vigenère cipher (byte-wise, mod 256)
  - XOR encryption with the key
  - Key-dependent pseudo shuffle/unshuffle
  - Manual Base64 encoding/decoding (no `base64` module)

- **Pure Python implementation** with no imports — runs in any standard Python 3 environment (tested with Python 3.5+).

- **Interactive command-line interface** allowing you to:
  - Encrypt plaintext with a user-provided key
  - Decrypt ciphertext with a user-provided key
  - Quit gracefully

- Handles all byte values by encoding intermediate steps in `latin1` encoding.

---

## Intended Use

This project is **developed for educational purposes only** and should be used solely as a learning tool to understand encryption concepts and programming techniques. It **is not secure** and should **never be used to protect real sensitive data**.

---

## Usage

Run the script in a Python 3 environment:

```bash
python encryption.py
