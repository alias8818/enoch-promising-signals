# Real-text exact-token QWED selection with loss guardrail

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-exact-token-qwed-selection-with-loss-guardrail-f8e8bdcace`
Run ID: `real-text-exact-token-qwed-selection-with-loss-guardrail-f8e8bdcace-20260518T202605789551+0000`

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

- Internal Enoch project: Real-text exact-token QWED selection with loss guardrail: internal_generated:real-text-exact-token-qwed-selection-with-loss-guardrail-f8e8bdcace

## What looked useful

Raw exact-token QWED retrieval was harmful, but adding a loss guardrail improved mean test mixture NLL versus distilgpt2 in all three seeds and beat unweighted, random, and shuffled controls. The same method hurt top-1 accuracy, so the result supports only a bounded retrieval-assisted probability-smoothing mechanism.

## Boundaries and scale limits

Single corpus, single GPT-2-class model, 32-token contexts, 3 seeds, 2000 test windows per seed, inference-only mixture evaluation; no larger-model, larger-corpus, long-context, generation-quality, or training-time validation.

## Claim scope

On WikiText-2 with distilgpt2, 30k exact-token QWED retrieval candidates, 2k validation/test windows per seed, and three fixed seeds, a validation-tuned LM-loss guardrail produced a small mean test mixture-NLL improvement over the dense LM baseline while lowering top-1 accuracy.

## Why it stopped

Medium local Tier 2 evidence is mixed: guarded QWED improves mixture NLL slightly but degrades top-1 accuracy and is too narrow for publication-grade support.

## Recommended next action

Stop this run as no-paper useful evidence; a future bounded deepen test should evaluate calibrated top-k QWED interpolation on a second real corpus and require NLL improvement without top-1 degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated top-k QWED interpolation on a second real corpus
- Success threshold: Mean test NLL improves by at least 0.02 versus the dense LM on both corpora, all seeds are non-worse on NLL, and top-1 accuracy is no more than 0.005 absolute below the dense LM baseline.
- Stop condition: Stop if top-k calibrated QWED fails to beat the dense LM mean NLL on either corpus or still reduces top-1 accuracy by more than 0.005 absolute.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-exact-token-qwed-selection-with-loss-guardrail-f8e8bdcace`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
