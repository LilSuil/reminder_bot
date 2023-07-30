from pydantic import SecretStr
from dataclasses import dataclass
from environs import Env

@dataclass
class Config:
    bot_token: SecretStr

    admins: set

    pg_db_name: SecretStr
    pg_db_host: SecretStr
    pg_db_password: SecretStr
    pg_db_username: SecretStr


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(bot_token=SecretStr(env('ReminderBotToken')), admins={928730667}, pg_db_host=SecretStr(env('pg_db_host')), pg_db_username=SecretStr(env('pg_db_username')),
                  pg_db_password=SecretStr(env('pg_db_password')), pg_db_name=SecretStr(env('pd_db_name')))



