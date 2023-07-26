from pydantic import SecretStr
from dataclasses import dataclass
from environs import Env
@dataclass
class Config:
    bot_token: SecretStr

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot_token=SecretStr(env('ReminderBotToken')))



