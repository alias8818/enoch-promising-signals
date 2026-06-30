# Anchor-Locked Memory Architecture for CPU Agent Loops

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-locked-memory-architecture-for-cpu-agent-loops-eed0f33ce8ca`
Run ID: `anchor-locked-memory-architecture-for-cpu-agent-loops-eed0f33ce8ca-20260621T162659824993+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 10, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- weak evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5e9c9627c941

## What looked useful

Anchor-locked memory reached 1.000 anchor accuracy, 1.000 mutable accuracy, and 0.000 contradiction rate, outperforming transcript search, flat retrieval, and unlocked layered doctrine memory on this proxy suite.

## Boundaries and scale limits

Synthetic proxy only; no live LLM agent, real Enoch trace replay, production memory store, long-horizon pressure, embedding retrieval, or throughput validation.

## Claim scope

On 12 deterministic synthetic repeated-agent replay tasks, anchor-locked memory preserved immutable anchor facts against later contradictory transcript noise while still updating mutable preferences.

## Why it stopped

Closed as a proxy useful-signal result, not a full validation or paper-ready result.

## Recommended next action

Run a bounded real-trace replay comparing anchor-locked memory against transcript search, flat retrieval, and layered doctrine memory on anchor violations, mutable update accuracy, latency, and memory growth.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay of anchor-locked memory for CPU agent loops
- Success threshold: At least 50% lower anchor violation rate than layered_doctrine_memory, mutable update accuracy >= 95%, and less than 20% latency overhead on the replay corpus.
- Stop condition: Stop if anchor_locked_memory fails to reduce anchor violations versus layered_doctrine_memory or if mutable update accuracy drops below 95%.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-locked-memory-architecture-for-cpu-agent-loops-eed0f33ce8ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
