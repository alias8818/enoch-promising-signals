# Evidence Ledger for Small Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-agent-reliability-02afaac6d11d`
Run ID: `evidence-ledger-for-small-agent-reliability-02afaac6d11d-20260527T073424628313+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01d3df5daa94

## What looked useful

Full ledger accuracy was 92.14% versus 61.93% baseline and 81.30% unverified retry. Full ledger reduced unsupported and stale final-answer errors to 0.00% in this oracle-structured harness, at 7.86% abstention.

## Boundaries and scale limits

Synthetic-only, 240 episodes x 8 seeds x 5 conditions; no real LLM, natural-language entailment, adversarial documents, long-horizon autonomy, or production cost/latency validation.

## Claim scope

In a synthetic small-agent harness with oracle-structured entity/field/value/version evidence and injected retrieval or memory faults, a full evidence ledger with support and freshness checks improved reliable completion versus baseline and unverified retry controls.

## Why it stopped

Closed as no-paper useful signal: the mechanism was supported in a synthetic oracle-structured proxy, but this is not direct publication-grade evidence for real small-agent reliability.

## Recommended next action

Run a bounded deepen follow-up with an actual small LLM or tool-using agent on natural-language evidence update tasks, preserving the no-ledger, retry-only, ablation, and full-ledger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language small-agent evidence ledger validation
- Success threshold: Full ledger improves accuracy by at least 5 percentage points over retry-only control while reducing unsupported plus stale error rate by at least 50% relative, with abstention below 20%.
- Stop condition: Stop if the full ledger fails to beat retry-only accuracy or if reduced error rate is explained entirely by abstention above 20%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-reliability-02afaac6d11d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
