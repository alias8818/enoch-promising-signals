# Optimal Domain-Mix Search for Tiny Pretraining under sequence-item budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `optimal-domain-mix-search-for-tiny-pretraining-under-token-budget-a9bf6454dff9`
Run ID: `optimal-domain-mix-search-for-tiny-pretraining-under-token-budget-a9bf6454dff9-20260619T092306813339+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fc6676296d4e

## What looked useful

Domain mixture affected final target loss, with the best final mixture improving over uniform by 0.0188 nats. However, the early proxy top-1 selector had 0.0342 nats regret versus the final-best mixture and was 0.0154 nats worse than uniform.

## Boundaries and scale limits

Synthetic token domains, tiny Transformer, 160 training steps, 38 unique mixtures, 3 seeds; not evidence for real-corpus or large-model data mixing.

## Claim scope

On a bounded synthetic four-domain tiny Transformer pretraining sweep, exhaustive final-budget mixture search found a better mixture than uniform, but selecting the top mixture by very early validation loss chose a final-worse-than-uniform mixture.

## Why it stopped

Early/proxy falsification of the simple cheap top-1 domain-mix search rule, not a full validation or full rejection of domain-mix optimization.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should evaluate a multi-fidelity top-k scheduler that uses early loss for pruning but performs final-budget checks on several candidate mixtures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-fidelity top-k domain-mix search for tiny pretraining
- Success threshold: Selected mixture final loss within 0.005 nats of exhaustive final-best and at least 0.015 nats better than uniform across at least 5 seeds, while using less than half the full-budget candidate evaluations.
- Stop condition: Stop if promoted top-k candidates are not consistently better than uniform or if pruning removes the final-best region in more than one seed.

## Evidence references

- Artifact root: `<local-path>/projects/optimal-domain-mix-search-for-tiny-pretraining-under-token-budget-a9bf6454dff9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
