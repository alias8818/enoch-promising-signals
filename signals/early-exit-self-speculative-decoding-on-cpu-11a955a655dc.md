# Early-Exit Self-Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-self-speculative-decoding-on-cpu-11a955a655dc`
Run ID: `early-exit-self-speculative-decoding-on-cpu-11a955a655dc-20260527T230903193188+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1649e0e8edf2

## What looked useful

Acceptance alone was insufficient for CPU speedup. A shallow cheap exit with high early/full agreement and moderate draft length can help, but deeper exits, overly long drafts, and degraded agreement made self-speculative decoding slower than full decoding.

## Boundaries and scale limits

Synthetic Markov-style layered model only; no trained Transformer, KV cache, tokenizer/corpus prompts, production CPU kernels, or LLM-scale validation. Non-smoke sweeps covered 33 local conditions with vocab=512, dim=256, layers=12, up to 512 generated tokens per repeat.

## Claim scope

In a NumPy synthetic layered token model on this CPU worker, exact early-exit self-speculative decoding produced a narrow best-case 1.192x wall-clock speedup when the early proposal was extremely close to the full distribution, but most tested settings regressed.

## Why it stopped

No-paper closure: bounded proxy evidence found one favorable speedup condition but many regressions, so this is useful implementation guidance rather than direct publication-grade validation.

## Recommended next action

Run a bounded real-model CPU follow-up using a small Transformer with early-exit logits and KV-cache verification; stop paper work for this run because the current evidence is synthetic and mixed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model CPU Early-Exit Self-Speculative Decoding Probe
- Success threshold: At least 1.10x median tokens/s speedup over full decoding across multiple prompt lengths with no distributional verifier bug and acceptance/alignment metrics explaining the gain.
- Stop condition: Stop if real-model early/full agreement is too low for acceptance above roughly 0.85, or if calibrated wall-clock speedup remains below 1.05x in the shallow-exit favorable setting.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-on-cpu-11a955a655dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
