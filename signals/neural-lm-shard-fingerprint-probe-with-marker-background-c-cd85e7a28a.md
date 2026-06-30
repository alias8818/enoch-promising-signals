# Neural LM shard fingerprint probe with marker-background controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `neural-lm-shard-fingerprint-probe-with-marker-background-c-cd85e7a28a`
Run ID: `neural-lm-shard-fingerprint-probe-with-marker-background-c-cd85e7a28a-20260621T013716093924+0000`

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

- Parent run decision: Statistical Fingerprinting of Volunteer Training Shards: enoch://control-plane/projects/statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb/runs/statistical-fingerprinting-of-volunteer-training-shards-f9e573fc6ebb-20260621T011752544847+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/addb2b44e416

## What looked useful

The Tier-1 controlled test met its threshold: marker_background_masked accuracy was 1.0000 versus 0.25 chance, while the cue-stripped motif_masked_negative_control was 0.2604. Background rematching dropped accuracy to 0.3563, showing that marker/background controls are necessary for interpreting shard fingerprints.

## Boundaries and scale limits

Small synthetic corpus only: 4 shards, 240 train sequences per shard, 120 held-out sequences per shard, 64-token vocabulary, neural bigram architecture, single seed. No real corpora, pretrained transformers, long contexts, multi-seed robustness, or production-scale shard attribution were tested.

## Claim scope

In a deterministic synthetic 4-shard neural bigram LM setup, shard source attribution by per-shard LM negative log likelihood remains accurate after explicit marker and background tokens are masked, and collapses to chance when shard-specific motifs are also removed.

## Why it stopped

Tier-1 controlled direct test completed and produced useful mechanism evidence, but the result is synthetic and not paper-ready.

## Recommended next action

Run a bounded medium confirmation with repeated seeds and a small transformer or GPT-2-small-class baseline on semi-real corpora, comparing against n-gram attribution and retaining the same marker/background/motif controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium transformer shard fingerprint confirmation with marker-background controls
- Success threshold: Across at least 3 seeds, controlled transformer attribution remains at least 0.60 and at least 0.15 absolute above the strongest non-neural baseline after marker/background controls, while cue-stripped controls stay no more than 0.10 above chance.
- Stop condition: Stop if controlled transformer attribution falls below 0.60 in two seeds, if the non-neural baseline matches the neural effect within 0.05 absolute accuracy, or if cue-stripped controls remain substantially above chance.

## Evidence references

- Artifact root: `<local-path>/projects/neural-lm-shard-fingerprint-probe-with-marker-background-c-cd85e7a28a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
