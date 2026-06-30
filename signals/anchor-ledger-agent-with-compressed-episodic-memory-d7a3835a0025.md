# Anchor-Ledger Agent with Compressed Episodic Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-ledger-agent-with-compressed-episodic-memory-d7a3835a0025`
Run ID: `anchor-ledger-agent-with-compressed-episodic-memory-d7a3835a0025-20260604T034920977612+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/79f886d5213e

## What looked useful

Repeated-update noisy stream: anchor_ledger temporal_accuracy=1.0000, bytes_vs_raw=0.4140, query_seconds_mean=0.0023; lossy_compressed temporal_accuracy=0.4540 at 0.1202x raw bytes; window temporal_accuracy=0.0509. High fact-density stream: anchor_ledger kept exact recall but used 0.8996x raw bytes, so the mechanism is regime-dependent.

## Boundaries and scale limits

Evidence is synthetic only. It does not test natural-language agent episodes, embedding retrieval, learned summarization, conflict resolution, serialization overhead, or model-in-the-loop behavior. The storage advantage failed the preset <=0.60 raw-byte threshold on high fact-density streams.

## Claim scope

In a synthetic long-horizon fact stream with sparse durable anchors and repeated updates per key, an anchor ledger plus bounded compressed summaries preserves exact current and temporal recall at substantially lower byte footprint than raw full-log memory and much higher temporal accuracy than sliding-window or lossy fixed-slot compression.

## Why it stopped

No-paper closure: the run produced a useful synthetic mechanism signal, but direct agent evidence is missing and the storage target failed on dense fact streams.

## Recommended next action

Run a bounded direct agent-memory benchmark with natural-language episodes, conflict updates, retrieval-index ablations, and implementation-level storage accounting; stop treating this synthetic result as paper evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct natural-language anchor-ledger memory benchmark
- Success threshold: anchor_ledger temporal audit accuracy >= 0.90, at least 0.25 above lossy_compressed and window baselines, with serialized storage <= 0.60x raw_full on at least three random seeds
- Stop condition: Stop if anchor_ledger serialized storage exceeds 0.75x raw_full or temporal audit accuracy advantage over lossy_compressed is below 0.10 on two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-ledger-agent-with-compressed-episodic-memory-d7a3835a0025`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
