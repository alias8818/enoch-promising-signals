# Natural-text canary attribution under adaptive poisoning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-text-canary-attribution-under-adaptive-poisoning-b0065877bc`
Run ID: `natural-text-canary-attribution-under-adaptive-poisoning-b0065877bc-20260628T190507386999+0000`

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

- Parent run decision: Canary Probe Attribution for Volunteer Data Poisoning Detection: enoch://control-plane/projects/canary-probe-attribution-for-volunteer-data-poisoning-detection-4379a08fdf78/runs/canary-probe-attribution-for-volunteer-data-poisoning-detection-4379a08fdf78-20260628T180715490297+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Multi-hit margin attribution preserved no-attack owner recall and kept imperfect slot-mimic false victim attribution near 1-2% at equal exposure, but exact-copy adaptive poisoning caused about 31% false victim attribution for 4+ bit canaries at equal exposure and about 59% at double exposure.

## Boundaries and scale limits

CPU-only simulation with 24 sources, 50 seeds, 500 owner and 500 poison samples per condition. Does not test trained-model memorization, decoding, paraphrase robustness, retrieval augmentation, tokenizer effects, or real corpus filtering.

## Claim scope

Synthetic attribution-combinatorics benchmark for natural-text canary codebooks under controlled exact-copy and imperfect slot-mimic poisoning; no language model was trained.

## Why it stopped

Proxy/synthetic early falsification of broad robust-attribution claims: exact-copy adaptive poisoning is a direct false-attribution failure mode for text-only canary attribution, although imperfect mimicry remains promising.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test the same canary/scorer design in a small trained LM with owner, exact-copy poison, and slot-mimic poison splits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM natural-text canary attribution under exact-copy and slot-mimic poisoning
- Success threshold: Useful follow-up if owner recall is at least 0.80 with slot-mimic false victim attribution at most 0.05 at equal exposure, while exact-copy failure is quantified with confidence intervals.
- Stop condition: Stop as unsupported if canary leakage is too rare for attribution, owner recall falls below 0.50 without attack, or exact-copy and slot-mimic attacks both exceed 0.20 false victim attribution at equal exposure.

## Evidence references

- Artifact root: `<local-path>/projects/natural-text-canary-attribution-under-adaptive-poisoning-b0065877bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
