# Skill Card: local-inference-tuning

## Description
Selects and tunes a local LLM inference engine for the user's hardware, model format, storage policy, batching needs, KV cache profile, and OpenAI-compatible endpoint requirements.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when setting up local/private model serving, choosing between MLX, llama.cpp, Ollama, and vLLM, estimating model fit, deciding model/cache storage locations, tuning batching and KV cache flags, and validating a local OpenAI-compatible endpoint.

## Out of Scope
Do not use to delete existing models, download multi-GB weights, expose services beyond loopback, change global shell/package-manager config, or alter production inference infrastructure without explicit approval.

## Sources and Attribution
ABVX original, informed by local Apple Silicon inference work, Rapid-MLX and MLX tuning practice, llama.cpp deployment patterns, Ollama model management, vLLM CUDA serving patterns, and public discussions of memory bandwidth, batching, and KV cache constraints.

## Inputs and Outputs
Inputs: hardware details, OS, accelerator, RAM/VRAM, model format, existing model inventory, approved storage volume, target latency/concurrency, and privacy/network constraints.

Outputs: engine recommendation, rejected-engine rationale, model fit estimate, storage/cache policy, tuned flags, smoke benchmark plan, endpoint recipe, and residual risks.

## Risks and Mitigations
- Risk: model downloads fill the wrong disk. Mitigation: require storage policy and cache env vars before pulling weights.
- Risk: memory pressure or system instability on unified-memory Macs. Mitigation: estimate working set, keep headroom, and lower concurrency/cache before increasing model size.
- Risk: unsafe local server exposure. Mitigation: default to `127.0.0.1` and require auth review before `0.0.0.0`.
- Risk: overfitting to one model. Mitigation: separate engine choice, model fit, and tuning profile.

## Model Sensitivity
Works best on models that can reason about systems constraints and command-line tradeoffs. Smaller models may need stronger templates for memory estimates and rejected-engine rationale.

## Composable With
- `goal-loop-designer`
- `token-efficient-execution`
- `delivery-preflight-gate`
- `web-quality-audit`

## Anti-Patterns
- choosing vLLM for Apple Silicon laptops
- downloading models before checking the approved storage volume
- treating Ollama model inventory as disposable
- setting global pip, uv, Hugging Face, or shell config when a project-local env is enough
- increasing context and concurrency before measuring memory pressure

## Evaluation
Evaluated by hardware audit quality, engine fit, cache-location verification, smoke benchmark evidence, endpoint usability, and whether existing local models/configs were left intact unless the user approved changes.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
