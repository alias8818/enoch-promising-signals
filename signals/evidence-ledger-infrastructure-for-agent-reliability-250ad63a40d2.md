# Evidence ledger infrastructure for agent reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2`
Run ID: `evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2-20260607T052838375790+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2b828dab0d6c

## What looked useful

A small reproducible probe found that ledger structure makes provenance faults mechanically checkable at microsecond-scale local overhead, while the unstructured transcript baseline missed unsupported, stale, and tampered evidence faults hidden in plausible transcript wording.

## Boundaries and scale limits

Synthetic traces only; baseline is a lightweight unstructured transcript scanner; no real LLM agents, strong LLM judge baseline, human annotation burden, production persistence, distributed ledger operation, or downstream reliability improvement was tested.

## Claim scope

In deterministic synthetic agent traces with injected unsupported-claim, stale-evidence, tampered-evidence, and contradiction faults, a structured evidence ledger with support edges, hashes, freshness requirements, and predicate checks detects these provenance faults with perfect measured recall and no false positives across 10,000 generated cases.

## Why it stopped

Synthetic/proxy-only evidence supports the mechanism but is not broad or direct enough for a paper-positive reliability claim.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded real/replayed agent-trace study using a stronger transcript or LLM-judge baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger verification on real or replayed agent-tool traces
- Success threshold: Ledger recall >= 0.95, false-positive rate <= 0.02, stronger-baseline recall advantage >= 0.20 on non-contradiction provenance faults, and p95 verification latency below 1 ms per trace.
- Stop condition: Stop if ledger recall is below 0.80, false-positive rate exceeds 0.05, annotation overhead is impractical for the trace format, or the stronger baseline matches ledger recall within 0.05 without ledger structure.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
