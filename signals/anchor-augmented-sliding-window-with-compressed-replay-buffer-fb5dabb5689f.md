# Anchor-Augmented Sliding Window with Compressed Replay Buffer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-augmented-sliding-window-with-compressed-replay-buffer-fb5dabb5689f`
Run ID: `anchor-augmented-sliding-window-with-compressed-replay-buffer-fb5dabb5689f-20260528T163343655615+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ad0d66fa7103

## What looked useful

Sliding-window recall failed outside its horizon as expected. A global compressed replay baseline reached 34.688% accuracy with 3,584 peak memory slots. The naive anchor-replay configuration reached only 0.106% accuracy with 4,400 slots; it beat global replay only after increasing per-segment capacity to about 18,259 slots, with substantially slower lookup.

## Boundaries and scale limits

Tested 30k-50k synthetic items, 5k-10k queries per seed, 3-5 seeds, CPU-only. This does not validate or reject learned transformer implementations, natural-language perplexity, GPU attention kernels, or GPT-2-small-class training.

## Claim scope

In a bounded synthetic associative-recall probe with fixed long lags, exact sliding-window memory, non-learned segment anchors, and lossy hash-bucket compressed replay, the naive anchor-gated compressed replay mechanism did not provide an efficient recall advantage over a simpler global compressed replay baseline.

## Why it stopped

Bounded synthetic evidence is an early falsification of the naive efficient anchor-plus-compressed-replay mechanism, not a full-scale validation or rejection of learned long-context model variants.

## Recommended next action

Stop this project as a no-paper useful negative; only revisit with a distinct learned-compression follow-up that directly tests whether learned replay can overcome the per-segment capacity failure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned compressed replay for anchor-gated long-range recall
- Success threshold: At matched peak memory within 10% of the global replay baseline, learned anchor-replay improves long-lag recall accuracy by at least 20% relative over global compressed replay while keeping false positives below 1%.
- Stop condition: Stop if learned anchor-replay cannot exceed global replay at matched memory after a small trained probe with at least 3 seeds and a fixed validation set.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-augmented-sliding-window-with-compressed-replay-buffer-fb5dabb5689f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
