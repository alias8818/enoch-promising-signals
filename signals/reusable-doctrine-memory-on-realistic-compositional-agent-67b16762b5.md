# Reusable doctrine memory on realistic compositional agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `reusable-doctrine-memory-on-realistic-compositional-agent-67b16762b5`
Run ID: `reusable-doctrine-memory-on-realistic-compositional-agent-67b16762b5-20260628T235654985553+0000`

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

- Parent run decision: Memory That Learns Reusable Operator Doctrine: enoch://control-plane/projects/memory-that-learns-reusable-operator-doctrine-863ce8198019/runs/memory-that-learns-reusable-operator-doctrine-863ce8198019-20260628T233632058055+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aa15f41a92c5

## What looked useful

Doctrine memory outperformed nearest-trace episodic reuse on held-out compositions: at 3% label noise, OOD micro-F1 was 0.9977 vs 0.8668 and exact match was 0.9724 vs 0.1222. At 10% label noise, OOD micro-F1 was 0.9912 vs 0.8576 and exact match was 0.8969 vs 0.1075.

## Boundaries and scale limits

No real production traces, no natural-language extraction from messy logs, no live agent intervention, and no datacenter-scale validation. Runs were CPU-only: 50 seeds at 3% label noise plus 20 seeds at 10% label noise.

## Claim scope

Controlled synthetic benchmark only: compact doctrine rules learned from generated multi-label agent traces transferred to held-out higher-order feature compositions when component doctrines were observable in training.

## Why it stopped

Closed as no-paper useful signal because the evidence is generated-trace proxy evidence, not direct validation on realistic compositional agent traces.

## Recommended next action

Run a bounded direct-evidence follow-up on 200-1000 real or public agent traces with doctrine/action labels and a predeclared held-out composition split.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine memory on labeled real agent traces
- Success threshold: Doctrine memory improves OOD composition micro-F1 by at least 0.05 and recall by at least 0.10 over nearest-trace retrieval, with precision drop no worse than 0.03.
- Stop condition: Stop if real-trace doctrine labels cannot be obtained locally/publicly, or if doctrine memory fails to beat nearest-trace retrieval on OOD micro-F1 in two independently seeded splits.

## Evidence references

- Artifact root: `<local-path>/projects/reusable-doctrine-memory-on-realistic-compositional-agent-67b16762b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
