# Adversarial Evidence-Ledger for CPU-Bound Agent Tool-Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adversarial-evidence-ledger-for-cpu-bound-agent-tool-use-663e78915f36`
Run ID: `adversarial-evidence-ledger-for-cpu-bound-agent-tool-use-663e78915f36-20260619T145102222358+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d5fffda1b4

## What looked useful

Reference-only evidence ledgers are easy to false-accept when evidence exists but contradicts or fails to support the claim. Adding structured predicates for status, numeric metrics, source count, and required/prohibited evidence text caught all adversarial negatives in the bounded fixture set.

## Boundaries and scale limits

Synthetic JSON fixtures only; no live LLM/tool-agent traces, no blinded human labels, and no large heterogeneous benchmark.

## Claim scope

On a 12-case synthetic adversarial evidence-ledger fixture set for CPU-bound agent tool-use claims, structured claim-specific evidence predicates reduced false accepts from 7 to 0 relative to a reference-existence-only ledger gate, with no false rejects on 4 valid controls.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic fixture/proxy evidence, not direct real-agent validation.

## Recommended next action

Run a bounded deepen evaluation on at least 100 real or replayed tool-agent traces with blinded validity labels and compare false accept/reject rates against this strict verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence-ledger false-accept benchmark
- Success threshold: Strict gate cuts false accept rate by at least 50% versus reference-only validation while keeping false reject rate at or below 10% on labeled valid claims.
- Stop condition: Stop if labeled traces cannot be obtained locally or if the strict gate fails to reduce false accepts by at least 25% on the first 50 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-evidence-ledger-for-cpu-bound-agent-tool-use-663e78915f36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
