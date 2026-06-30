# Real-trace prefix verifier versus token-loss curation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2`
Run ID: `real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2-20260629T084412212920+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Early-token reasoning quality scorer for post-training data curation: enoch://control-plane/projects/early-reasoning-quality-token-loss-curation-20260628/runs/early-reasoning-quality-token-loss-curation-20260628-20260629T062713910921+0000
- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-207 frontier research issue: linear-ALI-207
- Linear ALI-208 frontier research issue: linear-ALI-208
- Early-token reasoning quality scorer for post-training data curation: https://arxiv.org/abs/2606.26797v1

## What looked useful

On 1,208 eligible GSM8K test traces expanded into 3,624 candidates, the verifier accepted exactly the original trace in every group (1.0 group-exact rate, 0 FP, 0 FN). Token-loss curation selected the original as lowest-NLL in only 53.4% of groups and had 72.2% pairwise original-lower-NLL rate.

## Boundaries and scale limits

No downstream training, no model-generated candidate traces, one generic causal LM scorer, one dataset format, and a narrow verifier that only covers explicit arithmetic annotations plus final numeric answers.

## Claim scope

For GSM8K-style human-written traces with explicit <<expr=result>> annotations and a #### final numeric answer, a deterministic prefix/final arithmetic verifier selected the original trace over controlled arithmetic-corrupted variants far more reliably than distilgpt2 answer-token mean NLL.

## Why it stopped

Bounded local evidence supports the mechanism, but the result is proxy/controlled-corruption evidence rather than full validation on model-generated traces or downstream training.

## Recommended next action

Stop this run as a no-paper useful signal; next, test the same curation criteria on model-generated GSM8K candidate traces and evaluate final-answer correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier versus token-loss curation on model-generated GSM8K traces
- Success threshold: Verifier-selected traces improve final-answer correctness by at least 10 percentage points over token-loss selection with non-overlapping bootstrap confidence intervals on the bounded problem set.
- Stop condition: Stop if fewer than 50% of generated traces contain verifier-compatible arithmetic annotations, or if verifier selection is not at least 5 percentage points better than token-loss selection after 300 problems.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
