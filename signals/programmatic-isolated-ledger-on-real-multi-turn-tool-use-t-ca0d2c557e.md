# Programmatic isolated ledger on real multi-turn tool-use traces

Status: `useful_signal`
Project ID: `programmatic-isolated-ledger-on-real-multi-turn-tool-use-t-ca0d2c557e`
Run ID: `programmatic-isolated-ledger-on-real-multi-turn-tool-use-t-ca0d2c557e-20260518T211204812424+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3a12a50e16d3

## What looked useful

The isolated ledger reached 0.998857 complete-row rate with one localized incomplete row, admitted 0 fake rows under 90 injected fake event pairs, while FIFO pairing had 194 mismatches and transcript regex detected all 90 fake IDs.

## Boundaries and scale limits

Local trace corpus only; 30 traces, 2,516 structured events, 875 command rows. Tested command_execution events in persisted JSONL, not live streaming tails, all tool types, signed ledgers, external anchors, concurrent writers, or a public benchmark.

## Claim scope

A structured per-tool-call isolated ledger keyed by item.id reconstructs command_execution rows in 30 local real Codex/Enoch JSONL multi-turn traces, flags incomplete rows, and resists output-embedded fake event text better than transcript-style or FIFO global parsing.

## Why it stopped

Tier 1 controlled direct test supports the mechanism on local real traces, but evidence is not broad or production-grade enough for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up that validates the same isolated ledger as an online tailer during active multi-turn agent sessions across all item types.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online isolated ledger tailing during live multi-turn tool-use traces
- Success threshold: Online isolated ledger has >=0.995 complete-row rate for closed events, <=0.005 unexplained anomaly rate, 0 admitted fake rows under injection, and exact agreement with offline structured replay for closed events; at least one baseline must show measurable pairing or contamination failures.
- Stop condition: Stop if the online ledger admits any injected fake event row, cannot match offline replay for closed events, or cannot collect at least 10 live multi-turn sessions with tool use.

## Evidence references

- Artifact root: `<local-path>/projects/programmatic-isolated-ledger-on-real-multi-turn-tool-use-t-ca0d2c557e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
