# Progressive Residual Channel Discovery via Outlier Score Accumulation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `progressive-residual-channel-discovery-via-outlier-score-accumulation-bbac2cf42f70`
Run ID: `progressive-residual-channel-discovery-via-outlier-score-accumulation-bbac2cf42f70-20260525T032801021188+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c69c72668164

## What looked useful

The useful mechanism is progressive residual refitting, not accumulated outlier score state. Accumulation tied no-accumulation on 120 medium seeds and was slightly worse on 80 rare/dense stress seeds.

## Boundaries and scale limits

Synthetic feature channels only; no learned neural activations, no GPT-2-small-class model, no real training checkpoints, and no broad robustness sweep beyond two local regimes.

## Claim scope

In a bounded synthetic sparse residual-channel recovery benchmark, progressive residual refitting improves over single-pass and random selection, but accumulating robust residual-outlier scores does not improve over simply rescoring the current residual at each round.

## Why it stopped

Synthetic evidence did not support score accumulation as the novel improvement: it was redundant in the medium benchmark and slightly worse in the rare/dense stress benchmark.

## Recommended next action

Stop this run as a proxy early falsification of the accumulation-specific claim; next bounded work should test decayed or reset accumulation variants against current-residual rescoring before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Decay/Reset Accumulation for Progressive Residual Channel Discovery
- Success threshold: A decay/reset accumulation variant improves recall@k by at least 0.05 and held-out MSE improvement by at least 0.5 over current-residual rescoring in paired means, without losing in more than 40% of seeds.
- Stop condition: Stop if no accumulation variant beats current-residual rescoring on paired recall@k and MSE improvement across the stress sweep.

## Evidence references

- Artifact root: `<local-path>/projects/progressive-residual-channel-discovery-via-outlier-score-accumulation-bbac2cf42f70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
