# Domain-mix Pareto sweep for code+text tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-mix-pareto-sweep-for-code-text-tiny-pretraining-1b7703a70cc0`
Run ID: `domain-mix-pareto-sweep-for-code-text-tiny-pretraining-1b7703a70cc0-20260621T041606800272+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3adb369ee78e

## What looked useful

Pure text minimized text loss but failed code; pure code minimized code loss but failed text. Every sampled ratio was Pareto-efficient. Best balanced mix shifted from 75% code at 300 steps (balanced loss 1.7591) to 50% code at 1000 steps (balanced loss 0.2168), indicating mixture recommendations are horizon-dependent even in a tiny controlled setup.

## Boundaries and scale limits

Synthetic corpora, character tokenizer, 4-layer 128-wide Transformer, two seeds per horizon, 300 and 1000 optimization steps. No real corpus, GPT-style tokenizer, GPT-2-small-class baseline, long-horizon pretraining, or downstream evaluation was run.

## Claim scope

In a deterministic synthetic character-level tiny-LM proxy, fixed-token code/text mixture sweeps produce a monotonic code-vs-text Pareto frontier; intermediate mixtures outperform pure-domain training on balanced held-out code/text loss.

## Why it stopped

No-paper closure: the run produced a reproducible useful proxy signal, but synthetic char-level evidence is insufficient for a publication-grade code+text pretraining claim.

## Recommended next action

Run a bounded follow-up on real public Python/prose corpora with a GPT-style tokenizer, at least 3 seeds, and multiple token budgets to test whether the horizon-dependent balanced optimum persists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny GPT domain-mix horizon sweep
- Success threshold: At least one intermediate mixture improves mean balanced validation loss by >=5% over both pure-domain endpoints at two token budgets, with consistent Pareto tradeoff across at least 3 seeds.
- Stop condition: Stop as negative if no intermediate mixture beats both pure endpoints on balanced loss by 5% at any measured token budget, or if results are seed-unstable enough that confidence intervals overlap all candidate mixtures.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-pareto-sweep-for-code-text-tiny-pretraining-1b7703a70cc0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
