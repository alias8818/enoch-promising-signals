# Alias-Robust Suffix Ledger for Low-Memory Agent Consistency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `alias-robust-suffix-ledger-for-low-memory-agent-consistenc-a5bf24e296`
Run ID: `alias-robust-suffix-ledger-for-low-memory-agent-consistenc-a5bf24e296-20260519T204150438842+0000`

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

- Parent run decision: N-Gram KV Suffix Ledger for Low-Memory Agent Consistency: enoch://control-plane/projects/n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f/runs/n-gram-kv-suffix-ledger-for-low-memory-agent-consistency-822c01664f0f-20260519T202818718270+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a632fe50dec5

## What looked useful

Mechanism support is positive for clean aliases: 1.000 alias-robust accuracy versus 0.231 surface-ledger and 0.015 window-only accuracy in the main run. The same simple union mechanism is not robust enough for noisy aliases, scoring 0.794 under 8% false-alias injection.

## Boundaries and scale limits

This was a Tier 1 synthetic direct test, not an LLM or production-agent trace. It did not validate natural-language extraction, token serialization overhead, learned alias admission, long production horizons, or robustness to real ambiguous aliases. The tested union-based ledger exceeded the predeclared 168-item mean-memory target and fell below 0.90 accuracy under 8% false-alias injection.

## Claim scope

In a controlled synthetic low-memory entity-fact stream with clean alias assertions, a canonical alias suffix ledger preserved alias-query consistency far better than recent-window and surface-keyed suffix baselines, reaching 100% accuracy over 3,520 queries when the fact ledger held all active entity-slot facts.

## Why it stopped

No-paper closure: the Tier 1 direct test produced useful mechanism evidence but also showed memory and noisy-alias failure modes, so it is not paper-positive.

## Recommended next action

Run a bounded deepen test adding alias admission/disambiguation and compact alias retention, with success defined as at least 0.90 accuracy under 5% false-alias injection while keeping serialized ledger size below half the raw transcript token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Collision-Aware Compact Alias Ledger for Noisy Low-Memory Agent Consistency
- Success threshold: Alias-admission ledger achieves >= 0.90 old-alias query accuracy and >= 25 percentage-point margin over the best baseline under at least 5% false-alias injection, with serialized ledger size below 50% of the raw transcript budget.
- Stop condition: Stop if accuracy remains below 0.85 at the 50% raw-transcript memory budget or if disambiguation requires storing nearly all alias evidence.

## Evidence references

- Artifact root: `<local-path>/projects/alias-robust-suffix-ledger-for-low-memory-agent-consistenc-a5bf24e296`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
