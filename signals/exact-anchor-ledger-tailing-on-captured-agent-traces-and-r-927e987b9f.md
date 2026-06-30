# Exact-anchor ledger tailing on captured agent traces and real collector baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `exact-anchor-ledger-tailing-on-captured-agent-traces-and-r-927e987b9f`
Run ID: `exact-anchor-ledger-tailing-on-captured-agent-traces-and-r-927e987b9f-20260528T110333461073+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Online exact-anchor ledger tailing across live small-agent tool events: enoch://control-plane/projects/online-exact-anchor-ledger-tailing-across-live-small-agent-579cfa14f1/runs/online-exact-anchor-ledger-tailing-across-live-small-agent-579cfa14f1-20260528T072031145547+0000
- Parent run decision: Exact-anchor ledger on real small-agent traces: enoch://control-plane/projects/exact-anchor-ledger-on-real-small-agent-traces-062e6318fb/runs/exact-anchor-ledger-on-real-small-agent-traces-062e6318fb-20260528T034503278129+0000

## What looked useful

The mechanism cleanly separates collection from exact-once resume and audit integrity: exact_anchor_ledger had min recall 1.0, duplicate rate 0.0, and detected rotation/truncation plus tamper; offset_only fell to 0.5 recall under rotation and duplicated after restart; whole_file_hash_poll kept recall but duplicated after restart and did not flag tamper.

## Boundaries and scale limits

Local CPU-only replay; GNU tail -F baseline only covered 500-event rename rotation; no production Fluent Bit/vector/filebeat deployment, concurrent writers, network shipping, power-loss crash recovery, non-JSON logs, or multi-day traces.

## Claim scope

On local replay of 5,000 captured agent JSONL events into growing files, an exact-anchor chained ledger tailer preserved exact event order and recall across partial append, copy-truncate rotation, rename rotation, restart/resume, and historical valid-JSON tamper, while exposing integrity evidence missing from offset and polling baselines.

## Why it stopped

Bounded local threshold was met, but evidence remains local captured-trace replay with limited real collector coverage rather than publication-grade production collector validation.

## Recommended next action

Stop short of paper writing; the next useful bounded deepen test is production-collector replay against Fluent Bit/vector/filebeat with crash/backpressure injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production collector replay for exact-anchor trace ledgers
- Success threshold: Exact-anchor sidecar preserves recall >= 0.999, duplicate rate <= 0.001, detects all injected tamper/truncation cases, and adds <= 20% CPU overhead or <= 10 ms p95 per-event latency relative to each collector baseline.
- Stop condition: Stop if any production collector integration loses more than 0.1% events, duplicates more than 0.1% events after restart, fails to detect injected tamper/truncation, or exceeds the overhead threshold on 100k events.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-tailing-on-captured-agent-traces-and-r-927e987b9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
