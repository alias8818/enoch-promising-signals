# Real-context benchmark ablation for evidence-ledger gates on small factual QA agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-context-benchmark-ablation-for-evidence-ledger-gates-6c04e7de89`
Run ID: `real-context-benchmark-ablation-for-evidence-ledger-gates-6c04e7de89-20260604T013413754858+0000`

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

- Parent run decision: Evidence ledger gate on small-model factual QA agents: enoch://control-plane/projects/evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff/runs/evidence-ledger-gate-on-small-model-factual-qa-agents-06c47df5ff-20260603T232431027075+0000
- Parent run decision: Evidence Ledger Reduces Hallucination in Tiny Agents: enoch://control-plane/projects/evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249/runs/evidence-ledger-reduces-hallucination-in-tiny-agents-d99cb8d44249-20260603T195533993078+0000

## What looked useful

Ledger_gate improved mean overall accuracy from 0.7615 to 0.8846 versus confidence_gate, improved answer precision from 0.7279 to 0.8762, and reduced wrong-context false answers from 0.2511 to 0.0301. Shuffled ledger ablation dropped to 0.7538 accuracy, supporting that the evidence signal mattered.

## Boundaries and scale limits

Single small extractive QA model; SQuAD answerable examples plus synthetic wrong-context negatives; lexical ledger support only; no generative agent, retrieval stack, Natural Questions/TriviaQA, human citation judging, or semantic entailment baseline.

## Claim scope

On a bounded SQuAD validation stress test using DistilBERT extractive QA, lexical evidence-ledger gating improved held-out reliability versus no gate and confidence-only abstention across three fixed seeds.

## Why it stopped

Medium local evidence supports the mechanism in a bounded stress test but does not satisfy publication-grade breadth or ecological validity.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a second real dataset and a generative small QA agent before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-dataset generative QA replication for evidence-ledger gates
- Success threshold: Across at least two datasets and two agent classes, ledger gating improves overall accuracy by at least 5 percentage points over confidence-only, cuts false answers on negatives by at least 50 percent, and loses no more than 10 percentage points of positive coverage.
- Stop condition: Stop if ledger gains disappear on either the generative agent or naturally unanswerable dataset, or if gains only come from severe positive-coverage collapse.

## Evidence references

- Artifact root: `<local-path>/projects/real-context-benchmark-ablation-for-evidence-ledger-gates-6c04e7de89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
