import yaml
import os


class ConfigReader:
    """Singleton pattern - see data-driven-framework/utils/config_reader.py for rationale."""

    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = os.path.join(
            os.path.dirname(__file__), "..", "config", "config.yaml"
        )
        with open(config_path, "r") as f:
            self._config = yaml.safe_load(f)

    @property
    def base_url(self) -> str:
        return self._config["base_url"]

    @property
    def browser(self) -> str:
        return self._config.get("browser", "chromium")

    @property
    def headless(self) -> bool:
        return self._config.get("headless", True)
