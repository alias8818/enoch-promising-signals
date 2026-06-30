# Difficulty-Routed Curriculum for Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `difficulty-routed-curriculum-for-home-training-150e98c2a670`
Run ID: `difficulty-routed-curriculum-for-home-training-150e98c2a670-20260524T195316236679+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a9550f8d4233

## What looked useful

Difficulty awareness appears useful for scarce-update training on this controlled noisy-hard task: at 150 updates, loss-routed sampling improved final accuracy by +0.00642 and hard-band accuracy by +0.02034 versus uniform, with approximate paired 95% CIs above zero. The effect disappeared at 300 updates and was inconclusive at 600 updates, while classic easy-to-hard was consistently worse.

## Boundaries and scale limits

Synthetic tabular task only; small MLP only; no language model, real corpus, token-level difficulty estimator, real home-training workload, or long-run validation. The 600-update run used 5 seeds; 150/300 update sweeps used 10 seeds.

## Claim scope

On a synthetic home-scale binary classification task with controlled easy/medium/hard strata and train-only hard-label noise, difficulty-aware sampling improved scarce-budget 150-update accuracy versus uniform, but adaptive loss routing did not beat a simpler hard-focus control and did not provide stable gains at 300 or 600 updates.

## Why it stopped

Proxy evidence produced a useful scarce-budget signal but did not support the broader difficulty-routed home-training hypothesis as paper-ready; final gains were small or absent outside the 150-update regime and adaptive routing did not clearly outperform a simpler hard-focus control.

## Recommended next action

Run a bounded direct language-model follow-up on a tiny corpus with equal token budgets, comparing uniform, hard-focus, easy-to-hard, and adaptive loss-routed sampling under 150-300 update scarce-budget conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-LM Scarce-Budget Difficulty Routing
- Success threshold: Adaptive loss-routed sampling improves mean validation perplexity by at least 2% versus uniform and at least 1% versus hard-focus at the same token budget, with no worse memorization/noise diagnostic in at least 4 of 5 seeds.
- Stop condition: Stop if adaptive routing fails to beat uniform or hard-focus on mean validation perplexity, or if gains come only from repeatedly sampling high-loss/noisy examples.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-routed-curriculum-for-home-training-150e98c2a670`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
