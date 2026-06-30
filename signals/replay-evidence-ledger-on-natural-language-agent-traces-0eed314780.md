# Replay Evidence Ledger on Natural-Language Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-evidence-ledger-on-natural-language-agent-traces-0eed314780`
Run ID: `replay-evidence-ledger-on-natural-language-agent-traces-0eed314780-20260604T091917440256+0000`

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

- Parent run decision: Tiny Agent Evidence Ledger for Tool Calls: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b/runs/tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b-20260604T065304736695+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ede08e12091f

## What looked useful

Replay-ledger unsupported-claim F1 was 1.00 with case accuracy 1.00, compared with baseline F1 0.25 and case accuracy 0.40 on the same controlled traces; the result supports the mechanism but not publication readiness.

## Boundaries and scale limits

Synthetic controlled traces only; no real LLM-agent trace corpus, no human annotation agreement, no open-domain semantic entailment, and no robustness testing against noisy or adversarial phrasing.

## Claim scope

In a 10-case controlled natural-language trace suite with 12 final claims, a deterministic replay evidence ledger identified unsupported final claims caused by missing evidence, retracted evidence, wrong citations, unresolved conflicts, and derived arithmetic errors better than a final-answer citation-presence baseline.

## Why it stopped

Tier 1 controlled direct test passed the bounded mechanism threshold, but evidence remains synthetic/small and is not paper-grade broad validation.

## Recommended next action

Run a deepen follow-up on at least 50 held-out real or LLM-generated agent traces with independent claim-support labels and compare replay ledger against final-only and entailment baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence ledger on labeled held-out agent traces
- Success threshold: Replay-ledger unsupported-claim F1 >= 0.75 and at least 0.15 absolute F1 improvement over the strongest baseline on held-out labeled traces.
- Stop condition: Stop if replay-ledger F1 is below 0.60 or fails to beat the strongest baseline by at least 0.05 after error analysis on the held-out set.

## Evidence references

- Artifact root: `<local-path>/projects/replay-evidence-ledger-on-natural-language-agent-traces-0eed314780`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
