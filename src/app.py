# app.py
import os

def get_secret():
    return os.getenv('SECRET_KEY')

if __name__ == "__main__":
    print("Secret Key:", get_secret())
