# Human-authored repeated-agent memory replay with embedding retrieval control

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `human-authored-repeated-agent-memory-replay-with-embedding-ae98e04c89`
Run ID: `human-authored-repeated-agent-memory-replay-with-embedding-ae98e04c89-20260620T014209185772+0000`

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

- Parent run decision: Layered Agent Memory: Notes+Operator-Model vs Retrieval-Only: enoch://control-plane/projects/layered-agent-memory-notes-operator-model-vs-retrieval-only-24a3c6d4a5cc/runs/layered-agent-memory-notes-operator-model-vs-retrieval-only-24a3c6d4a5cc-20260620T012100389486+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/17cd328b4fe6

## What looked useful

Layered entity/type filtering reduced distractor retrieval versus flat keyword and embedding controls, but the embedding control was already strong enough that the improvement margin was only 0.040 F1. This supports the mechanism direction but is not paper-positive.

## Boundaries and scale limits

Small hand-authored corpus; deterministic retrieval/scoring only; no live LLM generation; memories are pre-distilled; embedding control is a lightweight stdlib semantic-hashing approximation rather than a production embedding model.

## Claim scope

In a deterministic Tier 1 replay suite with 6 human-authored repeated-agent tasks and 12 later-session queries, typed layered memory achieved perfect fact F1 and zero configured false recall, but did not beat the embedding retrieval control by the predeclared 0.05 F1 margin.

## Why it stopped

Controlled Tier 1 direct test produced useful mechanism support but missed the predeclared layered-vs-embedding improvement threshold, so this is no-paper evidence rather than a positive closure.

## Recommended next action

Run a bounded deepen follow-up with 30-50 human-authored replay cases, a production embedding backend, and a fixed threshold requiring at least 0.05 F1 gain plus lower false recall before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium human-authored replay suite with production embedding control
- Success threshold: Layered memory mean answer F1 >= 0.85, layered minus production embedding control F1 >= 0.05, and layered false recall rate at least 50% lower than embedding control with no more than 0.10 absolute false recall.
- Stop condition: Stop as no-paper if the layered strategy fails the 0.05 F1 gain or false-recall reduction on the medium suite, or if failures concentrate in common replay patterns that cannot be fixed without changing the memory contract.

## Evidence references

- Artifact root: `<local-path>/projects/human-authored-repeated-agent-memory-replay-with-embedding-ae98e04c89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
