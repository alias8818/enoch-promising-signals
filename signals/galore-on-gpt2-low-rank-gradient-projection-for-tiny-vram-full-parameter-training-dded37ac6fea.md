# GaLore-on-GPT2: Low-rank gradient projection for tiny-VRAM full-parameter training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-on-gpt2-low-rank-gradient-projection-for-tiny-vram-full-parameter-training-dded37ac6fea`
Run ID: `galore-on-gpt2-low-rank-gradient-projection-for-tiny-vram-full-parameter-training-dded37ac6fea-20260621T203837041436+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1dd78a52684f

## What looked useful

The core memory mechanism is reproducible locally: optimizer-state bytes dropped from 27.636 MB for AdamW to 0.831 MB at rank 8, 2.994 MB at rank 32, and 11.645 MB at rank 128. Projection error decreased with rank, and rank-128 GaLore at lr=1e-3 reached final loss 5.8319, near AdamW lr=2e-4 final loss 5.7998, but AdamW lr=1e-3 reached 5.0173 and GaLore throughput was about 53-55% of AdamW.

## Boundaries and scale limits

Synthetic data only, 80 training steps, random initialization, tiny GPT-2 configuration with 13.8 MB of parameters, one GB10 GPU, and a simple full-SVD GaLore-style implementation rather than a production-optimized GaLore package.

## Claim scope

On a synthetic 4-layer GPT-2-style CUDA language-modeling benchmark, a local GaLore-style AdamW optimizer reduced optimizer-state memory by 58-97% while updating all parameters, but matched-learning-rate training quality and throughput lagged AdamW over 80 steps.

## Why it stopped

Finalized as no-paper useful signal because the local evidence is synthetic and short-horizon, and the tested GaLore-style implementation reduces optimizer memory but does not match AdamW quality or throughput under fair high-learning-rate control.

## Recommended next action

Run a bounded deepen test on a real small text corpus for 1k-5k steps using an optimized/reference GaLore implementation, tuned LR per optimizer, and an explicit VRAM cap; stop if GaLore cannot reach within 5% validation loss of AdamW while preserving at least 50% optimizer-state savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-GPT2 GaLore memory-quality tradeoff
- Success threshold: GaLore reaches within 5% of AdamW validation loss at equal step budget while preserving at least 50% optimizer-state byte reduction and avoiding more than 2x wall-clock slowdown.
- Stop condition: Stop if rank-128 GaLore remains more than 5% worse in validation loss after LR tuning or if its wall-clock slowdown exceeds 2x while optimizer-state savings fall below 50%.

## Evidence references

- Artifact root: `<local-path>/projects/galore-on-gpt2-low-rank-gradient-projection-for-tiny-vram-full-parameter-training-dded37ac6fea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
