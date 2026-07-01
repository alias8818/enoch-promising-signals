# Exact-Dedup vs MinHash Dedup at fixed sequence-item budget for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-dedup-vs-minhash-dedup-at-fixed-token-budget-for-gpt-2-small-41b919b9bffc`
Run ID: `exact-dedup-vs-minhash-dedup-at-fixed-token-budget-for-gpt-2-small-41b919b9bffc-20260619T095642173088+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f26d7f39e047

## What looked useful

Across four fair-budget seeds, MinHash removed all retained near-duplicate pairs with Jaccard >= 0.8, increased selected source clusters by 25.25 on average, increased distinct GPT-2 token 5-grams per 1k by 8.58, and improved clean-eval trigram perplexity by 0.239, while worsening contaminated-eval perplexity by 0.045 and increasing broad eval 5-gram overlap by 0.0476.

## Boundaries and scale limits

No GPT-2-small training was run; corpus was synthetic; downstream model quality was proxied by a smoothed GPT-2-token trigram LM. The initial 120k setting could not be fairly compared because MinHash could not fill the budget from the generated pool.

## Claim scope

On a seeded synthetic web-text-like corpus at a fixed 80k GPT-2 BPE token budget, MinHash-LSH near-deduplication improves corpus diversity and clean n-gram LM proxy performance versus exact dedup, but does not consistently reduce all eval-overlap metrics.

## Why it stopped

Synthetic proxy evidence is mixed and does not directly validate GPT-2-small training outcomes.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded real-corpus GPT-2-family training comparison at equal token budget before making any model-quality claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-family exact-vs-MinHash fixed-token training probe
- Success threshold: MinHash must improve clean validation loss or perplexity by at least 1% versus exact dedup while reducing a predeclared memorization/leakage metric, with no larger than 1% degradation on a contamination-controlled general validation split.
- Stop condition: Stop if MinHash does not improve clean validation loss/perplexity or if leakage reduction comes only with a general-validation regression larger than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/exact-dedup-vs-minhash-dedup-at-fixed-token-budget-for-gpt-2-small-41b919b9bffc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
