# Hash-chained evidence ledger for small local agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808`
Run ID: `hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808-20260609T132655290717+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a08a821698a2

## What looked useful

Hash-chained MAC-protected JSONL detected payload edits, unsigned local rehashing, middle deletion, and suffix truncation with a trusted head in 6/6 measurement cases. It failed to detect suffix truncation without a trusted head in 6/6 cases, showing anchoring is mandatory for that threat model. Median write-time overhead was 1.175x and median file-size overhead was 1.721x versus baseline JSONL.

## Boundaries and scale limits

Single-process CPU-only Python harness; synthetic events only; no real agent traces, concurrent writers, crash injection, long-running operation, remote notary, privacy review, or production filesystem adversary model.

## Claim scope

Synthetic local JSONL evidence ledgers up to 10,000 entries and 2,048-byte target payloads can use per-entry payload hashes, previous-entry hashes, and keyed MACs to detect common local tampering with low absolute CPU cost, provided verifiers retain a trusted head hash or checkpoint.

## Why it stopped

Bounded local evidence supports a practical mechanism but is not novel or broad enough for a paper; it also demonstrates that hash chains require external head anchoring to detect suffix truncation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test concurrent append, crash recovery, and checkpoint anchoring on realistic local-agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent crash-safe anchored evidence ledger for local agents
- Success threshold: Across at least 100,000 realistic events and four concurrent writers, detect 100% of injected payload edits, middle deletions, rollback, and anchored truncation attacks; maintain p95 append latency under 10 ms and recover after injected crashes without silent acceptance of corrupted ledgers.
- Stop condition: Stop if concurrent append cannot avoid silent corruption under crash injection, if checkpoint anchoring misses any rollback/truncation attack, or if p95 append latency exceeds 10 ms by more than 2x after straightforward batching and locking improvements.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-small-local-agents-0f380ac31808`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
