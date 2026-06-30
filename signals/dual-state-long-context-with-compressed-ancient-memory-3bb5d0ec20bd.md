# Dual-State Long Context with Compressed Ancient Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dual-state-long-context-with-compressed-ancient-memory-3bb5d0ec20bd`
Run ID: `dual-state-long-context-with-compressed-ancient-memory-3bb5d0ec20bd-20260527T204052114640+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3b8ae3aeba13

## What looked useful

Recent-only retrieval after cutover was chance-level at 0.01556 accuracy, a one-vector mean summary reached only 0.04826, and slot-addressed memory improved from 0.12382 at 8 slots to 1.0 at 512 collision-free slots. Compression collisions were the dominant failure mode.

## Boundaries and scale limits

No learned transformer was trained; no natural-language corpus, perplexity, attention implementation, runtime scaling, or GPT-2-small-class parameter-matched baseline was evaluated. The result is a toy mechanism probe over 100000 synthetic trials.

## Claim scope

Deterministic synthetic key-value retrieval after a hard context cutover: a compressed ancient state preserves facts only when it remains query-addressable and has enough effective slots to avoid destructive collisions.

## Why it stopped

No-paper closure: this is a deterministic synthetic mechanism probe, not a full learned long-context validation.

## Recommended next action

Run a bounded learned follow-up with a small parameter-matched transformer baseline, recent-only hard-cutover baseline, mean-summary control, and learned dual-state memory on the same retrieval task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Dual-State Memory Versus Parameter-Matched Transformer on Synthetic Ancient-Fact Retrieval
- Success threshold: Dual-state held-out accuracy at least 20 percentage points above recent-only and mean-summary controls at matched parameter count, with explicit memory/runtime overhead below full-context attention for long cutover distances.
- Stop condition: Stop as negative if the learned dual-state model fails to beat the best control by 10 percentage points after matched training budget or if gains require collision-free memory as large as the full ancient fact set.

## Evidence references

- Artifact root: `<local-path>/projects/dual-state-long-context-with-compressed-ancient-memory-3bb5d0ec20bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
