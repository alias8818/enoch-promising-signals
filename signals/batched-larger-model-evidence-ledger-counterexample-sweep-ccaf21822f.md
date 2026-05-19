# Batched Larger-Model Evidence Ledger Counterexample Sweep

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `batched-larger-model-evidence-ledger-counterexample-sweep-ccaf21822f`
Run ID: `batched-larger-model-evidence-ledger-counterexample-sweep-ccaf21822f-20260517T141732813419+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Batched Larger-Model Evidence Ledger Counterexample Sweep: internal_generated:batched-larger-model-evidence-ledger-counterexample-sweep-ccaf21822f

## What looked useful

The larger-model role-diverse ledger beat random search by +59.0 paired points but lost to the same-model repeated generalist baseline by -3.7 paired points after parser-corrected rescoring; ledger gains on modular tasks were offset by regressions on sparse_needles and boundary_low.

## Boundaries and scale limits

Synthetic integer universal-claim tasks only; one local 7B-class quantized model; no real production evidence ledgers, theorem provers, software-verification traces, human labels, closed models, or natural counterexamples.

## Claim scope

On a 300-task fixed-seed generated integer counterexample benchmark using local Qwen2.5-7B-Instruct-Q4_K_M batched inference, a four-role blinded evidence-ledger sweep did not outperform four same-model generalist passes under the same candidate budget.

## Why it stopped

Direct local larger-model validation failed the paper-readiness threshold against a real same-model, same-budget baseline; this is a useful counterexample/control result, not publication-grade positive evidence.

## Recommended next action

Stop this follow-up chain at depth 4; treat the result as a bounded no-paper counterexample showing that larger-model generalist passes can erase the earlier heuristic-agent ledger advantage.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/batched-larger-model-evidence-ledger-counterexample-sweep-ccaf21822f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
