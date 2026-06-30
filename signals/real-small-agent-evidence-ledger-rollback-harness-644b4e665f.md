# Real Small-Agent Evidence Ledger Rollback Harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-agent-evidence-ledger-rollback-harness-644b4e665f`
Run ID: `real-small-agent-evidence-ledger-rollback-harness-644b4e665f-20260522T145924343297+0000`

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

- Parent run decision: Small-Agent Evidence Ledger with Rollback: enoch://control-plane/projects/small-agent-evidence-ledger-with-rollback-1ce70bd75f24/runs/small-agent-evidence-ledger-with-rollback-1ce70bd75f24-20260522T142314527859+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/04fb381aed47

## What looked useful

Rollback with recomputation achieved 100% accuracy, zero stale active answers, and zero invalid-dependency violations across 200 trials. Non-recursive controls retained stale active answers in 200/200 trials, including when corrected evidence and a corrected answer were added.

## Boundaries and scale limits

Tested only on 200 synthetic arithmetic trials with deterministic agents in a single-process in-memory ledger. Not tested on LLM agents, real research evidence, concurrent writes, crash persistence, database-backed ledgers, or long task histories.

## Claim scope

In a deterministic small-agent controlled harness, recursive dependency rollback prevents active derived answers from depending on invalidated root evidence, and rollback plus recomputation restores correct final answers after verifier correction.

## Why it stopped

Controlled Tier 1 mechanism threshold was met, but evidence is small and deterministic, so it is useful no-paper support rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up in a real small-agent file-backed harness with concurrent writer/verifier turns and require zero stale active citations after injected verifier invalidations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: File-Backed Concurrent Small-Agent Ledger Rollback Test
- Success threshold: Across at least 100 injected invalidation episodes, rollback treatment has zero active stale citations and zero invalid-dependency violations, while the non-recursive control shows stale active citations in at least 80% of episodes.
- Stop condition: Stop if the file-backed rollback treatment produces any unreconciled active entry depending on invalid evidence after verifier invalidation and one recomputation opportunity, or if persistence/concurrency mechanics cannot be implemented locally.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-agent-evidence-ledger-rollback-harness-644b4e665f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
