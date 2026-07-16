"""Quantization abstractions for INT4/INT8 execution."""

from enum import Enum


class QuantizationMode(str, Enum):
    INT8 = "int8"
    INT4 = "int4"


class QuantizedModel:
    def __init__(self, mode: QuantizationMode) -> None:
        self.mode = mode

    def describe(self) -> str:
        return f"Quantized model using {self.mode.value}"
