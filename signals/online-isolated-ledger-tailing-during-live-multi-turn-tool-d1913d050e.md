# Online isolated ledger tailing during live multi-turn tool-use traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `online-isolated-ledger-tailing-during-live-multi-turn-tool-d1913d050e`
Run ID: `online-isolated-ledger-tailing-during-live-multi-turn-tool-d1913d050e-20260518T211723532363+0000`

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

- Internal Enoch project: Online isolated ledger tailing during live multi-turn tool-use traces: internal_generated:online-isolated-ledger-tailing-during-live-multi-turn-tool-d1913d050e

## What looked useful

Across 10 fixed seeds and 10,000 expected events per variant, isolated_atomic and isolated_no_fsync recovered 10,000/10,000 events with zero parse errors under partial-write fault injection. The shared JSONL baseline recovered 9,787/10,000 events with 242 parse errors. A no-fault control showed all variants recover 10,000/10,000 events, so the isolated-ledger advantage is fault containment rather than raw speed.

## Boundaries and scale limits

Synthetic local traces only; no real Codex/LangGraph production traces, no actual process-kill syscall timing, no power-loss recovery, no network filesystems, and no multi-process concurrent writer stress.

## Claim scope

In a deterministic local benchmark of live multi-turn tool-use trace emission, isolated per-event ledger tailing recovered all events under partial-write fault injection while a shared JSONL tailing baseline missed events after corrupt writes.

## Why it stopped

No-paper closure: Tier 2 local evidence supports the mechanism, but the result remains synthetic/proxy evidence and is not publication-grade direct validation on real live tool-use infrastructure.

## Recommended next action

Run a bounded deepen study on real Codex/LangGraph trace traffic with process-kill fault injection and restart recovery; stop paper pursuit for this synthetic-only run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real trace restart recovery for isolated ledger tailing
- Success threshold: Across at least 10 fixed seeds and at least 50,000 real trace events total, isolated ledger tailing has >=99.9% completeness, zero corrupt records surfaced to tailers, no order violations within a run, p95 tail latency <25 ms, and p95 durable write overhead <10 ms while outperforming the baseline by at least 10x on missing/corrupt events under fault injection.
- Stop condition: Stop if isolated ledger tailing misses any committed event after restart, surfaces corrupt records to the tailer, exceeds 25 ms p95 tail latency or 10 ms p95 durable write overhead in two independent seeds, or fails to improve missing/corrupt events over the real baseline.

## Evidence references

- Artifact root: `<local-path>/projects/online-isolated-ledger-tailing-during-live-multi-turn-tool-d1913d050e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
