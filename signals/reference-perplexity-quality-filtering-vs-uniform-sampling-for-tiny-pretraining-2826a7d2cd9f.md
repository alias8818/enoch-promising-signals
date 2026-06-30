# Reference-perplexity quality filtering vs uniform sampling for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `reference-perplexity-quality-filtering-vs-uniform-sampling-for-tiny-pretraining-2826a7d2cd9f`
Run ID: `reference-perplexity-quality-filtering-vs-uniform-sampling-for-tiny-pretraining-2826a7d2cd9f-20260619T195314530649+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/175b264212ca

## What looked useful

Low reference-PPL filtering beat uniform in 5/5 seeds by -0.0757 held-out bits/char on average and selected about 74 fewer contamination chunks than uniform at the same token budget; high reference-PPL selection was worse than uniform in 5/5 seeds.

## Boundaries and scale limits

No neural transformer training, no real web-corpus mixture, no pretrained neural reference scorer, and no large-scale or overnight validation were run.

## Claim scope

On a bounded CPU n-gram proxy using Tiny Shakespeare plus injected synthetic contamination, low reference-perplexity filtering improves held-out clean character-LM bits/char versus uniform equal-token sampling.

## Why it stopped

No-paper useful signal: proxy evidence supports the mechanism, but direct neural tiny-pretraining evidence on real mixed data is still required.

## Recommended next action

Run the same equal-token strategy matrix with a small neural causal LM on naturally mixed corpus shards before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural tiny-LM reference-perplexity filtering on real mixed shards
- Success threshold: Low-reference-PPL selection improves clean held-out validation loss versus uniform equal-token sampling in at least 3/3 seeds without a larger off-domain loss regression than the all-data baseline.
- Stop condition: Stop if low-reference-PPL fails to beat uniform in two seeds or if gains disappear when synthetic contamination is replaced by naturally mixed corpus shards.

## Evidence references

- Artifact root: `<local-path>/projects/reference-perplexity-quality-filtering-vs-uniform-sampling-for-tiny-pretraining-2826a7d2cd9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
