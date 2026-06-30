# Anchor-Hashed Compressed Memory for Long-Horizon Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-hashed-compressed-memory-for-long-horizon-agents-db86f6532bb5`
Run ID: `anchor-hashed-compressed-memory-for-long-horizon-agents-db86f6532bb5-20260620T233617886905+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8637e62a1db0

## What looked useful

Anchor-addressed compression is collision fragile under high active-anchor cardinality. At 2048 slots, reservoir exceeded the best anchor variant by 0.0676 to 0.0952 absolute exact old-fact accuracy across medium scenarios. A capacity sanity check reached 0.997 for 4-way anchor hashing at 8192 slots, but recency and reservoir were already 1.0 there.

## Boundaries and scale limits

Evidence is synthetic and retrieval-only. It does not include natural-language memory extraction, LLM reader/writer errors, real agent trajectories, vector DB baselines with learned embeddings, or downstream task success. Medium sweep was 40k events per scenario, 5 seeds, and up to 2048 memory slots.

## Claim scope

On synthetic long-horizon fact-recall streams with fixed compressed slot budgets, simple anchor-hashed memory and a 4-way set-associative anchor variant do not outperform reservoir retention for old sparse fact retrieval; they only beat recency in some settings and work well only when slot budget approaches active anchor cardinality.

## Why it stopped

Proxy early falsification rather than full validation: the simple anchor-hashed compressed memory mechanism failed to beat a cheap reservoir baseline under tight synthetic long-horizon memory budgets.

## Recommended next action

Stop this as a no-paper useful signal; only pursue a bounded follow-up if it adds adaptive retention, such as reservoir-within-anchor-buckets or multi-hash admission control, and compares against reservoir on the same old-fact task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Anchor-Reservoir Memory Under Fixed Slot Budgets
- Success threshold: At 2048 slots, adaptive anchor memory must beat global reservoir by at least 0.03 absolute exact accuracy on sparse_old_clean and not lose by more than 0.01 on many_anchors_clean, while keeping query time within 2x simple anchor_hash.
- Stop condition: Stop if adaptive variants fail to match reservoir on old-fact accuracy at 2048 slots or require scanning enough slots that the mechanism no longer has a meaningful lookup-cost advantage.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-hashed-compressed-memory-for-long-horizon-agents-db86f6532bb5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
