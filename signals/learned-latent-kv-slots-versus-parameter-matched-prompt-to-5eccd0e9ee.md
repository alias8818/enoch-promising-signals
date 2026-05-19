# Learned latent KV slots versus parameter-matched prompt-token memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `28`
Project ID: `learned-latent-kv-slots-versus-parameter-matched-prompt-to-5eccd0e9ee`
Run ID: `learned-latent-kv-slots-versus-parameter-matched-prompt-to-5eccd0e9ee-20260519T111407832418+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `28`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Learned latent KV slots versus parameter-matched prompt-token memory: internal_generated:learned-latent-kv-slots-versus-parameter-matched-prompt-to-5eccd0e9ee

## What looked useful

Learned latent KV slots slightly improved loss versus prompt tokens, but the same effect was matched by frozen zero KV slots, indicating an architectural attention-sink/normalization effect rather than learned latent memory.

## Boundaries and scale limits

Synthetic lookup only; small 4-layer 96-dimensional transformer; 1000-1500 training steps; no natural-language pretraining, GPT-2-small-class replication, or high-accuracy solved-task regime.

## Claim scope

Small-transformer synthetic in-context key-value lookup with parameter-matched learned prompt tokens, learned latent KV slots, and frozen KV-slot controls across seeds 0, 1, and 2.

## Why it stopped

Direct bounded lookup tests with a parameter-matched prompt baseline and frozen-slot ablation did not support learned KV slots as a distinct learned-memory mechanism; evidence is useful but not paper-positive.

## Recommended next action

Stop this depth-4 follow-up as a no-paper mechanism falsification; do not recommend another chained follow-up because the controller lineage is already at depth 4.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/learned-latent-kv-slots-versus-parameter-matched-prompt-to-5eccd0e9ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
