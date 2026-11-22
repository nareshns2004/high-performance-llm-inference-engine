# high-performance-llm-inference-engine

> [!IMPORTANT]
> **Superseded and archived.** This repository is an early placeholder and is not an
> inference engine. It contains about 160 lines of placeholder classes named after serving
> features. There is no model, no tensors and no inference. My inference work lives in
> **[kvwire](https://github.com/nareshns2004/kvwire-disaggregated-inference-engine)**,
> which plugs into vLLM through its KV connector instead of building an engine.
> See [ADR-0001](docs/adr/0001-superseded-by-kvwire.md).

## What is here

| Module | What it is | What a real engine does instead |
|---|---|---|
| `api/server.py` | Stores requests in a list | Async OpenAI-compatible server with streaming |
| `batching/continuous_batcher.py` | A **static** FIFO batch queue | Iteration-level scheduling under a per-step token budget, with chunked prefill and preemption |
| `cache/kv_cache.py` | A dict of float lists | Paged block pool, per-request block tables, prefix-hash caching, eviction |
| `decoding/speculative.py` | Returns a draft length | A draft proposer plus rejection-sampling verification in one target pass |
| `quantization/quantize.py` | An enum | Quantised weights with dequantisation fused into the GEMM kernels |
| `models/base.py` | Returns a string | Loads and shards weights and captures CUDA graphs |

Each module's docstring says what it is not, so that nobody mistakes it for the real mechanism.

## Why it was not built

vLLM, SGLang and TensorRT-LLM already solve the scheduler, kernels and model support, and
they change quickly. The unsolved piece that fits my background is moving KV between prefill
and decode pools over RDMA, and staying correct when the network fails. That is kvwire.

## Running the smoke test

```bash
pip install -e '.[dev]'
pytest
```

## License

See [LICENSE](LICENSE).
