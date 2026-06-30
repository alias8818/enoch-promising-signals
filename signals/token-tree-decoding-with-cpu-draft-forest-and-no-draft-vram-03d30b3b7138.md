# Token tree decoding with CPU draft forest and no draft VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `token-tree-decoding-with-cpu-draft-forest-and-no-draft-vram-03d30b3b7138`
Run ID: `token-tree-decoding-with-cpu-draft-forest-and-no-draft-vram-03d30b3b7138-20260529T115213237615+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8d22261cc54

## What looked useful

Draft weights stayed off CUDA with zero draft CUDA parameter tensors, and draft top-k child overlap was substantial, but CPU draft proposal time dominated wall clock: Pythia lookahead-4 throughput was 22.18 tokens/s vs 159.08 tokens/s baseline (0.139x), and Qwen probe throughput was 4.37 tokens/s vs 43.51 tokens/s baseline (0.100x).

## Boundaries and scale limits

Tested Pythia 410M GPU target with Pythia 70M CPU draft across 4 prompts x 24 tokens plus lookahead sweep, and a short Qwen 1.5B GPU target with Qwen 0.5B CPU draft probe. Did not test production batching, async CPU/GPU overlap, quantized CPU draft inference, optimized tree verifier kernels, or larger 7B+ target models.

## Claim scope

Small local greedy-decoding microbenchmarks with real cached causal LMs show that CPU-resident draft models can avoid draft VRAM and produce target-token overlap, but do not improve end-to-end throughput versus target-only greedy decoding.

## Why it stopped

Direct local microbenchmarks falsified the throughput part of the hypothesis for the tested configurations: zero draft VRAM was achieved, but CPU draft latency overwhelmed target-forward savings. This is a bounded early falsification, not a full production-scale validation.

## Recommended next action

Stop this run as a no-paper useful negative; only revisit with an optimized asynchronous or quantized CPU draft implementation that can demonstrate CPU draft wall share below 20-30% before larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Async quantized CPU draft forest with larger GPU verifier
- Success threshold: Greater than 1.10x end-to-end tokens/s versus target-only greedy decoding while keeping draft CUDA parameter tensors at zero and CPU draft wall share below 30%.
- Stop condition: Stop if optimized CPU draft wall share remains above 50% or if end-to-end throughput stays below 0.9x baseline after lookahead/tree-width tuning.

## Evidence references

- Artifact root: `<local-path>/projects/token-tree-decoding-with-cpu-draft-forest-and-no-draft-vram-03d30b3b7138`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
