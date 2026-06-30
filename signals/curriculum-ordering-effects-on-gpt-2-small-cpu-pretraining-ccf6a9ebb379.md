# Curriculum ordering effects on GPT-2-small CPU pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-ordering-effects-on-gpt-2-small-cpu-pretraining-ccf6a9ebb379`
Run ID: `curriculum-ordering-effects-on-gpt-2-small-cpu-pretraining-ccf6a9ebb379-20260628T165317934506+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6a792cdac89d

## What looked useful

Interleaving beat both easy-to-hard and hard-to-easy schedules on mean all-loss and hard-bucket loss, suggesting curriculum-ordering experiments should include shuffled/interleaved controls before scaling.

## Boundaries and scale limits

Not GPT-2-small, not Transformer architecture, not natural text, not long CPU pretraining; only 10,240 train examples per run and 3 epochs in a toy setup.

## Claim scope

In a three-seed synthetic causal-LM proxy with fixed data multiset and a small NumPy neural n-gram model, simple monotonic curriculum orders did not improve held-out loss over interleaving.

## Why it stopped

The local calibrated proxy found ordered curricula worse than interleaving; this is not full GPT-2-small validation and does not justify a paper-positive decision.

## Recommended next action

Stop this run as a no-paper proxy early falsification; next bounded evidence should train a small Transformer/GPT-2-small-class model on a real text shard with equal token budgets and an interleaved control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer text-shard curriculum ordering control
- Success threshold: A monotonic curriculum must beat interleaving by at least 2% relative held-out all-loss and not degrade the hardest held-out bucket at the same token budget.
- Stop condition: Stop if the ordered curriculum fails to beat interleaving on mean held-out all-loss after the planned token budget or shows worse hard-bucket loss in at least 2 of 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-effects-on-gpt-2-small-cpu-pretraining-ccf6a9ebb379`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
