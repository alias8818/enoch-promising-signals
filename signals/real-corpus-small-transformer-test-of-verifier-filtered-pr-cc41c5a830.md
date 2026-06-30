# Real-corpus small-transformer test of verifier-filtered pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-small-transformer-test-of-verifier-filtered-pr-cc41c5a830`
Run ID: `real-corpus-small-transformer-test-of-verifier-filtered-pr-cc41c5a830-20260630T020748062523+0000`

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

- Parent run decision: Small-verifier quality-filtered pretraining: enoch://control-plane/projects/small-verifier-quality-filtered-pretraining-cd4e027a83d4/runs/small-verifier-quality-filtered-pretraining-cd4e027a83d4-20260629T203331647248+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a1bc16d9a396

## What looked useful

The verifier mechanically selected lower-NLL chunks, but final loss deltas were seed-sensitive and near zero: mean validation delta filtered-minus-baseline +0.00019 and mean test delta +0.00082, with filtering improving only 1 of 3 seeds.

## Boundaries and scale limits

Small byte-level model, short training horizon, WikiText-2 only, simple trigram verifier only, no GPT-2-scale baseline, no neural/semantic verifier, no downstream transfer, no long-run scaling.

## Claim scope

On WikiText-2 raw byte-level next-byte pretraining with an 875,264-parameter Transformer, 500 steps per arm, three seeds, and equal-token controls, filtering train chunks by lowest held-out trigram-verifier NLL did not robustly improve validation or test loss over random sampling.

## Why it stopped

Bounded real-corpus evidence is mixed and does not support the verifier-filtered pretraining hypothesis for the tested small-transformer/trigram-verifier setup; this is an early scoped falsification, not a full-scale validation.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded deepen follow-up if using a stronger neural verifier plus GPT-2-style tokenization/model and pre-registered multi-seed thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-verifier filtered WikiText pretraining with GPT-2-style tokenization
- Success threshold: Filtered arm improves mean validation and test loss versus random by at least 0.01 nats or 0.014 bits/byte across five seeds, with at least 4 of 5 seeds improving.
- Stop condition: Stop if the neural-verifier filtered arm fails to improve at least 3 of the first 5 seeds or if the mean held-out loss gain remains below 0.005 nats after matched training.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-small-transformer-test-of-verifier-filtered-pr-cc41c5a830`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
