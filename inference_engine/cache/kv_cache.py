"""Simple KV cache interface."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class KVCache:
    blocks: Dict[str, List[float]] = field(default_factory=dict)

    def update(self, key: str, values: List[float]) -> None:
        self.blocks[key] = values

    def get(self, key: str) -> List[float]:
        return self.blocks.get(key, [])
