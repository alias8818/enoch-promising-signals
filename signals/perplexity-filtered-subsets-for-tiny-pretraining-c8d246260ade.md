# Perplexity-Filtered Subsets for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtered-subsets-for-tiny-pretraining-c8d246260ade`
Run ID: `perplexity-filtered-subsets-for-tiny-pretraining-c8d246260ade-20260525T002327465558+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7fbc702656d

## What looked useful

Low-perplexity filtering reduced mean held-out clean PPL from 3.9754 for random subsets to 3.0088 and won 5/5 seeds. High-perplexity filtering selected mostly noise and failed badly with mean PPL 11.6469. Mid-perplexity filtering removed noise but selected mostly corrupted documents and underperformed random with mean PPL 4.2899.

## Boundaries and scale limits

Synthetic corpus only; clean/noise separation was generated and easy; held-out evaluation was clean in-domain only; target model was a tiny transformer trained for 180 steps per policy, not GPT-2-small-class or larger; no real tokenizer, web corpus, downstream task, or long-run scaling evidence.

## Claim scope

In a controlled synthetic tiny-pretraining setup with known clean, corrupted, and noise documents, a small clean in-domain scorer used for low-perplexity filtering selected the clean slice and improved clean held-out perplexity versus equal-size random subsets across 5 seeds.

## Why it stopped

No-paper closure: this run produced reproducible synthetic mechanism evidence, but it is proxy evidence rather than direct real-corpus pretraining validation.

## Recommended next action

Run a bounded real-corpus follow-up using a small public text corpus, fixed tokenizer, multiple retained fractions, and GPT-2-small-class or parameter-matched tiny baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus retained-fraction test for perplexity-filtered tiny pretraining
- Success threshold: Low or low-mid perplexity filtering improves held-out validation PPL by at least 5% versus equal-token random in at least 3 seeds while preserving diversity diagnostics within 10% of random.
- Stop condition: Stop if filtered subsets fail to beat random by 5% in two retained fractions or if gains are explained by duplicate/easy-text collapse.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-subsets-for-tiny-pretraining-c8d246260ade`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
