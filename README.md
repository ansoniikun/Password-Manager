# Password Manager

This is a simple password manager built using Python and Tkinter. It allows users to securely store passwords for different services or accounts, with the ability to encrypt and decrypt these passwords using the cryptography library. The passwords are saved locally in a text file in an encrypted format, and the encryption key is securely stored and reused for future sessions.

## Features

> Add new passwords: Store usernames and passwords for different accounts securely.
> Retrieve passwords: Decrypt and retrieve stored passwords for accounts.
> Encryption: All passwords are encrypted using the Fernet encryption method from the cryptography library.
> Local storage: Passwords are stored locally in a text file (passwords.txt), and the encryption key is saved in a separate file (key.key).

## Libraries Used

  Tkinter: A Python library for creating graphical user interfaces (GUIs).
  Cryptography: A Python library used to securely encrypt and decrypt passwords with the Fernet encryption scheme.
  JSON: For saving and loading password data in a structured format from a local text file.

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```

Install required libraries:

```
pip install cryptography
```

Run the program:
```
python3 password_manager.py
```

## How to Use

Add a Password:
>Fill in the Account, Username, and Password fields.
>Click on the Add Password button. The password will be encrypted and stored locally.

Retrieve a Password:
>Enter the account name in the Account field.
>Click on the Get Password button. The program will decrypt and display the username and password for that account.

## Security Disclaimer

This program uses encryption to store your passwords securely, but it is a simple project intended for educational purposes. It does not provide advanced security features like multi-factor authentication (MFA), cloud backups, or real-time threat detection.

Disclaimer: While encryption is used, this program may not provide sufficient protection for sensitive information if used in high-risk environments. Use this password manager at your own discretion, and I hold no liability for any data breaches, loss, or misuse of information caused by the use of this software. It is recommended to use professional-grade password managers for critical and sensitive information.
