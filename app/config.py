import os

class Config:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "your-slack-bot-token")
    SLACK_TEST_CHANNEL =["C08BRQGQ2VB"]
