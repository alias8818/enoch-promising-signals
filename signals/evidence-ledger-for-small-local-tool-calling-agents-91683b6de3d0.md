# Evidence ledger for small local tool-calling agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-local-tool-calling-agents-91683b6de3d0`
Run ID: `evidence-ledger-for-small-local-tool-calling-agents-91683b6de3d0-20260603T210723697709+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae55cc497071

## What looked useful

The local benchmark supports the practical mechanism: ledger verification detected 100% of modify_args, modify_output, delete_entry, reorder_entries, duplicate_entry, and rewrite_chain mutations across 50 trials each, while plain JSONL validation averaged 33.3% detection and missed valid-JSON edits, reorders, and chain rewrites.

## Boundaries and scale limits

Synthetic deterministic tools only; no live LLM planner, no human audit study, no nondeterministic networked tools, no independent timestamp service, and no test where the compromised runtime controls both ledger emission and anchor storage.

## Claim scope

In deterministic synthetic local tool-calling traces, a per-step hash-chained evidence ledger with a separately stored final anchor detects tested post-hoc trace tampering that a plain JSONL log verifier misses, with about 0.007 ms extra CPU time per tool-call step and about 2.5x storage overhead on a 10000-step benchmark.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct publication-grade validation of real tool-calling agents or auditor usefulness.

## Recommended next action

Stop this run as no-paper useful evidence; next, run the same ledger inside a real small local LLM tool-calling loop with nondeterministic tools and an independent anchor channel.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-agent evidence ledger with nondeterministic tools
- Success threshold: Ledger detection is at least 95% across mutation classes, plain logs miss at least two valid-JSON tamper classes, replay/audit coverage is at least 95%, and median ledger overhead is below 25 ms per tool step.
- Stop condition: Stop as negative if ledger detection drops below 90% on any critical mutation class, if independent anchoring cannot be implemented locally, or if median per-step overhead exceeds 100 ms for small local agents.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-tool-calling-agents-91683b6de3d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
