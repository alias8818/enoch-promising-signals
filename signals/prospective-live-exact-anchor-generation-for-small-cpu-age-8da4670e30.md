# Prospective live exact-anchor generation for small CPU agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prospective-live-exact-anchor-generation-for-small-cpu-age-8da4670e30`
Run ID: `prospective-live-exact-anchor-generation-for-small-cpu-age-8da4670e30-20260528T213813425586+0000`

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

- Parent run decision: Real-trace exact-anchor replay for small CPU agents: enoch://control-plane/projects/real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41/runs/real-trace-exact-anchor-replay-for-small-cpu-agents-b8f4ab4b41-20260528T161321080441+0000
- Parent run decision: Exact-anchor evidence ledger for small CPU agents: enoch://control-plane/projects/exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87/runs/exact-anchor-evidence-ledger-for-small-cpu-agents-034f4e681c87-20260528T020551071549+0000

## What looked useful

On 900 fixed-seed tasks over 627 Python stdlib files, prospective live AST anchors achieved 100.0% exact accuracy with 0.00051 ms median lookup latency after live edits. Stale anchors achieved 0.0%, symbol-only AST 73.3%, fresh module regex 83.0%, and global regex 53.3%.

## Boundaries and scale limits

Python-only; synthetic comment-line insertions; no natural-language LLM agent in the loop; no non-Python repositories; no ambiguous or partially specified queries; no publication-scale user/task diversity.

## Claim scope

For uniquely addressable Python stdlib code-navigation queries that specify module, kind, and qualified symbol name, a prospective live AST anchor index returns exact file:line anchors after synthetic live line-shifting edits and outperforms stale-anchor and regex baselines.

## Why it stopped

No-paper closure: medium local evidence supports the exact-anchor mechanism, but the claim remains a structured Python helper benchmark rather than an end-to-end agent or broad systems result.

## Recommended next action

Run a bounded end-to-end small-agent benchmark where a CPU LLM answers code-review/navigation tasks using either live anchors or regex retrieval, with exact final-answer anchor accuracy as the primary metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end small-agent exact-anchor accuracy with live AST anchors
- Success threshold: At least 95% exact final-answer anchor accuracy and at least +15 percentage points over the strongest regex baseline across 300 or more tasks, with no regression in answer validity.
- Stop condition: Stop if live-anchor exact accuracy is below 90%, if improvement over the strongest regex baseline is under 10 percentage points, or if integration latency exceeds the budget for small CPU agents.

## Evidence references

- Artifact root: `<local-path>/projects/prospective-live-exact-anchor-generation-for-small-cpu-age-8da4670e30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
