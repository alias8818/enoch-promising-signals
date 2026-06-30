# Live-agent commitment-window context under controlled truncation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-agent-commitment-window-context-under-controlled-trun-4aecf6f875`
Run ID: `live-agent-commitment-window-context-under-controlled-trun-4aecf6f875-20260619T030331507954+0000`

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

- Parent run decision: Commitment-Window Agent Context: enoch://control-plane/projects/commitment-window-agent-context-1cf940282a36/runs/commitment-window-agent-context-1cf940282a36-20260619T021652117396+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/18122a9b386e

## What looked useful

Commitment preservation across a controlled truncation boundary appears to require durable state. A local commitment_ledger.json was sufficient for exact recovery in all tested trials; absent visible context or durable state, the agent did not infer or leak the hidden token.

## Boundaries and scale limits

Small synthetic commitment-token task; simulated truncation boundary; one live agent stack; four trials per condition; no real controller compaction, adversarial ledger conflicts, long histories, or cross-model replication.

## Claim scope

In a 12-trial controlled live Codex CLI test, visible commitments and truncation-with-local-ledger commitments were recovered exactly, while hard-truncated commitments without durable state were not recovered and produced UNKNOWN.

## Why it stopped

Tier 1 direct test completed and produced a useful mechanism signal, but the evidence is too small and synthetic for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up using a real multi-turn hard-cutover/compaction harness with at least 30 randomized commitments, conflicting-ledger controls, and predeclared exact-recall and no-leak thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real multi-turn commitment ledger under hard-cutover compaction
- Success threshold: >=0.90 exact recall for visible and truncated-ledger commitments, >=0.90 UNKNOWN with zero exact hidden-token leaks for truncated-blind commitments, and no systematic failure on conflict controls.
- Stop condition: Stop if truncated-ledger exact recall falls below 0.75 after 20 trials, if any blind condition leaks the exact hidden token from unavailable context, or if the harness cannot produce real cutover evidence.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-commitment-window-context-under-controlled-trun-4aecf6f875`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
