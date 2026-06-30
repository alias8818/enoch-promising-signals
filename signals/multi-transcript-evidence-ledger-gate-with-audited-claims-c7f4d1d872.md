# Multi-Transcript Evidence-Ledger Gate With Audited Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `multi-transcript-evidence-ledger-gate-with-audited-claims-c7f4d1d872`
Run ID: `multi-transcript-evidence-ledger-gate-with-audited-claims-c7f4d1d872-20260527T233341045365+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Agent Transcript Evidence-Ledger Gate: enoch://control-plane/projects/real-agent-transcript-evidence-ledger-gate-5e9d27093b/runs/real-agent-transcript-evidence-ledger-gate-5e9d27093b-20260527T083729626611+0000
- Parent run decision: LLM Agent Evidence-Ledger Gate Test: enoch://control-plane/projects/llm-agent-evidence-ledger-gate-test-aebc52e098/runs/llm-agent-evidence-ledger-gate-test-aebc52e098-20260524T235228082550+0000

## What looked useful

Audited gate achieved precision 0.9974 and recall 0.9612 on 5,000 cases, reducing false positives by 99.50% versus ungated union and 97.67% versus the two-evidence/no-audit ablation. Robustness runs kept audited precision between 0.9962 and 0.9987 and recall between 0.9541 and 0.9700.

## Boundaries and scale limits

Synthetic structured extraction only; no live LLM extraction, no real transcript corpus, no human claim audit, and no retrieval/citation baseline on natural language transcripts. Full run covered 5,000 synthetic cases plus a 9-run robustness grid.

## Claim scope

In controlled synthetic five-transcript bundles with planted true facts, stale contradictions, single-transcript false mentions, and extraction misses, a two-transcript evidence ledger plus contradiction audit improves accepted-claim precision over ungated union and support-only baselines while retaining recall above 0.95.

## Why it stopped

The local result supports the mechanism only in a synthetic structured setting, so it is useful no-paper evidence rather than direct publication-grade validation.

## Recommended next action

Stop paper path for this run; the next concrete step is a bounded real-transcript validation with human-audited atomic claims and live extraction outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Transcript Evidence-Ledger Gate With Human-Audited Atomic Claims
- Success threshold: Audited ledger gate improves precision by >=10 percentage points over the strongest real baseline with recall >=0.85 and statistically non-overlapping 95% bootstrap confidence intervals on claim precision.
- Stop condition: Stop if audited precision gain over the strongest baseline is <5 percentage points, recall falls below 0.80, or human audit shows most accepted claims rely on ambiguous/non-verifiable evidence spans.

## Evidence references

- Artifact root: `<local-path>/projects/multi-transcript-evidence-ledger-gate-with-audited-claims-c7f4d1d872`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
