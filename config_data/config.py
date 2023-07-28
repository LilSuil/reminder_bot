from pydantic import SecretStr
from dataclasses import dataclass
from environs import Env
from typing import Any

@dataclass
class Config:
    bot_token: SecretStr
    admins: set

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot_token=SecretStr(env('ReminderBotToken')), admins={928730667})



