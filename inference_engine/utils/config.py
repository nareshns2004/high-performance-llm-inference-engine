"""Simple configuration helpers."""

from dataclasses import dataclass


@dataclass
class EngineConfig:
    max_batch_size: int = 8
    max_context_length: int = 4096
    quantization_mode: str = "int8"
