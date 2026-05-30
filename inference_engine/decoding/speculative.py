"""Speculative decoding helpers."""

from dataclasses import dataclass


@dataclass
class SpeculativeDecoderConfig:
    draft_tokens: int = 4
    verify_every: int = 2


class SpeculativeDecoder:
    def __init__(self, config: SpeculativeDecoderConfig | None = None) -> None:
        self.config = config or SpeculativeDecoderConfig()

    def plan(self, prompt_length: int) -> int:
        return min(self.config.draft_tokens, max(1, prompt_length))
