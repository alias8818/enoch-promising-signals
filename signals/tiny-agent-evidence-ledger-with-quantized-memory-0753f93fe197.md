# Tiny agent evidence ledger with quantized memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-with-quantized-memory-0753f93fe197`
Run ID: `tiny-agent-evidence-ledger-with-quantized-memory-0753f93fe197-20260528T232413560894+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/862178abae9a

## What looked useful

Across five seeds, int8 and int4 maintained about 0.976 mean target top-5 retrieval and at least 0.962 top-1 agreement with float32, while shuffled-memory control target top-5 stayed near 0.003 and binary sign memory averaged only 0.504 target top-5.

## Boundaries and scale limits

Synthetic retrieval-only proxy; no real agent loop, no learned embeddings, no dynamic ledger writes, no contradiction handling, no latency under service load, and no downstream answer-accuracy benchmark.

## Claim scope

In a synthetic static evidence ledger using deterministic hashed text embeddings at 2048 records, row-wise int8 and int4 quantized memory preserved float-like retrieval utility while reducing storage by about 4x and 8x respectively; binary sign memory was too lossy.

## Why it stopped

No-paper useful signal: local synthetic evidence supports int8/int4 quantized retrieval memory but is not direct/full validation of agent evidence-ledger performance.

## Recommended next action

Run a bounded real-agent ledger benchmark with append/update operations and downstream answer accuracy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent quantized evidence ledger benchmark
- Success threshold: int8 and int4 each achieve at least 95% of float32 downstream answer accuracy and at least 0.95 retrieval top-5 recall, with at least 3x storage reduction and binary/shuffled controls clearly worse.
- Stop condition: Stop if int4 or int8 drops below 90% of float32 answer accuracy on two independent splits, or if retrieval fidelity fails despite synthetic success.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-with-quantized-memory-0753f93fe197`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
