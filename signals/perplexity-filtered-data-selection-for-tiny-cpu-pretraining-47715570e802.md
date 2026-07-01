# Perplexity-Filtered Data Selection for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtered-data-selection-for-tiny-cpu-pretraining-47715570e802`
Run ID: `perplexity-filtered-data-selection-for-tiny-cpu-pretraining-47715570e802-20260529T171813488237+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c54bb4f578ef

## What looked useful

Low-perplexity filtering was useful when the candidate pool was contaminated and the scorer matched the target distribution: 16/16 paired wins over random, 0.4407 mean NLL reduction, and 13.46% mean relative NLL improvement. The mechanism was target-like chunk enrichment.

## Boundaries and scale limits

Synthetic contamination only; byte-level neural bigram model only; no transformer, subword tokenizer, real web-noise mixture, downstream task, or long-horizon pretraining validation.

## Claim scope

In a bounded CPU experiment using real text8 as the target corpus and synthetic off-domain/noisy contamination, a byte-bigram low-perplexity selector improved a tiny NumPy byte-level neural LM's held-out target NLL versus matched random selection across 16 paired runs.

## Why it stopped

No-paper useful signal: the local evidence supports the contamination-filtering mechanism but remains a bounded proxy because noise is synthetic and the tiny model is not a transformer.

## Recommended next action

Run a bounded real-off-domain follow-up with a small transformer and matched sequence-item budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real off-domain contamination test for perplexity-filtered tiny transformer pretraining
- Success threshold: Low-perplexity selection beats matched random and the quality/diversity control by at least 2% held-out target loss across at least 3 paired seeds while retaining at least 80% of random's distinct n-gram diversity.
- Stop condition: Stop as no-paper if low-perplexity selection fails to beat random by 1% mean held-out target loss or wins fewer than 2 of 3 paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-data-selection-for-tiny-cpu-pretraining-47715570e802`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
