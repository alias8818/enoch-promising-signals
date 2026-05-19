# Real-runtime signed provenance ledger evaluation for agent actions

Status: `useful_signal`
Project ID: `real-runtime-signed-provenance-ledger-evaluation-for-agent-f56187a255`
Run ID: `real-runtime-signed-provenance-ledger-evaluation-for-agent-f56187a255-20260516T021802902034+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40feb6f09d0c

## What looked useful

Tier 1 controlled direct test supports the mechanism: signed ledgers verified cleanly, persisted and reverified after reload, detected all tested tamper cases across 20 trials, and exposed the expected hash-only weakness where adaptive rehash tampering passed hash-only verification.

## Boundaries and scale limits

Synthetic actions only; no real Codex or LangGraph runtime integration, no concurrent appenders, no networked append-only storage, no key rotation or hardware-backed key custody, no long-running operational recovery, and no production adversary model beyond post-hoc ledger tampering without the signing key.

## Claim scope

In a local single-process synthetic agent-action runtime, a SHA-256 hash chain plus Ed25519 signatures can append signed provenance entries for 100 to 20000 actions at about 20.7 us/action and verify them at about 48.7 us/action while detecting payload, chain, signature, deletion, reordering, and adaptive rehash tampering.

## Why it stopped

No-paper closure: this run produced a useful Tier 1 mechanism signal, but it remains synthetic/local and is not publication-grade direct evidence for real agent runtimes.

## Recommended next action

Run a bounded real-agent integration test that instruments actual Codex or LangGraph tool actions, writes the same signed ledger during live tasks, and measures missed-action rate, append latency, verification latency, and tamper detection under concurrent or interrupted execution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live agent runtime signed provenance ledger integration
- Success threshold: Across at least 1000 real runtime actions, capture 100% of emitted tool/action events, keep signed append p95 below 1 ms/action and end-to-end task overhead below 5%, verify persisted ledgers after restart, and detect all tamper cases including adaptive rehash.
- Stop condition: Stop as negative if any real runtime run misses captured actions, persisted signed ledgers fail clean verification after restart, adaptive rehash tampering is not detected, or signed append p95 exceeds 1 ms/action under ordinary local runtime load.

## Evidence references

- Artifact root: `<local-path>/projects/real-runtime-signed-provenance-ledger-evaluation-for-agent-f56187a255`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
