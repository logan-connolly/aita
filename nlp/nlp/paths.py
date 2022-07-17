import dataclasses
import enum
import uuid
from pathlib import Path
from typing import Optional


class DataDir(enum.Enum):
    RAW = "raw"
    PROCESSED = "processed"
    CONFIGS = "configs"
    MODELS = "models"


@dataclasses.dataclass
class DataDirs:
    raw: Path
    processed: Path
    configs: Path
    models: Path

    def __post_init__(self):
        for data_dir_name in self.__dataclass_fields__:
            data_dir = getattr(self, data_dir_name)
            data_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def create(cls, root_path: Path):
        return cls(
            raw=root_path / DataDir.RAW.value,
            processed=root_path / DataDir.PROCESSED.value,
            configs=root_path / DataDir.CONFIGS.value,
            models=root_path / DataDir.MODELS.value,
        )

    def create_run_id(self, target: str, run_id: Optional[str] = None) -> Path:
        assert target in self.__dataclass_fields__, f"{target} dir not available"
        run_id_ = run_id if run_id else str(uuid.uuid4())
        run_id_path = getattr(self, target) / run_id_
        run_id_path.mkdir(exist_ok=True)
        return run_id_path

    def get_run_id(self, target: str, run_id: str) -> Path:
        assert target in self.__dataclass_fields__, f"{target} dir not available"
        run_id_path = getattr(self, target) / run_id
        assert run_id_path.exists(), f"Can't find file: {run_id_path}"
        return run_id_path


DATA_DIRS = DataDirs.create(root_path=Path(__file__).parents[1] / "data")
