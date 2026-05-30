"""Minimal inference server skeleton."""

from dataclasses import dataclass
from typing import List


@dataclass
class InferenceRequest:
    prompt: str
    max_new_tokens: int = 64


class InferenceServer:
    """A lightweight server placeholder for orchestration logic."""

    def __init__(self, model_name: str = "demo-model") -> None:
        self.model_name = model_name
        self.requests: List[InferenceRequest] = []

    def add_request(self, request: InferenceRequest) -> None:
        self.requests.append(request)

    def run(self) -> str:
        return f"Inference server initialized for {self.model_name}"
