---
name: local-inference-tuning
description: Select and tune a local LLM inference engine for the user's hardware. Use when setting up or auditing local/private model serving, choosing between MLX, llama.cpp, Ollama, and vLLM, estimating model fit, deciding cache/storage policy, tuning batching and KV cache flags, running smoke benchmarks, or exposing an OpenAI-compatible local endpoint.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Local Inference Tuning

Use this skill to design a local inference setup that fits the actual machine, model format, storage policy, and target workflow.

This skill may inspect hardware and local model inventory. Do not remove models, download large weights, change global package manager config, expose network services beyond loopback, or write to system-wide config unless the user explicitly approves.

## Hardware Audit

Collect the minimum useful facts:

- OS and architecture;
- CPU / SoC / GPU;
- RAM or unified memory;
- available accelerators: Metal, CUDA, ROCm, Vulkan, CPU-only;
- free disk on the approved model/cache volume;
- thermal class if visible: desktop, laptop, fanless laptop;
- existing engines: Ollama, llama.cpp, MLX, vLLM, LM Studio, Docker;
- existing local models and formats: GGUF, MLX, safetensors, Ollama manifests.

Use compact commands. On macOS, prefer:

```bash
sysctl -n machdep.cpu.brand_string
sysctl -n hw.memsize
system_profiler SPHardwareDataType
system_profiler SPDisplaysDataType
df -h
ollama list
```

## Engine Selection

Choose the engine by hardware and model format:

- **MLX / Rapid-MLX**: best default for Apple Silicon and MLX-format models. Prefer when the user wants an OpenAI-compatible local endpoint, batching, prompt/prefix cache, and Apple GPU kernels.
- **llama.cpp / llama-cpp-python**: best fallback for GGUF models, especially existing Ollama blobs or fully local files. Use Metal on Apple Silicon, CUDA on NVIDIA, CPU only as fallback.
- **Ollama**: best simple model manager and casual local endpoint. Keep when ease of use matters more than fine-grained batching/KV tuning.
- **vLLM**: best for NVIDIA CUDA servers with enough VRAM and concurrent serving workloads. Do not choose for Apple Silicon laptops.
- **TensorRT-LLM**: specialized NVIDIA deployment path; only use when the user has server NVIDIA hardware and deployment maturity.

If a lower-overhead engine already meets the goal, do not introduce a heavier stack.

## Model Fit Estimate

Estimate before downloading:

- model parameter count and quantization;
- on-disk size;
- expected working set;
- KV cache growth with context length, batch size, and concurrent sequences;
- whether the model fits with OS headroom;
- whether storage policy allows the download location.

For Apple Silicon laptops, keep a meaningful unified-memory reserve. Treat fanless 16 GB machines conservatively:

- prefer 3B-4B 4-bit models as daily local fallback;
- treat 7B 4-bit as possible but pressure-sensitive;
- avoid long-context serving and high concurrency unless memory pressure is low.

## Storage And Cache Policy

Before downloading or converting a model, state where model and cache files will live.

Rules:

- Do not put multi-GB model downloads on the system disk if the user has designated an external or work volume.
- Set Hugging Face and engine cache env vars per project or per command.
- Avoid global shell profile changes unless explicitly requested.
- Do not delete existing local models without explicit approval.

Useful env vars:

```bash
HF_HOME=/Volumes/Work/AI/huggingface
HF_HUB_CACHE=/Volumes/Work/AI/huggingface/hub
MLX_CACHE_DIR=/Volumes/Work/AI/mlx
XDG_CACHE_HOME=/Volumes/Work/AI/cache
```

If an engine hardcodes `~/.cache/<engine>`, use a narrow symlink to the approved volume and document it.

## Tuning Profile

Produce a profile with:

- engine and model;
- model alias served to clients;
- bind host and port;
- max concurrent sequences and request queue cap;
- prefill and completion batch sizes;
- context or max token limits;
- KV cache dtype or quantization;
- prefix/prompt cache settings;
- chunked prefill settings for agent prompts;
- GPU memory utilization or memory reserve;
- fallback profile for reasoning or high-quality checks.

For Apple Silicon + Rapid-MLX, prefer:

- loopback-only bind: `127.0.0.1`;
- low concurrency on 16 GB machines;
- prefix cache enabled;
- radix index where available;
- int4 KV cache for speed/memory fallback work;
- int8 KV cache for harder reasoning if quality matters more;
- chunked prefill for long agent prompts;
- conservative GPU memory utilization on fanless laptops.

For llama.cpp, prefer:

- Metal enabled on Apple Silicon;
- `n_gpu_layers=-1` when it fits;
- `n_ctx` no larger than needed;
- moderate `n_batch` and smaller `n_ubatch` on memory-constrained laptops;
- mmap on, mlock off by default.

## Smoke Bench

Verify in this order:

1. Engine health check.
2. Model list or model info.
3. Single-prompt smoke benchmark.
4. OpenAI-compatible `/v1/models`.
5. Short `/v1/chat/completions`.
6. Cache location check.
7. Memory pressure check.

If memory pressure warning appears, lower concurrency and cache before increasing model size.

## Endpoint Recipe

Return copy-paste commands for:

- environment loading;
- server start;
- `/v1/models` test;
- chat completion test;
- client configuration model id;
- shutdown.

Never expose the server on `0.0.0.0` without auth review.

## Final Report

Report:

- hardware summary;
- selected engine and why;
- rejected engines and why;
- selected model and storage path;
- tuned flags;
- benchmark/smoke result;
- endpoint URL and model id;
- remaining risks;
- explicit non-actions, such as models not removed or global config not changed.
