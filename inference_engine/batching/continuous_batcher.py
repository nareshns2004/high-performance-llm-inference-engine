"""Continuous batching primitives."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class BatchItem:
    request_id: str
    prompt: str
    max_new_tokens: int = 64


@dataclass
class ContinuousBatcher:
    max_batch_size: int = 8
    active_requests: List[BatchItem] = field(default_factory=list)

    def add_request(self, item: BatchItem) -> None:
        if len(self.active_requests) >= self.max_batch_size:
            raise ValueError("batch capacity exceeded")
        self.active_requests.append(item)

    def next_batch(self) -> List[BatchItem]:
        batch = self.active_requests[: self.max_batch_size]
        self.active_requests = self.active_requests[self.max_batch_size :]
        return batch
