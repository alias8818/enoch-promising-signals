# Code/NLP Mix Ratio Sweep for Tiny Mixed-Domain Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f`
Run ID: `code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f-20260611T214922817279+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c7cadde24a06

## What looked useful

The run validates a compact reproducible sweep harness and shows the expected mixed-domain tradeoff: code-only and NLP-only training overfit their own domain objective, while a mid-ratio mixture substantially improves balanced held-out loss in this toy setting.

## Boundaries and scale limits

Synthetic template corpora only; character tokenizer only; 300 training steps per run; 2 seeds; no real-code corpus, real NLP corpus, downstream task, long-horizon training, or larger model validation.

## Claim scope

In a synthetic tiny mixed-domain pretraining sweep with a 354,578-parameter character-level causal Transformer, fixed token budget, 5 code/NLP sampling ratios, and 2 seeds, a 50% code mixture gave the best unweighted mean of held-out synthetic code and NLP losses, while single-domain extremes won only their matching domain.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but does not provide publication-grade or real-corpus validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace synthetic templates with small real code and NLP corpora while keeping the same ratio sweep and fixed token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Tiny Code/NLP Mix Ratio Sweep
- Success threshold: An intermediate ratio must improve balanced held-out loss by at least 5% over both single-domain extremes and avoid more than 20% degradation on either individual domain probe relative to the domain-specialist run.
- Stop condition: Stop if no intermediate ratio beats both extremes on balanced held-out loss across the majority of seeds, or if real-corpus data preparation dominates the run without producing train/eval splits.

## Evidence references

- Artifact root: `<local-path>/projects/code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
