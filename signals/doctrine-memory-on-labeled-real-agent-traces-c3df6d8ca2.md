# Doctrine memory on labeled real agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `doctrine-memory-on-labeled-real-agent-traces-c3df6d8ca2`
Run ID: `doctrine-memory-on-labeled-real-agent-traces-c3df6d8ca2-20260629T001704437531+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Reusable doctrine memory on realistic compositional agent traces: enoch://control-plane/projects/reusable-doctrine-memory-on-realistic-compositional-agent-67b16762b5/runs/reusable-doctrine-memory-on-realistic-compositional-agent-67b16762b5-20260628T235654985553+0000
- Parent run decision: Memory That Learns Reusable Operator Doctrine: enoch://control-plane/projects/memory-that-learns-reusable-operator-doctrine-863ce8198019/runs/memory-that-learns-reusable-operator-doctrine-863ce8198019-20260628T233632058055+0000

## What looked useful

The completed local harness produced labeled obligation rows and metrics. On the final completed trace state, doctrine-memory audit reached precision 1.0, recall 1.0, F1 1.0; the trace-only baseline reached precision 1.0, recall 0.333, F1 0.5. This supports the mechanism as an audit/data-construction pattern, but not a paper-grade research claim.

## Boundaries and scale limits

Only one real trace from this worker run was available. Labels are deterministic audit labels derived from the controller doctrine, not independently human-labeled annotations. No model training, cross-run validation, or robustness testing was performed.

## Claim scope

A single local Codex JSONL trace can be converted into deterministic doctrine-obligation labels, and a prompt/doctrine-memory audit can recover Enoch-specific compliance obligations that a no-doctrine trace-only baseline misses.

## Why it stopped

Single-trace deterministic-label evidence is useful for mechanism validation but is too small and too circular for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded corpus of at least 20 real agent traces and independently reviewed obligation labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine-memory audit on a 20-trace real-agent corpus
- Success threshold: Doctrine-memory audit improves macro F1 by >=0.15 over the strongest no-doctrine baseline and maintains precision >=0.85 on required artifact obligations.
- Stop condition: Stop if fewer than 20 usable traces are available, if adjudicated label agreement is below 0.7 Cohen's kappa, or if doctrine-memory F1 gain is below 0.05 after the first 10 traces.

## Evidence references

- Artifact root: `<local-path>/projects/doctrine-memory-on-labeled-real-agent-traces-c3df6d8ca2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
