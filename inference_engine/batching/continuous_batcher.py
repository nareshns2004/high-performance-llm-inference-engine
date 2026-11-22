"""Placeholder batch queue. This is STATIC batching, not continuous batching.

``add_request`` raises once the queue is full, and ``next_batch`` drains the whole batch at
once. Real continuous (iteration-level) batching re-forms the batch every decode step:
finished sequences leave, waiting ones join if the token budget and free KV blocks allow,
long prompts are chunked, and requests are preempted (recompute or swap) under memory
pressure instead of being rejected.
"""

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
