# Deterministic evidence ledger for tiny agent reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021`
Run ID: `deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021-20260528T154250896752+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0c44e0cde6a7

## What looked useful

The ledger reduced false accepts from 4198/6000 for a plain transcript to 0/6000 with replay; a no-replay ablation accepted all 1000 replay-drift cases, showing deterministic replay is necessary beyond hash chaining.

## Boundaries and scale limits

Synthetic local deterministic tools only; no real LLM agents, external APIs, concurrent tool use, adversarial cryptographic attack model, production storage, long traces, signature/key management, or human audit workflow was tested.

## Claim scope

In a synthetic 5-tool-call tiny-agent harness, a deterministic hash-chained evidence ledger with answer hashes and deterministic replay accepted 1000/1000 clean traces and rejected 6000/6000 injected corruptions covering stored evidence tampering, action tampering, deletion, reordering, answer tampering, and replay drift.

## Why it stopped

Closed as no-paper useful signal: evidence is direct for the synthetic harness but not broad or realistic enough for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on real small-agent workflows with nondeterministic tool wrappers and a stronger append-only/Merkle-log baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic evidence ledgers on real tiny-agent workflows with replay drift
- Success threshold: Ledger accepts at least 98% of clean real traces, has 0 false accepts on at least 1000 realistic corruptions, and stays below 5 ms p95 verification overhead per short workflow while outperforming the baselines on false accepts.
- Stop condition: Stop if clean real-trace false rejections exceed 5% after deterministic wrappers are added, or if the ledger misses any corruption class that the Merkle baseline catches.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-evidence-ledger-for-tiny-agent-reliability-9329e525f021`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
