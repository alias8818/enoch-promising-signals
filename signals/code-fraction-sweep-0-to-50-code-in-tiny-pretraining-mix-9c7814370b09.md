# Code fraction sweep: 0% to 50% code in tiny pretraining mix

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `code-fraction-sweep-0-to-50-code-in-tiny-pretraining-mix-9c7814370b09`
Run ID: `code-fraction-sweep-0-to-50-code-in-tiny-pretraining-mix-9c7814370b09-20260610T104338876003+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000b52be0247

## What looked useful

The sweep found a clear tradeoff: 50% code reduced code heldout loss by 90.6% and 50/50 mixed loss by 83.5% versus 0% code, but increased prose loss by 12.5%. Robust 3-gram and 7-gram probes agreed on the rank pattern.

## Boundaries and scale limits

Synthetic templates, byte n-gram models, 500k training bytes per condition, 10 seeds, no neural transformer, no real corpus, no tokenizer study, and no downstream benchmark accuracy.

## Claim scope

In a synthetic fixed-budget byte n-gram proxy with 0% to 50% code-like data, adding code sharply improves code and balanced heldout likelihood while monotonically worsening prose-only heldout likelihood.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic n-gram proxy, not direct neural or real-corpus pretraining evidence.

## Recommended next action

Run a bounded deepen follow-up with a tiny transformer/tokenizer on real prose and code shards to test whether the same code-loss gain and prose-retention cost appear in neural pretraining.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural LM real-corpus code fraction sweep
- Success threshold: The follow-up succeeds if 10% or more code reduces code heldout loss by at least 20% versus 0% code while prose heldout loss increases by less than 10%, or if it clearly falsifies that tradeoff with matched controls.
- Stop condition: Stop if the 0% and code-mixed runs cannot be matched for token budget and architecture, or if a smoke run exceeds the local CPU/GPU budget without producing checkpointed heldout losses.

## Evidence references

- Artifact root: `<local-path>/projects/code-fraction-sweep-0-to-50-code-in-tiny-pretraining-mix-9c7814370b09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
