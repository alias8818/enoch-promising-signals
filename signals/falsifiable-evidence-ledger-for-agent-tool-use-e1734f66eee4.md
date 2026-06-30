# Falsifiable Evidence Ledger for Agent Tool-Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-for-agent-tool-use-e1734f66eee4`
Run ID: `falsifiable-evidence-ledger-for-agent-tool-use-e1734f66eee4-20260602T130412424517+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5aeb7f761b92

## What looked useful

The minimal ledger mechanism produced 1.0 precision and 1.0 recall for 2,939 injected unsupported claims, detected all 1,572 injected tampered entries, and averaged about 0.007 ms/event for build and verify; the transcript baseline had recall 1.0 but only 0.09797 precision due to 27,061 false positives.

## Boundaries and scale limits

Proxy-only local experiment: 30 trials, 30,000 synthetic events total, no real LLM agent, no real tool APIs, no adversarial natural-language traces, no distributed append-only store, no human audit study, and no comparison to production observability systems.

## Claim scope

On deterministic synthetic traces, a hash-linked evidence ledger with event hashes and claim evidence references mechanically detected injected unsupported claims and post-hoc ledger tampering with low runtime overhead, outperforming a brittle unstructured transcript string baseline on precision.

## Why it stopped

Closed as a no-paper useful signal because evidence is synthetic/proxy-only, not full validation on real agent tool-use.

## Recommended next action

Run a bounded real-agent integration test that instruments an agent harness with the ledger and evaluates unsupported-claim and tamper detection on natural tool-use traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Audit Probe
- Success threshold: At least 0.95 precision and 0.95 recall for unsupported-claim and tamper detection on real traces, with less than 5 percent wall-clock overhead and clear baseline comparison.
- Stop condition: Stop as negative if ledger integration cannot preserve stable evidence references on real traces or if precision or recall falls below 0.90 in the controlled audit.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-agent-tool-use-e1734f66eee4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
