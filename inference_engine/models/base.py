"""Model adapter interfaces."""

from dataclasses import dataclass


@dataclass
class ModelConfig:
    model_name: str = "demo-model"
    quantization: str = "int8"


class BaseModel:
    def __init__(self, config: ModelConfig | None = None) -> None:
        self.config = config or ModelConfig()

    def load(self) -> str:
        return f"Loaded {self.config.model_name}"
