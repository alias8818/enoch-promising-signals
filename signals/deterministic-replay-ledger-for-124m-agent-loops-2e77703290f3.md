# Deterministic Replay Ledger for 124M Agent Loops

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-replay-ledger-for-124m-agent-loops-2e77703290f3`
Run ID: `deterministic-replay-ledger-for-124m-agent-loops-2e77703290f3-20260524T205636865355+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

The mechanism worked in the bounded benchmark: replay digest matched, tamper detection succeeded, naive reruns matched 0/5 times, record throughput was 19,478.8 loops/s, replay throughput was 23,544.5 loops/s, and measured storage projected to about 317.1 GiB JSONL or 83.6 GiB gzip for 124M loops at the synthetic event density.

## Boundaries and scale limits

The run used deterministic synthetic agents and tools, not real LangGraph/OpenAI-agent execution, real LLM sampling, real API/tool payloads, concurrent writers, crash recovery, or distributed storage. The 124M-loop storage/runtime figures are projections from a 100k-loop local proxy.

## Claim scope

In a CPU-only synthetic 8-agent loop benchmark, an append-only JSONL replay ledger that records scheduler order, per-step entropy, model decisions, tool observations, and a Blake2 hash chain replayed 100,000 loops exactly, detected tampering, and made naive rerun divergence observable.

## Why it stopped

The current evidence is a synthetic proxy that supports the mechanism but is not direct/full validation of a 124M-loop production agent ledger.

## Recommended next action

Stop this run as no-paper useful signal; next, implement the same ledger boundary in a real LangGraph/OpenAI-agent workload and require exact replay across crash/restart and tool-response replay tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph replay ledger integration with crash-restart validation
- Success threshold: Exact replay digest match on all tested real traces, tamper detection on injected mutation, crash/restart recovery from a ledger prefix, and compressed storage below 2 KiB per loop.
- Stop condition: Stop as negative if replay mismatches cannot be resolved without recording full opaque process snapshots, or if representative compressed storage exceeds 10 KiB per loop before full prompts/responses are included.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-ledger-for-124m-agent-loops-2e77703290f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
