# Anchor-Token Memory: Compressed Agent State with Exact Recall

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-token-memory-compressed-agent-state-with-exact-recall-4d6fc2cc6f8d`
Run ID: `anchor-token-memory-compressed-agent-state-with-exact-recall-4d6fc2cc6f8d-20260628T060952144468+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c40863a826e

## What looked useful

Anchor-token memory achieved 4096/4096 exact recall with working state equal to 27.8% of transcript bytes and total anchor index plus payload store equal to 88.9% of transcript bytes. Lossy summary got 0/4096 exact recall, sliding transcript got 32/4096, and flat exact retrieval got 4096/4096 at full transcript size.

## Boundaries and scale limits

Tested 4096 synthetic facts and 4096 exact queries on one CPU process. No LLM-in-the-loop anchor generation, paraphrased retrieval, noisy metadata, stale-anchor handling, deletion semantics, adversarial corruption, or long-running persistence was tested.

## Claim scope

In a deterministic synthetic replay with oracle entity/field resolution, anchor-token memory can preserve exact recall while compressing the agent working state by storing entity/field-to-anchor references and retrieving verbatim values from a separate anchor-keyed payload store.

## Why it stopped

Bounded synthetic evidence supports the anchor-backed mechanism but is not direct/full evidence for real agent memory; exact recall depends on a separate payload store and oracle-style key resolution.

## Recommended next action

Stop this run as no-paper useful signal; next run should test LLM-in-the-loop anchor creation, state compression, and paraphrased query-to-anchor resolution on natural replay tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop anchor-token memory under paraphrased repeated-agent replay
- Success threshold: At least 95% exact recall on 500 or more paraphrased queries, working-state bytes below 40% of full transcript bytes, and explicit accounting of total bytes including payload store.
- Stop condition: Stop if anchor creation/resolution falls below 80% exact recall or if total storage exceeds flat transcript retrieval without a compensating working-context reduction.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-token-memory-compressed-agent-state-with-exact-recall-4d6fc2cc6f8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
