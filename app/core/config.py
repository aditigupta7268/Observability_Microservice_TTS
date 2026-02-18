from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    app_name: str = "TTS Observable Service"
    version: str = "1.0.0"
    environment: str = "dev"
    output_dir: str = "output"

    @property
    def output_path(self) -> Path:
        return Path(self.output_dir).resolve()


settings = Settings()
