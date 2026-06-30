# Tiny neural LM validation for proxy-perplexity data filtering

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-neural-lm-validation-for-proxy-perplexity-data-filter-338fb0f594`
Run ID: `tiny-neural-lm-validation-for-proxy-perplexity-data-filter-338fb0f594-20260609T151531887890+0000`

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

- Parent run decision: Proxy perplexity filter for tiny pretraining: enoch://control-plane/projects/proxy-perplexity-filter-for-tiny-pretraining-69e5df8f15a1/runs/proxy-perplexity-filter-for-tiny-pretraining-69e5df8f15a1-20260609T080913756306+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/482d9398fb58

## What looked useful

Confirmation run met the predeclared threshold: low-proxy filtering improved mean downstream validation NLL by 10.78% versus random, beat random in 3/3 seeds, and high-proxy selection was much worse. Low-proxy selected 90/90 target documents in each confirmation seed and approached the oracle-clean control.

## Boundaries and scale limits

Synthetic document generators, 3 seeds, tiny NumPy character MLP LMs, short CPU-only training, no real web corpus, no transformer baseline, no large-scale or production data filtering validation.

## Claim scope

In a controlled synthetic mixed-corpus Tier 1 test, a tiny neural proxy character LM trained on a small clean target seed selected data that trained a downstream tiny neural character LM to lower held-out target NLL than random or high-proxy selected data.

## Why it stopped

No-paper closure: controlled Tier 1 direct mechanism evidence is useful but synthetic and too small for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a small real text corpus using the same proxy low/random/high controls and a small transformer or GPT-2-small-class downstream LM before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-corpus proxy-perplexity filtering validation with transformer downstream LM
- Success threshold: Low-proxy selection improves mean held-out target NLL by at least 5% versus random, beats random in at least 2 of 3 seeds, and high-proxy selection is worse than low-proxy.
- Stop condition: Stop as unsupported if low-proxy fails to beat random in at least 2 of 3 seeds or the mean NLL improvement is below 2% while high-proxy is not clearly worse.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-neural-lm-validation-for-proxy-perplexity-data-filter-338fb0f594`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
