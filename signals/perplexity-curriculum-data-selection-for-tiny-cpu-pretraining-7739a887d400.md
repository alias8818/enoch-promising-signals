# Perplexity-curriculum data selection for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-curriculum-data-selection-for-tiny-cpu-pretraining-7739a887d400`
Run ID: `perplexity-curriculum-data-selection-for-tiny-cpu-pretraining-7739a887d400-20260526T025941014651+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Perplexity sorting is risky as a curriculum control in this tiny CPU setting: easy-first ordering was 2.01% worse than random and hard-first was 9.85% worse. Perplexity filtering looked at most weakly useful, with low-ppl selection only 0.23% better than random and a rough paired confidence interval including zero.

## Boundaries and scale limits

The test used a character-level MLP language model, one small corpus, three seeds, 240 updates per policy, and a trigram proxy scorer. It does not validate transformer pretraining, subword tokenization, multi-corpus data selection, long-run convergence, or large-scale compute regimes.

## Claim scope

In a bounded Tiny Shakespeare CPU experiment with a tiny NumPy character language model, naive proxy-perplexity curriculum ordering did not improve held-out perplexity over random ordering, while low-perplexity filtering produced only a negligible 0.23% mean validation-perplexity improvement over random across three seeds.

## Why it stopped

Bounded local evidence is mixed-to-negative for the curriculum-ordering hypothesis and the only positive filtering effect is too small for a paper claim.

## Recommended next action

Stop this run as no-paper useful evidence; a direct follow-up should test low-perplexity filtering, not ordering, on a small transformer with a modern tokenizer and equal-token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer test of proxy-perplexity filtering versus random selection
- Success threshold: Low-perplexity filtering beats random selection by at least 1% validation perplexity in the paired mean on both corpora, with no degradation on either corpus and ordering policies not counted as success.
- Stop condition: Stop if low-perplexity filtering is within +/-0.5% of random or worse on either corpus after three seeds, or if ordering again degrades validation perplexity by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-curriculum-data-selection-for-tiny-cpu-pretraining-7739a887d400`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
