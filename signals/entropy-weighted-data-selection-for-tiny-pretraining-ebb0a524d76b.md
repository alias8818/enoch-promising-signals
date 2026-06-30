# Entropy-weighted data selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-weighted-data-selection-for-tiny-pretraining-ebb0a524d76b`
Run ID: `entropy-weighted-data-selection-for-tiny-pretraining-ebb0a524d76b-20260605T125615335770+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2d4671d07106

## What looked useful

Entropy weighting produced small budget-dependent changes: it slightly beat random at 2% and 20% budgets but lost at 5% and 10% across alpha values 1, 4, and 8. High-entropy-only and low-entropy-only selection were consistently worse than random, indicating entropy extremes are poor standalone selection criteria in this proxy.

## Boundaries and scale limits

Single small English literary corpus, byte-level entropy, byte n-gram proxy model, 100k validation bytes, four data budgets, five stochastic seeds for random and entropy-weighted policies; no neural LM, tokenizer, large-corpus, or downstream validation.

## Claim scope

On Tiny Shakespeare with 512-byte chunk selection and a byte 5-gram language-model proxy, raw chunk entropy weighting did not reliably improve validation NLL over random selection at matched byte budgets; selecting only entropy extremes was consistently harmful.

## Why it stopped

Proxy/early falsification of naive raw chunk entropy weighting as a reliable tiny-pretraining improvement; not a full validation of entropy-aware data selection.

## Recommended next action

Stop this no-paper run; if deepening, run a bounded neural causal-LM confirmation with matched token budgets and the same selection controls before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM confirmation of entropy-aware chunk selection
- Success threshold: Entropy-weighted selection must improve mean validation loss by at least 2% relative to random at both tested budgets without worse seed instability; otherwise confirm the negative proxy signal.
- Stop condition: Stop if entropy-weighted selection loses to random at either budget or if high-entropy-only selection remains worse than random with no compensating downstream benefit.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-weighted-data-selection-for-tiny-pretraining-ebb0a524d76b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
