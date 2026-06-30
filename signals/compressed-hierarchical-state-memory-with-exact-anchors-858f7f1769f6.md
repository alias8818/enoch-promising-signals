# Compressed Hierarchical State Memory with Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-hierarchical-state-memory-with-exact-anchors-858f7f1769f6`
Run ID: `compressed-hierarchical-state-memory-with-exact-anchors-858f7f1769f6-20260610T005133298084+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

Exact anchors produced 1.000 mean top-1 accuracy on anchor-target queries with 0.135 mean memory ratio, versus 0.415 for summary-only and 1.000 for full exact memory. For non-anchor detail queries, exact anchors reached only 0.010 mean top-1 accuracy, showing that a single block summary effectively loses detail identity.

## Boundaries and scale limits

Tested only NumPy synthetic retrieval, sequence lengths up to 4096, dimensions up to 96, block sizes 8 to 64, and a hand-coded mean-summary compressor. No transformer training, learned anchor policy, language modeling loss, real long-context benchmark, or serving-system validation was run.

## Claim scope

A synthetic key-retrieval probe shows that one exact anchor plus one compressed block summary can preserve exact retrieval for explicitly anchored states at 3.1% to 25% of full memory items, but does not preserve arbitrary non-anchor detail identity.

## Why it stopped

No-paper useful signal: this synthetic proxy supports exact anchored-state preservation but early-falsifies the broader claim that simple exact-anchor block summaries preserve non-anchor details.

## Recommended next action

Run a bounded deepen experiment with learned or policy-selected multiple anchors inside a small transformer/KV-cache setting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Multi-Anchor Compression for Non-Anchor Detail Recall
- Success threshold: Mean non-anchor detail top-1 accuracy >= 0.80 at memory_ratio <= 0.35, anchor top-1 accuracy >= 0.98, and no more than 20% latency overhead versus a same-item-count compressed baseline.
- Stop condition: Stop if non-anchor detail top-1 remains below 0.50 at memory_ratio 0.35 on the synthetic grid or if transformer/KV integration shows worse loss than summary-only at matched memory.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-hierarchical-state-memory-with-exact-anchors-858f7f1769f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
