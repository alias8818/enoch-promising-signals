# Tokenizer Transformer Quality-Quantity Crossover Sweep

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tokenizer-transformer-quality-quantity-crossover-sweep-bf515f447c`
Run ID: `tokenizer-transformer-quality-quantity-crossover-sweep-bf515f447c-20260628T044442679834+0000`

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

- Parent run decision: Quality-Filtered Data Quantity Crossover for Tiny Pretraining: enoch://control-plane/projects/quality-filtered-data-quantity-crossover-for-tiny-pretraining-4249c16c87d6/runs/quality-filtered-data-quantity-crossover-for-tiny-pretraining-4249c16c87d6-20260628T040304566243+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/253d88d48df7

## What looked useful

Morpheme-aware tokenization improved validation NLL per raw character by 39.4%, 31.1%, and 10.2% at 128, 512, and 2048 matched training examples. Extra data for the character tokenizer narrowed the gap and beat the 128-example morpheme run at 2048 examples, but did not beat the 512-example morpheme run.

## Boundaries and scale limits

Synthetic corpus only; oracle tokenizer only; one seed; CPU-only tiny 2-layer Transformer around 107k-110k parameters; no learned BPE/Unigram tokenizer, natural corpus, equal-compute control, GPT-2-small-class baseline, or multi-seed robustness.

## Claim scope

In a single-seed synthetic compositional language with oracle morpheme tokenization, a tiny causal Transformer showed materially better validation NLL per raw character with the morpheme-aware tokenizer than with a character tokenizer at matched raw-example counts; the character tokenizer only crossed over against the smallest morpheme-tokenizer condition after 16x more raw examples.

## Why it stopped

Tier 1 direct synthetic test produced a useful mechanism signal but not publication-grade evidence; finalize as no-paper useful signal rather than continue autonomously.

## Recommended next action

Run a bounded multi-seed learned-tokenizer follow-up on a small real or semi-real corpus, with equal raw-example and equal-compute controls, before considering any larger model escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed learned-tokenizer quality-quantity crossover on a small real corpus
- Success threshold: Across at least 3 seeds, the higher-quality learned tokenizer improves normalized validation loss by at least 10% at matched raw-example counts, and the lower-quality tokenizer's required data multiplier to match it is estimated within the tested grid.
- Stop condition: Stop if the learned tokenizer does not beat the character tokenizer by at least 5% normalized validation loss in 2 of 3 seeds at the smallest two matched dataset sizes, or if runtime exceeds a bounded CPU budget without checkpointed seed-wise metrics.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-transformer-quality-quantity-crossover-sweep-bf515f447c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
