# Positional Entropy Filtering for Long-Context Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `positional-entropy-filtering-for-long-context-tiny-pretraining-bcc07d761c77`
Run ID: `positional-entropy-filtering-for-long-context-tiny-pretraining-bcc07d761c77-20260529T114531598047+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c54bb4f578ef

## What looked useful

PEF is useful as a degeneracy filter but positional entropy alone is insufficient: a high-entropy-noise confound is selected similarly to learnable copy data, and the tiny transformer did not show reliable long-context accuracy gains.

## Boundaries and scale limits

No real text, tokenizer artifacts, GPT-2-small-class model, >64-token contexts, downstream benchmark, or datacenter-scale pretraining was run. Evidence is synthetic and CPU-bounded.

## Claim scope

Synthetic 64-token long-copy corpora on a tiny 1-layer CPU causal transformer: late-position entropy filtering perfectly removes low-entropy degenerate tails and gives a small short-run loss improvement, but does not produce robust copy accuracy or a persistent training advantage.

## Why it stopped

Early synthetic mechanism probe found selection behavior but not robust training-performance support; this is a proxy negative/useful signal rather than full validation.

## Recommended next action

Stop this run as no-paper evidence; a bounded follow-up should test PEF plus a learnability/control score against high-entropy noise before any real pretraining scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy-plus-learnability filtering under high-entropy tail confounds
- Success threshold: Entropy-plus-learnability must retain at least 90% copy-document selection in the degenerate pool, select at least 25% fewer noise-tail documents than entropy-only PEF in the confound pool, and improve held-out late-copy accuracy by at least 2 percentage points over random and entropy-only in three seeds.
- Stop condition: Stop if the combined score does not reject high-entropy noise or if copy accuracy remains at chance after the longer persistence budget.

## Evidence references

- Artifact root: `<local-path>/projects/positional-entropy-filtering-for-long-context-tiny-pretraining-bcc07d761c77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
