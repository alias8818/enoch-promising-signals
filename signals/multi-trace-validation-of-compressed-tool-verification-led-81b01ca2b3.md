# Multi-Trace Validation of Compressed Tool Verification Ledgers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-trace-validation-of-compressed-tool-verification-led-81b01ca2b3`
Run ID: `multi-trace-validation-of-compressed-tool-verification-led-81b01ca2b3-20260604T021654827635+0000`

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

- Parent run decision: Compressed State Ledger for Small Agent Tool Verification: enoch://control-plane/projects/compressed-state-ledger-for-small-agent-tool-verification-36d639504452/runs/compressed-state-ledger-for-small-agent-tool-verification-36d639504452-20260603T183845227647+0000
- Parent run decision: Real-Agent Trace Test for Compressed Tool Verification Ledgers: enoch://control-plane/projects/real-agent-trace-test-for-compressed-tool-verification-led-2374e109c8/runs/real-agent-trace-test-for-compressed-tool-verification-led-2374e109c8-20260604T003038546915+0000

## What looked useful

Mechanism works for digest-backed tamper validation and payload digest ablations fail as expected, but the average storage target was missed and hash chaining was not necessary for the tested threat model.

## Boundaries and scale limits

Synthetic traces only; no production traces; compact binary storage was byte-accounted rather than implemented as an encoder/decoder; no cryptographic collision, privacy leakage, concurrent merge, or cross-trace adversarial attack validation; full-chain necessity was not supported because the no-chain ablation also detected all generated tamper cases.

## Claim scope

On deterministic synthetic multi-trace tool logs with 500 traces x 32 events across three profiles and three fixed seeds, a compact full-chain verification ledger accepted clean traces and detected/localized all generated input, output, tool, deletion, insertion, and adjacent-reorder tamper trials; compact binary storage averaged 0.4008 of gzip-full logs, not the predeclared 0.3333 threshold.

## Why it stopped

Tier 2 fixed-seed validation produced a mixed useful signal but missed the predeclared 3x smaller-than-gzip-full storage threshold on average and did not show a detection advantage for the hash-chain component.

## Recommended next action

Run a bounded deepen follow-up with an actual packed binary ledger implementation, real or replayed tool traces, and cross-trace/order attacks that specifically test whether hash chaining adds value beyond ordered per-event digests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed Binary Ledger Validation on Realistic Tool Traces and Cross-Trace Attacks
- Success threshold: Full-chain packed ledger has clean accept rate 1.0, tamper detection at least 0.995 overall and above no-chain on cross-trace/order attack families, and compact bytes at most 0.3333 of gzip-full bytes averaged across trace regimes.
- Stop condition: Stop if packed full-chain storage remains above 0.3333 of gzip-full bytes on average or if no-chain controls match full-chain detection on cross-trace/order attack families.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-validation-of-compressed-tool-verification-led-81b01ca2b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
