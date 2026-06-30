# Domain-mix ratio grid: does the held-out optimum transfer across seeds?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mix-ratio-grid-does-the-held-out-optimum-transfer-across-seeds-cde710f6af7f`
Run ID: `domain-mix-ratio-grid-does-the-held-out-optimum-transfer-across-seeds-cde710f6af7f-20260619T142032411388+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/616dd4252f11

## What looked useful

Exact optimum identity transferred in only 9.09% of cross-seed pairs. Mean cross-seed regret from transferring a source seed's optimum was 0.01018 balanced accuracy, while the best global mean ratio had 0.00701 mean regret versus the per-seed oracle.

## Boundaries and scale limits

Synthetic domains only; logistic model only; 792 short CPU fits; no real corpus, tokenizer, neural language model, large-scale pretraining, or long-run training dynamics tested.

## Claim scope

In a deterministic synthetic three-domain logistic-classification benchmark with 12 seeds and a 0.1 simplex ratio grid, exact held-out-optimal domain-mix ratios were not seed-stable, but a global mean-best ratio retained most per-seed oracle performance.

## Why it stopped

No-paper closure: the local synthetic evidence is a useful seed-transfer probe, but it is not direct language-model/domain-corpus evidence and does not justify a publication-grade claim.

## Recommended next action

Run a bounded deepen follow-up on a real multi-domain text corpus with a small language model and the same cross-seed ratio-transfer analysis before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-LM domain-mix seed-transfer grid
- Success threshold: Useful confirmation if exact optimum transfer is below 25% while global-ratio mean regret is at most 0.010 validation loss or equivalent normalized metric; stop as negative if regret exceeds 0.020 for most cross-seed pairs.
- Stop condition: Stop after the fixed seed x ratio grid completes or after a reproducible execution blocker prevents training/evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-ratio-grid-does-the-held-out-optimum-transfer-across-seeds-cde710f6af7f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
