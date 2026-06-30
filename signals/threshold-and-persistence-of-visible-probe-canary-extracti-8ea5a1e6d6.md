# Threshold and persistence of visible-probe canary extraction across tokenizers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `threshold-and-persistence-of-visible-probe-canary-extracti-8ea5a1e6d6`
Run ID: `threshold-and-persistence-of-visible-probe-canary-extracti-8ea5a1e6d6-20260610T114451866876+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Direct small-model canary trust scoring under visible-probe contamination: enoch://control-plane/projects/direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4/runs/direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4-20260610T025059535603+0000
- Parent run decision: Dose-response visible-probe canary contamination across tokenization and small pretrained models: enoch://control-plane/projects/dose-response-visible-probe-canary-contamination-across-to-8d27eab779/runs/dose-response-visible-probe-canary-contamination-across-to-8d27eab779-20260610T071531798372+0000

## What looked useful

Char and byte models reached near-saturated exact extraction by 4-8 repeated visible canary insertions, while no-canary and untrained baselines stayed at zero. After 500 clean continuation steps, high-frequency char/byte canaries persisted at nonzero exact rates. BPE showed strong low-frequency extraction but a nonmonotone curve, with token fragmentation decreasing as canary frequency increased.

## Boundaries and scale limits

Synthetic corpus only; 1.8M-parameter models; three fixed seeds; greedy extraction only; one BPE configuration; no pretrained LMs, natural corpora, larger model scales, sampling attacks, or long retention horizon.

## Claim scope

Small from-scratch causal Transformers trained on controlled synthetic visible-probe canaries: character and byte tokenization show an immediate exact-extraction threshold around 4-8 insertions and weaker high-frequency persistence after clean continuation; byte-level BPE extracts canaries but does not show the same monotone frequency threshold.

## Why it stopped

Bounded direct validation found a real controlled signal but mixed tokenizer behavior and small synthetic scope are insufficient for publication-grade closure.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded action is to isolate BPE behavior with fixed-vocabulary versus canary-trained BPE and all-row per-canary diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fixed-vocabulary BPE ablation for visible-probe canary thresholds
- Success threshold: A clear separation between canary-trained-BPE and fixed-BPE threshold curves, or a falsification showing both BPE variants remain nonmonotone while controls stay at zero.
- Stop condition: Stop after matched BPE variants over three seeds if controls remain zero and the immediate plus persistence curves either converge to char/byte-like thresholds or remain reproducibly nonmonotone.

## Evidence references

- Artifact root: `<local-path>/projects/threshold-and-persistence-of-visible-probe-canary-extracti-8ea5a1e6d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
