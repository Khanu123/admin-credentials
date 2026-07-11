import os


def get_secret():
    return os.getenv("SECRET_KEY")


def mask_secret(value):
    if not value:
        return "not configured"
    if len(value) <= 4:
        return "****"
    return f"{value[:2]}{'*' * (len(value) - 4)}{value[-2:]}"


if __name__ == "__main__":
    print("Secret Key:", mask_secret(get_secret()))
