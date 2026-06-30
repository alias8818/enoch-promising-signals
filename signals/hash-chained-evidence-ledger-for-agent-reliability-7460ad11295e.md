# Hash-Chained Evidence Ledger for Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e`
Run ID: `hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e-20260628T164251261647+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/deb7aa3d971c

## What looked useful

Anchored hash-chain verification detected 100/100 tested tamper cases with zero false positives on 20 clean ledgers, while unanchored verification missed truncation and full rehash rewrites, detecting 60/100.

## Boundaries and scale limits

Synthetic traces only: 20 seeds, 200 tasks per seed, 600 entries per ledger, 100 tampered ledgers. No real LLM/tool-agent traces, distributed append-only storage, signatures, operator workflow, or human trust calibration were tested.

## Claim scope

In a deterministic synthetic agent evidence ledger, canonical SHA-256 hash chaining detects unrehashed payload edits, deletion, and reorder; detection of tail truncation and validly rehashed alternate histories requires verifying against the original trusted head hash.

## Why it stopped

Closed as no-paper useful signal: the local synthetic mechanism test supports the need for external anchoring, but it is not deployment-level or paper-positive evidence for agent reliability.

## Recommended next action

Run a bounded deepen follow-up on real tool-using agent traces with an external signed or append-only trusted-head anchor and compare false accept/reject rates against plain logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Evidence Ledger on Real Agent Tool Traces
- Success threshold: Anchored verification detects at least 99% of injected tamper cases with no more than 1% false rejects on clean real traces, and overhead remains below 10% of trace processing time.
- Stop condition: Stop if anchored verification misses any rehashed rewrite or truncation with a valid stored trusted head, or if false rejects exceed 1% on clean traces after canonicalization defects are fixed.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
