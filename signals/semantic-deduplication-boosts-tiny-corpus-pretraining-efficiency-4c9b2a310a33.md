# Semantic Deduplication Boosts Tiny Corpus Pretraining Efficiency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-deduplication-boosts-tiny-corpus-pretraining-efficiency-4c9b2a310a33`
Run ID: `semantic-deduplication-boosts-tiny-corpus-pretraining-efficiency-4c9b2a310a33-20260601T054711934474+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Semantic dedup reduced train tokens by 80.0% versus raw at duplicate multiplier 5 and improved validation NLL by 1.1135 versus raw and 0.3442 versus exact dedup; a duplicate-intensity sweep from multipliers 1 to 8 kept the semantic-dedup validation advantage over exact dedup near 0.33-0.35 NLL.

## Boundaries and scale limits

Synthetic generated corpus, controlled synonym-map semantic key, 112 retained semantic units, tiny neural n-gram LM, five seeds per setting, no real web corpus and no transformer/GPT-2-scale training.

## Claim scope

In a controlled synthetic tiny-corpus setting with injected paraphrase duplicates, a small NumPy neural trigram LM trained for equal SGD update budgets achieved lower held-out NLL after semantic deduplication than after raw training or exact-string deduplication.

## Why it stopped

No-paper closure: the result is a useful controlled mechanism signal, but it is synthetic/toy evidence and not a full validation of semantic deduplication for real tiny-corpus pretraining.

## Recommended next action

Run a bounded deepen experiment on a small real corpus using non-oracle semantic embeddings or MinHash-style near-dedup plus a parameter-matched transformer baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus semantic deduplication for tiny transformer pretraining
- Success threshold: Semantic dedup beats exact dedup by at least 0.05 validation NLL or reaches the exact-dedup best validation NLL with at least 20% fewer train tokens across repeated runs without hurting test NLL.
- Stop condition: Stop as unsupported if semantic dedup does not beat exact dedup on held-out NLL or token efficiency in repeated real-corpus runs, or if benefits disappear under equal-token controls.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-deduplication-boosts-tiny-corpus-pretraining-efficiency-4c9b2a310a33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
