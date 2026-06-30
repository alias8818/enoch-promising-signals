# Self-Speculative Decoding via Early Exit on Shared Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-on-shared-weights-bb695d3ea4e5`
Run ID: `self-speculative-decoding-via-early-exit-on-shared-weights-bb695d3ea4e5-20260529T200411609915+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ec37227404fd

## What looked useful

Auxiliary early-exit training changed the shallow-exit behavior sharply: the no-auxiliary control had only 0.046 layer-1 agreement and 0.0087 acceptance, while the auxiliary model reached 1.000 layer-1 agreement and 1.000 acceptance. Modeled layer work improved 2.0x at exit 1, but measured wall-clock remained slower than greedy baseline, with best auxiliary wall speedup 0.760x.

## Boundaries and scale limits

Evidence is limited to a tiny synthetic task, one seed, greedy decoding, draft length 4, and a naive no-KV-cache implementation on GB10. It does not validate natural-language quality, pretrained/GPT-2-small-class behavior, production serving kernels, or actual latency speedup.

## Claim scope

On a synthetic latent-topic recurrence task with a 4-layer shared-weight transformer, auxiliary intermediate LM losses can make layer-1 early-exit logits match the final model and achieve perfect speculative acceptance, yielding up to 2.0x modeled transformer-block work reduction.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the early-exit acceptance mechanism but the direct wall-clock test is slower than baseline and is not a full validation.

## Recommended next action

Run a bounded deepen test on a real small language-model setup with KV-cache-aware self-speculative decoding, and require actual tokens/s speedup before treating the idea as practically viable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware self-speculative early exits on a GPT-2-small-class language task
- Success threshold: Acceptance >= 0.75 at exit layer 1 or 2, quality/perplexity within 2% of greedy final-model decoding, and measured wall-clock tokens/s >= 1.15x greedy baseline on the same hardware.
- Stop condition: Stop if modeled layer-work speedup is below 1.10x after training, if acceptance stays below 0.50 at exits 1-2, or if KV-cache-aware wall-clock remains below 1.00x greedy baseline after profiling obvious overheads.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-on-shared-weights-bb695d3ea4e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
