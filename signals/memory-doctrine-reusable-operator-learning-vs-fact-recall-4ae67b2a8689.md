# Memory Doctrine: Reusable Operator Learning vs Fact Recall

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689`
Run ID: `memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689-20260610T234620332680+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9d36ccd668d

## What looked useful

Across 20 seeds with 4096 entities, 64 relations, 128 train facts/relation, and 512 held-out facts/relation, the XOR operator learner reached 1.0000 held-out accuracy on clean structured facts, 0.8998 under 10% target noise, and 0.000241 on random facts, matching a 0.000246 random floor. Fact recall had 0.0000 held-out accuracy. Full query-space table lookup would require about 157.5x the operator representation memory in this proxy.

## Boundaries and scale limits

Synthetic algorithmic proxy only; no neural model training, natural-language facts, learned representations, interference tests, or large-scale validation were run.

## Claim scope

In a bounded synthetic bit-string task, reusable XOR operator inference generalizes from sparse observed facts to held-out entity/relation pairs and rejects random-fact controls; exact fact recall only answers observed pairs.

## Why it stopped

The mechanism is supported in a synthetic proxy, but this is not direct neural or language-model evidence and is insufficient for a paper-positive decision.

## Recommended next action

Stop this run as a no-paper useful synthetic signal; next bounded test should train a small neural model on the same structured/noisy/random protocol and compare learned operator transfer against a parameter-matched fact-memory baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Reusable Operator Transfer vs Fact Memory Baseline
- Success threshold: Neural operator model exceeds 0.95 held-out accuracy on clean structured facts, reaches at least 0.80 under 10% noise, stays within 2x random floor on random-fact controls, and beats the fact-memory baseline by at least 50 percentage points on held-out structured pairs at comparable parameter/storage budget.
- Stop condition: Stop if the neural model cannot exceed 0.50 held-out accuracy on clean structured facts after a calibrated small sweep, or if it also generalizes on random-fact controls above 0.05, indicating leakage or an invalid protocol.

## Evidence references

- Artifact root: `<local-path>/projects/memory-doctrine-reusable-operator-learning-vs-fact-recall-4ae67b2a8689`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
