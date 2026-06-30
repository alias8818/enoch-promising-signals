# Domain mix ratio sweep for tiny CPU pretraining transfer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mix-ratio-sweep-for-tiny-cpu-pretraining-transfer-6c224609e0d0`
Run ID: `domain-mix-ratio-sweep-for-tiny-cpu-pretraining-transfer-6c224609e0d0-20260619T210702843845+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b904a67997da

## What looked useful

Small source pretraining budgets improved target-only fine-tuning, but larger source budgets caused negative transfer for every ratio. The 70% code-like target mixture did not favor the 0.75 code source ratio.

## Boundaries and scale limits

Synthetic domains, count-based trigram model, 10 seeds, <=20k pretraining tokens per ratio; does not validate neural transformer, real corpus, or larger-scale pretraining behavior.

## Claim scope

In a synthetic tiny CPU add-alpha trigram language-model transfer proxy, source-domain mix ratio did not produce a stable target-matched optimum; pretraining-token budget versus target fine-tune weight dominated transfer behavior.

## Why it stopped

No-paper useful signal: the local proxy falsified a simple stable target-matched ratio story and identified pretraining-budget dominance as the next mechanism to test.

## Recommended next action

Run a bounded tiny neural LM or count-decay follow-up that controls source-count dominance before spending compute on larger domain-ratio sweeps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny neural domain-mix sweep with source-count reweighting control
- Success threshold: A non-extreme source ratio beats target-only and both single-domain extremes by at least 0.02 nats/token mean target NLL after fine-tune across seeds, or the follow-up reproduces negative transfer across all ratios.
- Stop condition: Stop if all source ratios are worse than target-only in two independent bounded configurations, or if per-seed winners remain spread with <0.01 nats/token mean separation.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-ratio-sweep-for-tiny-cpu-pretraining-transfer-6c224609e0d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
