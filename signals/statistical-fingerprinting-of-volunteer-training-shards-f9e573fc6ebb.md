# Statistical Fingerprinting of Volunteer Training Shards

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb`
Run ID: `statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb-20260621T011752544847+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/addb2b44e416

## What looked useful

Null and marker-background controls stayed near chance while weak and medium marker-injection scenarios were recoverable. Weak background setting reached AUC 0.9126 and precision-at-included-k 0.8399; medium background reached AUC 0.9955 and precision-at-included-k 0.9730; permuted-marker controls stayed near chance.

## Boundaries and scale limits

Synthetic shards only; aggregate count model only; no neural LM training; no real volunteer data; no privacy-defense, deduplication, tokenizer, optimizer, or generation-policy validation.

## Claim scope

In a bounded synthetic aggregate-unigram proxy, volunteer shards with stable rare-token marker biases are statistically attributable from model probability scores, including with marker-background noise controls.

## Why it stopped

This run produced a useful proxy mechanism signal, but it is not direct publication-grade evidence for real volunteer training shards or neural models.

## Recommended next action

Run a bounded neural LM follow-up with the same candidate-marker, null, marker-background, and permuted-marker controls before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural LM shard fingerprint probe with marker-background controls
- Success threshold: Medium marker-background neural scenario reaches AUC >= 0.80 and precision-at-included-k >= 0.70 across at least 5 seeds while null and permuted controls remain between 0.40 and 0.60 AUC.
- Stop condition: Stop as negative if the medium marker-background scenario fails to exceed AUC 0.65 or if controls also rise above 0.65 AUC, indicating confounding rather than shard-specific attribution.

## Evidence references

- Artifact root: `<local-path>/projects/statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
