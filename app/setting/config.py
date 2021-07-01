from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    BASE_DIR = base_dir
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = 'mysql+pymysql://travis@localhost/fast_api?charset=utf8mb4'


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = True


def conf():
    config = dict(prof= ProdConfig(), loacl= LocalConfig())
    return config.get(environ.get("API_ENV", 'local'))