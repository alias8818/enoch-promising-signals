# N-gram dedup threshold sweep for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-dedup-threshold-sweep-for-tiny-pretraining-d0dfbf0e96b3`
Run ID: `n-gram-dedup-threshold-sweep-for-tiny-pretraining-d0dfbf0e96b3-20260629T210353702420+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a1bc16d9a396

## What looked useful

Duplicate removal rate alone was misleading in this tiny pretraining setup: aggressive thresholds reduced leak-like duplicate exposure but did not produce a clean held-out loss gain, and the most aggressive 0.35 threshold was worse on aggregate.

## Boundaries and scale limits

Small WikiText-derived corpus, controlled mutations, 2-layer tiny Transformer, 260 optimizer steps per threshold, word-level tokenizer, three seeds; not evidence for web-scale corpora, GPT-2-small-class models, long training, or downstream benchmarks.

## Claim scope

On a three-seed WikiText-2 tiny Transformer proxy with controlled near-duplicate contamination, lower word 5-gram Jaccard dedup thresholds reliably removed duplicate variants but did not improve clean validation loss over the no-dedup control.

## Why it stopped

Replicated bounded evidence supports the deduplication mechanism but not the utility-improvement hypothesis; this is a proxy/tiny-pretraining result, not full validation.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test real near-duplicate clusters under a fixed-token-budget training design before considering larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real near-duplicate cluster dedup threshold sweep with fixed sequence-item budget
- Success threshold: A moderate threshold beats no-dedup on mean clean validation loss by more than one seed standard deviation while reducing duplicate-target memorization exposure by at least 25%.
- Stop condition: Stop if duplicate removal again fails to improve clean validation loss across at least three seeds or if natural clusters are too sparse to create a valid threshold comparison.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-dedup-threshold-sweep-for-tiny-pretraining-d0dfbf0e96b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
