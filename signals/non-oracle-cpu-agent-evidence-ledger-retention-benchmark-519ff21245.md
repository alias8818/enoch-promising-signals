# Non-oracle CPU agent evidence-ledger retention benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `non-oracle-cpu-agent-evidence-ledger-retention-benchmark-519ff21245`
Run ID: `non-oracle-cpu-agent-evidence-ledger-retention-benchmark-519ff21245-20260531T193800890370+0000`

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

- Parent run decision: Evidence-ledger truncation test for multi-step CPU agents: enoch://control-plane/projects/evidence-ledger-truncation-test-for-multi-step-cpu-agents-b3111217f148/runs/evidence-ledger-truncation-test-for-multi-step-cpu-agents-b3111217f148-20260531T095618625702+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

The benchmark found a capacity-sensitive mechanism: the ledger missed the overall threshold across capacities 24/48/96/192 by a small margin (+19.44 pp over recency and +7.95 pp over reservoir), but a capacity sweep from 64 to 256 entries cleared the threshold overall (+39.29 pp over recency and +26.67 pp over reservoir), with per-capacity success beginning at 128 entries.

## Boundaries and scale limits

Synthetic parser-friendly observations only; deterministic extraction and answering; no LLM extraction errors, real agent traces, natural-language ambiguity, multi-step reasoning, adversarial distractors, or end-to-end task success measurement.

## Claim scope

On a synthetic structured CPU retention benchmark with 300 episodes, 480 observations per episode, delayed fact queries, and no future query labels for the tested ledger policy, an online evidence ledger outperforms recency and reservoir baselines once capacity is at least about 128 entries; it does not satisfy the threshold at smaller capacities.

## Why it stopped

Useful bounded synthetic signal, but not paper-positive direct evidence for real CPU agents; the current result should stop as no-paper evidence and feed a deeper real-trace validation.

## Recommended next action

Run a bounded real-trace or LLM-generated trace replay using the same non-oracle online constraint, noisy evidence extraction, and the predeclared +20 pp over recency and +10 pp over reservoir success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace non-oracle evidence-ledger retention replay
- Success threshold: Ledger exact-match retention accuracy exceeds recency by at least 20 percentage points and reservoir by at least 10 percentage points on paired delayed evidence queries, with bootstrap 95% confidence intervals remaining above zero for both gaps.
- Stop condition: Stop negative if the ledger fails to beat reservoir by 10 percentage points at calibrated capacities, or if extraction noise reduces ledger accuracy below recency on the paired replay set.

## Evidence references

- Artifact root: `<local-path>/projects/non-oracle-cpu-agent-evidence-ledger-retention-benchmark-519ff21245`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
