# Self-Speculative CPU Decoding via Early-Layer Exit Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-cpu-decoding-via-early-layer-exit-drafting-22502e9bd56d`
Run ID: `self-speculative-cpu-decoding-via-early-layer-exit-drafting-22502e9bd56d-20260524T161924970231+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57c7e86ee078

## What looked useful

Early exits at depths 1-5/6 matched the full model on 16.7%, 8.3%, 25.0%, 25.0%, and 50.0% of prompts respectively. The best optimistic speculative speed model over k={2,4,8} was 0.9505x at depth 1 and all other exits were lower, so the raw mechanism is unlikely to beat plain greedy decoding even before real implementation overheads.

## Boundaries and scale limits

Single CPU worker, NumPy implementation, distilgpt2 only, 12 prompts, sequence length cap 32, agreement/cost-model validation rather than a production KV-cache speculative decoder. Does not test trained exit heads, adaptive confidence thresholds, larger model families, or optimized C++ serving backends.

## Claim scope

On cached distilgpt2 with 12 fixed natural-language prompts, raw untrained early-layer exits projected through the tied LM head do not provide enough greedy next-token agreement relative to their CPU layer cost to support self-speculative CPU decoding speedups.

## Why it stopped

Proxy/early falsification rather than full validation: the necessary acceptance-versus-cost condition failed on a real GPT-2-family model under an optimistic speculative speed model.

## Recommended next action

Stop this raw untrained early-exit drafting line; a concrete adjacent follow-up should test whether a trained lightweight early-exit head with confidence gating can exceed 80% accepted-token rate at <=25% full-model draft cost on the same CPU harness.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Trained Confidence-Gated Early-Exit Heads for CPU Speculative Drafting
- Success threshold: At least 1.15x wall-clock tokens/sec over greedy decoding at identical output semantics, with <=25% full-model draft cost and >=80% accepted draft tokens on a held-out prompt set.
- Stop condition: Stop if trained/gated shallow exits cannot exceed 60% accepted-token rate at <=25% full-model draft cost or if direct decoder wall-clock speed remains <=1.0x greedy on the CPU worker.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-cpu-decoding-via-early-layer-exit-drafting-22502e9bd56d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
