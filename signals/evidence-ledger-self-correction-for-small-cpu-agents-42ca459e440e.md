# Evidence-Ledger Self-Correction for Small CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e`
Run ID: `evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e-20260525T091321098709+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/be15fec6b4ab

## What looked useful

Evidence-ledger accuracy was 0.9318 versus 0.6970 baseline and 0.7073 reflection-only. Retrieval-miss ablation showed the gain shrank as support coverage fell, consistent with the proposed mechanism.

## Boundaries and scale limits

Synthetic corpus and heuristic noisy-agent proxy only; no real LLM, no real tool logs, no adversarial or stale evidence, and no long-horizon tasks. Main run used 400 records, 600 tasks per seed, and 10 seeds.

## Claim scope

In a fixed-seed synthetic operations-QA harness for small CPU-bound agents, an explicit field-level evidence ledger with contradiction-based revision improved answer accuracy over one-shot and reflection-only baselines when required evidence was retrievable.

## Why it stopped

Closed as no-paper useful signal because the positive evidence is synthetic/proxy-based and not sufficient for a publication-grade agent claim.

## Recommended next action

Run a bounded direct follow-up with a real small local model or CPU tool agent on a public QA/tool benchmark with injected evidence conflicts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger correction on real small-agent tool traces
- Success threshold: Evidence-ledger condition improves accuracy by at least 5 percentage points over both controls while reducing harmful revisions by at least 25% relative to reflection-only on at least 300 evaluated tasks.
- Stop condition: Stop if ledger accuracy gain is under 2 percentage points or harmful revisions are not reduced versus reflection-only after the planned public benchmark run.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-self-correction-for-small-cpu-agents-42ca459e440e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
