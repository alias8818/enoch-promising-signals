# Early-token reasoning quality scorer for post-training data curation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `early-reasoning-quality-token-loss-curation-20260628`
Run ID: `early-reasoning-quality-token-loss-curation-20260628-20260629T062713910921+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-207 frontier research issue: linear-ALI-207
- Linear ALI-208 frontier research issue: linear-ALI-208
- Early-token reasoning quality scorer for post-training data curation: https://arxiv.org/abs/2606.26797v1

## What looked useful

Prefix-only parseability, grounding, and arithmetic consistency scored 0.6599 ROC-AUC versus 0.4460 for a length baseline on 5,000 synthetic traces; top-10% selection precision improved from 0.420 to 0.632. Stratification showed the mechanism works for early defects but fails on late arithmetic errors and penalizes valid format-noise traces.

## Boundaries and scale limits

Synthetic traces only; no real model generations, no token-loss baseline from an LM, no downstream post-training run, and no long-context or multi-domain reasoning validation. First-step scoring is blind to late errors and brittle to format variation.

## Claim scope

On synthetic two-step arithmetic reasoning traces with controlled injected errors, an auditable first-step prefix scorer improves final-correct trace selection over a length-like baseline and identifies early arithmetic/grounding failures.

## Why it stopped

No-paper closure: the evidence is a bounded synthetic proxy that supports a useful mechanism but does not directly validate post-training curation on real model traces or downstream training outcomes.

## Recommended next action

Run a bounded direct follow-up on real generated GSM8K-style traces comparing prefix-verifier filtering against token-loss, random, and length controls, with retained correctness and a small downstream SFT/DPO delta as target metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace prefix verifier versus token-loss curation
- Success threshold: At 10% and 25% retention, prefix-verifier filtering improves retained final-correct precision by at least 5 percentage points over token-loss and length baselines, and the filtered dataset improves downstream exact-match accuracy by at least 1 point over the best control in a repeated small-model run.
- Stop condition: Stop if prefix-verifier precision is not better than token-loss or length at matched retention, or if downstream training shows no repeatable gain despite better retained correctness.

## Evidence references

- Artifact root: `<local-path>/projects/early-reasoning-quality-token-loss-curation-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
