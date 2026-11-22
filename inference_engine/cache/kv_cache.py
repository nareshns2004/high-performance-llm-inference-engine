"""Placeholder KV store: a dict of float lists.

There are no blocks, paging, GPU memory or eviction. A real KV cache manager pre-allocates a
pool of fixed-size GPU blocks, maps each request's tokens to blocks through a block table,
reuses blocks by prefix hash with reference counts, and evicts free blocks LRU.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class KVCache:
    blocks: Dict[str, List[float]] = field(default_factory=dict)

    def update(self, key: str, values: List[float]) -> None:
        self.blocks[key] = values

    def get(self, key: str) -> List[float]:
        return self.blocks.get(key, [])
