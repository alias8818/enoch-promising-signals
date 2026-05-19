# Calibrated Soft Source Diversity for Cross-Corpus Claim Verification

Status: `useful_signal`
Project ID: `calibrated-soft-source-diversity-for-cross-corpus-claim-ve-908672b271`
Run ID: `calibrated-soft-source-diversity-for-cross-corpus-claim-ve-908672b271-20260517T201225170245+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Calibrated Soft Source Diversity for Cross-Corpus Claim Verification: internal_generated:calibrated-soft-source-diversity-for-cross-corpus-claim-ve-908672b271

## What looked useful

Soft source diversity did not improve held-out Climate-FEVER claim verification. With the FEVER-trained model scorer, macro-F1 was 0.3529 versus 0.3531 for no-diversity. With oracle evidence annotations, macro-F1 was 0.8901 versus 0.8929 for no-diversity, with only a small ECE improvement.

## Boundaries and scale limits

No large neural NLI or LLM scorer, no end-to-end retrieval, and only one target corpus with structured multi-evidence source IDs; however the target corpus had 1,381 3-way claims and 90.3% duplicate-source exposure.

## Claim scope

Bounded direct test of calibrated soft duplicate-source diversity for claim-level aggregation on Climate-FEVER, using a FEVER-NLI-trained evidence-pair baseline and an annotation-oracle aggregation control.

## Why it stopped

Bounded direct validation on a real multi-evidence target corpus found no improvement over calibrated no-diversity baselines, and the oracle control also failed on macro-F1 and NLL.

## Recommended next action

Stop this line as a no-paper negative unless a future project changes the mechanism beyond duplicate-source rank penalties; a stronger scorer alone is unlikely to overturn the oracle aggregation failure.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-soft-source-diversity-for-cross-corpus-claim-ve-908672b271`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
