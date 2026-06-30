# Two-Tier Memory: Verbatim Anchors Plus Compressed Semantic State

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `two-tier-memory-verbatim-anchors-plus-compressed-semantic-state-602e630faf83`
Run ID: `two-tier-memory-verbatim-anchors-plus-compressed-semantic-state-602e630faf83-20260610T105415712598+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b3efcd0e635c

## What looked useful

The run supports the mechanism that semantic compression plus separately stored verbatim anchors can preserve exact high-entropy details more efficiently than raw full-record caching under equal byte budgets. It remains no-paper evidence because the workload and memory policies are synthetic.

## Boundaries and scale limits

This was a CPU-only synthetic mechanism test, not a trained language model, real agent memory system, naturalistic corpus, or production retrieval stack. It does not validate learned compression, embedding retrieval, adversarial paraphrase, latency in a serving system, or long-running model behavior.

## Claim scope

In a synthetic fixed-byte memory benchmark with 2,000 records, 10 seeds, and high-entropy exact anchors, a two-tier memory policy using compressed semantic facts plus verbatim anchor records recovered exact anchors about 2x better than a raw-cache-only baseline at 15%, 25%, 35%, and 50% raw-corpus budgets, while compressed-only memory could not reproduce exact anchors.

## Why it stopped

Stopped after a completed medium synthetic confirmation: useful mechanism signal, but no direct model-level or naturalistic evidence sufficient for paper readiness.

## Recommended next action

Run a bounded real-workload follow-up that integrates two-tier memory into a retrieval or agent-memory stack and compares against learned summaries, vector chunk retrieval, full-text search, and raw cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-tier memory on naturalistic retrieval and agent-memory workloads
- Success threshold: At equal byte budget, two-tier memory improves exact-match accuracy by at least 20% relative over the best non-two-tier baseline while keeping semantic QA accuracy within 5% relative of the best compressed or retrieval baseline.
- Stop condition: Stop if two-tier memory fails to beat the best baseline exact-match accuracy by 10% relative on two naturalistic datasets or loses more than 10% relative semantic QA accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/two-tier-memory-verbatim-anchors-plus-compressed-semantic-state-602e630faf83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
