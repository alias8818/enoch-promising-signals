# Evidence-ledger replay falsifies hallucinated tool calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-replay-falsifies-hallucinated-tool-calls-3e311acd64a1`
Run ID: `evidence-ledger-replay-falsifies-hallucinated-tool-calls-3e311acd64a1-20260530T012911816760+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e6f3dc984d66

## What looked useful

Replay against an independently recorded signed hash chain rejected 900/900 mutated tool-call claim cases and accepted 100/100 clean cases; a transcript-only baseline falsely accepted 900/900 mutated cases.

## Boundaries and scale limits

Synthetic local cases only; no real LLM transcripts, production orchestration, concurrent tool calls, streaming calls, crash recovery, or adversarial runtime integration were tested.

## Claim scope

In a deterministic synthetic replay harness, a signed hash-chained evidence ledger falsified transcript tool-call claims that were extra, altered, omitted, reordered, or ledger-tampered, while accepting clean matching claims.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct production or publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; next concrete step is a real agent-runtime integration that captures actual tool events before transcript generation and replays them under retries, concurrency, and streaming.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-runtime evidence ledger replay for agent tool calls
- Success threshold: At least 200 real-runtime cases with 0 false accepts for unsupported tool-call claims and no more than 1% false rejects on clean supported claims.
- Stop condition: Stop if instrumentation cannot capture authoritative pre-transcript tool events, or if any unsupported real-runtime tool-call claim is accepted by replay after ledger integrity validation.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-replay-falsifies-hallucinated-tool-calls-3e311acd64a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
