# Real trace replay for evidence ledger and counterexample logging

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-replay-for-evidence-ledger-and-counterexample-l-23a59b1dc1`
Run ID: `real-trace-replay-for-evidence-ledger-and-counterexample-l-23a59b1dc1-20260605T195848357432+0000`

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

- Parent run decision: Agent reliability via evidence ledger and counterexample logging: enoch://control-plane/projects/agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693/runs/agent-reliability-via-evidence-ledger-and-counterexample-logging-d150c89c3693-20260605T161915922832+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/7be7d2f361d0

## What looked useful

The bounded replay harness passed the original real trace with zero counterexamples, detected all four injected perturbation scenarios, validated the ledger hash chain, and reproduced the same ledger head on repeat replay.

## Boundaries and scale limits

One local trace snapshot, 36 events, four simple perturbation classes; no multi-project corpus, concurrent trace streams, production service integration, schema migration testing, or adversarial filesystem threat model.

## Claim scope

A single real Enoch/Codex worker JSONL trace snapshot can be replayed into a deterministic hash-chained evidence ledger, and four controlled perturbation classes are recorded as linked counterexamples with 100% detection in this Tier 1 test.

## Why it stopped

Tier 1 direct mechanism support was obtained, but the result is no-paper because it is a single-trace bounded validation rather than broad or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up on 20 or more independent Enoch/Codex traces with at least 8 perturbation classes and report original-pass rate, injected-detection rate, runtime, and counterexample taxonomy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace replay robustness for evidence ledger counterexample logging
- Success threshold: At least 95% original trace pass rate, 100% injected perturbation scenario detection, 100% valid ledger chains, and deterministic ledger heads for repeat replay on every passing trace.
- Stop condition: Stop if original-pass rate is below 90% due to schema brittleness or any perturbation class has below 100% detection after one targeted harness fix.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-replay-for-evidence-ledger-and-counterexample-l-23a59b1dc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
