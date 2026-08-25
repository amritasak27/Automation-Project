import json
import csv


class DataReader:
    """Strategy pattern: test code calls read(path) without caring whether
    the underlying data source is JSON or CSV. Add a new format by adding
    one private method + one elif branch - no test code changes.
    """

    def read(self, path: str):
        if path.endswith(".json"):
            return self._read_json(path)
        elif path.endswith(".csv"):
            return self._read_csv(path)
        raise ValueError(f"Unsupported data file format: {path}")

    @staticmethod
    def _read_json(path: str):
        with open(path, "r") as f:
            return json.load(f)

    @staticmethod
    def _read_csv(path: str):
        with open(path, newline="") as f:
            return list(csv.DictReader(f))
