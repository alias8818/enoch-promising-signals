# Hybrid Low-Rank First Moment with Diagonal Second-Moment Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-low-rank-first-moment-with-diagonal-second-moment-r-da1ee9f5fe`
Run ID: `hybrid-low-rank-first-moment-with-diagonal-second-moment-r-da1ee9f5fe-20260518T094516450067+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6c6ccfa4c7b7

## What looked useful

Rank 32 reached mean validation loss 2.4253 versus AdamW 2.3923 at 700 steps, a +0.0330 gap with 26.0% fewer optimizer-state elements. Lower ranks saved more state but had larger loss regressions. Exact SVD made the hybrid optimizer about 14x slower than AdamW.

## Boundaries and scale limits

Tested only a 2-layer 96-dim char-level GPT on Tiny Shakespeare for 350 and 700 optimizer steps across 3 seeds. The implementation uses exact per-step SVD and does not validate efficient projection updates, GPT-2-small-class scale, large-token pretraining, or downstream transfer.

## Claim scope

Small direct Tiny Shakespeare character-LM training shows a low-rank first-moment plus diagonal second-moment AdamW variant has a monotonic rank-quality tradeoff and can approach AdamW validation loss while reducing optimizer-state elements.

## Why it stopped

Small direct evidence supports a mechanism but not a paper or practical optimizer: the best rank still slightly trails AdamW and the exact-SVD update is too slow.

## Recommended next action

Stop this run as no-paper useful signal; next implement a randomized or infrequent low-rank first-moment update and rerun the same small LM comparison with a throughput penalty below 2x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Efficient Hybrid Low-Rank AdamW Update for Small LM Training
- Success threshold: Hybrid rank 32 or lower has mean validation-loss gap <= +0.03 versus AdamW, saves >=20% optimizer-state elements, and runs at >=50% of AdamW tokens/s on the same GB10 setup.
- Stop condition: Stop if the efficient update either exceeds +0.05 validation-loss gap at 700 steps or remains slower than 2x AdamW after one bounded implementation attempt.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-low-rank-first-moment-with-diagonal-second-moment-r-da1ee9f5fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
