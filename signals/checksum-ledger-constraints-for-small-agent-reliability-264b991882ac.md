# Checksum ledger constraints for small-agent reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `checksum-ledger-constraints-for-small-agent-reliability-264b991882ac`
Run ID: `checksum-ledger-constraints-for-small-agent-reliability-264b991882ac-20260529T074121106260+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ab3b49546753

## What looked useful

Checksum+balance retry3 improved correct final balance from 0.39625 to 0.99960 in the main run and from 0.22250 to 0.99850 in the coherent/copy-error stress run. However, balance_retry3 alone reached 0.99995 and 0.99880, while checksum_only_retry3 reached only 0.47090 and 0.67420, indicating the semantic invariant drove most reliability gains.

## Boundaries and scale limits

No real LLM agents, natural-language prompts, tool-call latency, context-window pressure, or persisted-state tampering were tested. Evidence is from CPU-only synthetic episodes: 20,000 main episodes per condition and 10,000 stress episodes per condition.

## Claim scope

In a deterministic synthetic stochastic-updater ledger task, semantic ledger invariants plus bounded retries substantially improve exact final-state reliability with about 2-3% attempt overhead; checksum/hash constraints alone are insufficient for exact balance reliability.

## Why it stopped

No-paper closure: this is a useful synthetic proxy signal, not direct evidence that checksum ledgers improve real small-agent reliability.

## Recommended next action

Run a bounded direct small-LLM/tool-agent benchmark that compares no ledger, semantic invariant only, checksum ledger only, and combined constraints on resumable stateful tasks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-agent checksum ledger benchmark
- Success threshold: Combined checksum plus semantic invariant improves exact task success by at least 5 absolute percentage points over semantic invariant only, or cuts undetected resumed-history corruption by at least 50%, with less than 25% token/tool overhead.
- Stop condition: Stop if semantic invariant only matches or exceeds combined checksum constraints within confidence intervals and no resumed-history corruption benefit appears.

## Evidence references

- Artifact root: `<local-path>/projects/checksum-ledger-constraints-for-small-agent-reliability-264b991882ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
