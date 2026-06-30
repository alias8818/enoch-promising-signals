# Falsifiable Evidence Ledger for Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-for-tool-calling-agents-fd8f738424c2`
Run ID: `falsifiable-evidence-ledger-for-tool-calling-agents-fd8f738424c2-20260604T063850973277+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/368bec57e31c

## What looked useful

Ledger unsupported-claim recall was 1.000 versus 0.496 for transcript overlap; bootstrap mean unsupported-recall improvement was 0.505 with 95% interval [0.460, 0.548]. The mechanism is useful for citation and freshness defects but not validated as a broad agent-reliability result.

## Boundaries and scale limits

1,000 synthetic cases, one deterministic generator, simple transcript baseline, no real LLM traces, no production tools, no human audit labels, and no semantic entailment baseline.

## Claim scope

On a seeded synthetic benchmark where support is exact cited-field equality plus latest-evidence freshness, a falsifiable evidence ledger detects unsupported tool-agent final claims that a transcript-overlap audit accepts.

## Why it stopped

Synthetic mechanism evidence met the useful-signal threshold but is proxy evidence, not direct real-agent validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should test the ledger on real tool-calling agent traces with oracle labels and a stronger verifier baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Audit Benchmark
- Success threshold: Ledger unsupported-claim recall improves by at least 0.15 absolute over the strongest baseline while supported-claim false rejection remains below 0.10.
- Stop condition: Stop if oracle labeling cannot be produced reproducibly or if the ledger improvement over the strongest baseline is below 0.05 absolute on at least 100 traces.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-tool-calling-agents-fd8f738424c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
