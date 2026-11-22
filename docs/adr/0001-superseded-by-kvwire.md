# ADR-0001: Superseded by kvwire; do not build an engine

- **Status:** Accepted
- **Date:** 2026-11-22

## Context

This repository was scaffolded as a "high-performance LLM inference engine" with modules
named after continuous batching, KV cache management, speculative decoding and INT4/INT8
quantisation. None of them was implemented. A real engine needs model loading, paged
attention kernels, an iteration-level scheduler, a sampler, a tokenizer, an OpenAI-compatible
API and quantised kernels. That is months of work, and the result would still trail vLLM and
SGLang.

[kvwire](https://github.com/nareshns2004/kvwire-disaggregated-inference-engine) has since
made the opposite decision: it plugs into vLLM through the KV connector interface and owns only
the KV transport between prefill and decode pools, plus failure handling.

## Decision

Superseded by kvwire. We extend an engine rather than write one, because the scheduler,
kernels and model support are a solved, fast-moving problem. This repository stays as an
archived placeholder and gets no new features.

## Consequences

- The repository is archived on GitHub, unpinned, and not linked from the resume or portfolio.
- The serving knowledge (scheduling, paged KV, speculative decoding, quantisation,
  disaggregation) is studied by reading vLLM's source, and the notes feed kvwire.
- Nothing here overlaps kvwire's scope (KV transport, the re-layout kernel, the coordinator).
