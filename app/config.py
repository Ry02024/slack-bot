import os

class Config:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "your-slack-bot-token")
    SLACK_TEST_CHANNEL = os.getenv("SLACK_TEST_CHANNEL", "your-slack-test-channel-id")
