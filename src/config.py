import os


class Config:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.api_key = os.getenv("API_KEY")

    def get_database_url(self):
        return self.database_url

    def get_api_key(self):
        return self.api_key

    def validate(self):
        missing = []
        if not self.database_url:
            missing.append("DATABASE_URL")
        if not self.api_key:
            missing.append("API_KEY")
        return missing


if __name__ == "__main__":
    config = Config()
    missing_values = config.validate()
    if missing_values:
        print("Missing environment variables:", ", ".join(missing_values))
    else:
        print("Configuration loaded from environment variables.")
