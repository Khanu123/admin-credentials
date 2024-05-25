# config.py
import os

class Config:
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL', 'default-database-url')
        self.api_key = os.getenv('API_KEY', 'default-api-key')

    def get_database_url(self):
        return self.database_url

    def get_api_key(self):
        return self.api_key

if __name__ == "__main__":
    config = Config()
    print("Database URL:", config.get_database_url())
    print("API Key:", config.get_api_key())
