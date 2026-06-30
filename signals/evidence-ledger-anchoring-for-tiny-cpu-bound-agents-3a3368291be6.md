# Evidence-ledger anchoring for tiny CPU-bound agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6`
Run ID: `evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6-20260529T101321005606+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

Ledger anchoring gave 1.000 answer accuracy, 1.000 exact-evidence rate, 1.000 tamper rejection, and 0.019 ms mean query latency, versus rolling-memory accuracy from 0.026 to 0.824 and unanchored full-scan 1.000 accuracy but 0.000 tamper rejection and 1.000 undetected tamper rate.

## Boundaries and scale limits

The benchmark is synthetic and schema-keyed; it does not test a real LLM policy, natural-language ambiguity, real tool traces, long multi-turn planning, or production-scale ledgers. The largest completed run was 11.41 seconds wall clock and 33.9 MiB max RSS on a CPU worker.

## Claim scope

In a deterministic synthetic CPU-only event-stream benchmark with 1k entities, 20 update steps, 2k queries, and 5 seeds, an append-only hash-anchored evidence ledger preserved exact evidence, matched full-history retrieval accuracy, detected silent evidence corruption, and was substantially more accurate than bounded rolling-memory agents once the stream exceeded context capacity.

## Why it stopped

Synthetic deterministic evidence supports the mechanism but is not direct enough for a paper claim about real tiny CPU-bound language agents.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same ledger anchoring protocol in a bounded local small-model agent harness with natural-language evidence and the same rolling-memory and unanchored full-history controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger anchoring in a local tiny language-agent harness
- Success threshold: Ledger anchoring improves supported-answer rate by at least 20 percentage points over rolling memory, matches or exceeds unanchored full-history answer accuracy, achieves at least 0.95 tamper rejection, and keeps median query latency under 2x the unanchored retrieval baseline.
- Stop condition: Stop if ledger anchoring fails to improve supported-answer rate by 10 percentage points over rolling memory or if latency exceeds 5x unanchored retrieval on the bounded local harness.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-anchoring-for-tiny-cpu-bound-agents-3a3368291be6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
