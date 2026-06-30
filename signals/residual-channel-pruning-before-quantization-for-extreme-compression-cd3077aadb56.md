# Residual Channel Pruning Before Quantization for Extreme Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-pruning-before-quantization-for-extreme-compression-cd3077aadb56`
Run ID: `residual-channel-pruning-before-quantization-for-extreme-compression-cd3077aadb56-20260605T230425187795+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/98b36175dbbe

## What looked useful

Final 3-seed main run: best extreme activation prune+quant accuracy 0.5802 mean versus 0.1110 quantization-only and 0.4714 random prune+quant. Per-seed matched-or-smaller storage deltas versus available quantization-only controls were all positive: +0.3281, +0.6470, +0.4585.

## Boundaries and scale limits

Synthetic teacher-generated classification only; residual MLP rather than transformer; no real text corpus, GPT-2-small-class model, packed-kernel storage, latency, or downstream robustness validation. Effective storage counts parameters times bit-width and omits metadata and hardware packing overhead.

## Claim scope

In a 3-seed NumPy teacher/student residual-MLP classification proxy, activation-ranked residual-branch channel pruning before uniform low-bit weight quantization preserved substantially higher test accuracy than quantization-only under at least 16x fp32 parameter-storage compression, and outperformed random residual-channel pruning at matched keep fractions.

## Why it stopped

No-paper useful signal: the mechanism is supported only by a small synthetic residual-network proxy, not by direct transformer or real-dataset evidence.

## Recommended next action

Run a bounded small-transformer real-text follow-up with residual-stream MLP/channel pruning before 4-bit and 2-bit quantization, equal-storage baselines, and packed-size accounting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer residual-channel pruning before quantization on real text
- Success threshold: At matched effective storage of at least 8x fp32 compression, activation-ranked prune-before-quantization improves validation perplexity by at least 5% versus the best quantization-only or random-pruning control in at least 2 of 3 seeds without more than 10% perplexity degradation versus the dense baseline.
- Stop condition: Stop if activation-ranked pruning fails to beat both quantization-only and random-pruning controls at matched storage in 2 of 3 seeds, or if packed-size accounting removes the claimed compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-pruning-before-quantization-for-extreme-compression-cd3077aadb56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
