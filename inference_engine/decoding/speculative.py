"""Placeholder for speculative decoding. There is no draft model and no verification.

``plan`` only caps the draft length, and ``verify_every`` is unused. Real speculative
decoding drafts k tokens, scores all k+1 positions in one target forward pass, accepts each
token with probability min(1, p_target / p_draft), and resamples from the residual
distribution at the first rejection, so the output distribution is exactly the target's.
"""

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
