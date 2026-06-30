# Budget-aware learned anchor selection from compressed decoder loss

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `budget-aware-learned-anchor-selection-from-compressed-deco-f799fa9f86`
Run ID: `budget-aware-learned-anchor-selection-from-compressed-deco-f799fa9f86-20260524T065721227224+0000`

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

- Parent run decision: Anchor-Gated KV Compression: Exact Anchors with Interleaved Compressed State: enoch://control-plane/projects/anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c/runs/anchor-gated-kv-compression-exact-anchors-with-interleaved-compressed-state-35d0265a341c-20260524T062932842792+0000
- Parent run decision: Learned anchor selection for exact-anchor interleaved KV compression in a small decoder: enoch://control-plane/projects/learned-anchor-selection-for-exact-anchor-interleaved-kv-c-67455381c0/runs/learned-anchor-selection-for-exact-anchor-interleaved-kv-c-67455381c0-20260524T065052895262+0000

## What looked useful

The direct compressed-loss target exposed a large gap: the best budget-aware learned classifier trailed recency by +0.391, +0.406, and +0.224 NLL at budgets 8, 16, and 32, while oracle single-anchor selection was far better than all practical policies. This suggests the simple compressed-loss labels are real but not learnable enough from token/position/surprisal/attention features in this setup.

## Boundaries and scale limits

Single small character-level decoder, one base-model seed, three selector/evaluation seeds, 384 validation contexts per seed, local GB10 runtime under 2 minutes per medium run; not evidence about GPT-2-class or production LLM KV-cache compression.

## Claim scope

On a small CUDA-trained character decoder over Tiny Shakespeare with 128-token contexts and budgets of 8/16/32 anchors, compressed-decoder-loss-trained learned selectors did not beat simple recency or attention baselines on validation next-token NLL; an oracle single-anchor utility control showed exploitable anchor structure exists.

## Why it stopped

Tier 2 local validation produced a reproducible negative result for the tested learned selectors against real recency/attention baselines, despite an oracle utility gap showing the task itself was not vacuous.

## Recommended next action

Stop this branch as no-paper useful-signal evidence; a bounded deepen follow-up should test richer selector inputs from hidden states and direct budget-level loss training before any larger-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden-state budget-level selector for compressed decoder anchors
- Success threshold: For at least two of three budgets, learned hidden-state selection must beat recency by >=0.05 mean NLL and beat attention by >=0.03 mean NLL across three seeds, with no budget worse than recency by >0.02.
- Stop condition: Stop if hidden-state learned selection still trails recency at two or more budgets or selector utility/ranking diagnostics remain below 0.25 correlation/AUC-equivalent signal.

## Evidence references

- Artifact root: `<local-path>/projects/budget-aware-learned-anchor-selection-from-compressed-deco-f799fa9f86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
