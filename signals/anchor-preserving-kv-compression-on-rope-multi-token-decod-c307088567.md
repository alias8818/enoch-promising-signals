# Anchor-preserving KV compression on RoPE multi-token decoding with matched baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-kv-compression-on-rope-multi-token-decod-c307088567`
Run ID: `anchor-preserving-kv-compression-on-rope-multi-token-decod-c307088567-20260621T191036171716+0000`

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

- Parent run decision: Anchor-preserving KV compression with exact state reuse: enoch://control-plane/projects/anchor-preserving-kv-compression-with-exact-state-reuse-387bf0e4d598/runs/anchor-preserving-kv-compression-with-exact-state-reuse-387bf0e4d598-20260621T185001440024+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9fb28cddb478

## What looked useful

Anchor-preserving compression retained 100% of anchors and achieved 0.985 mean cosine to full attention output, much higher than matched baselines, but its MSE was 0.139 versus the best matched baseline MSE of 0.102, indicating magnitude distortion under compressed-cache softmax renormalization.

## Boundaries and scale limits

No trained or pretrained transformer, no real text perplexity/task metric, synthetic known anchors, short local GPU run, and no dropped-attention-mass or value-residual correction.

## Claim scope

In a controlled synthetic RoPE multi-token attention test with 2048-token history, 8-token decode blocks, and matched 384-token KV retention budgets, preserving known anchors improved output direction versus matched baselines but did not improve absolute output MSE.

## Why it stopped

Tier 1 direct test produced mixed evidence: the anchor mechanism is supported directionally, but the uncorrected drop-in KV compression claim is directly falsified on absolute output MSE versus a matched uniform baseline.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up that adds dropped-mass or residual-value correction and requires lower absolute output MSE than matched baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dropped-mass-corrected anchor-preserving KV compression for RoPE decoding
- Success threshold: Corrected anchor-preserving must reduce mean absolute output MSE by at least 20% versus the best matched baseline while maintaining cosine similarity at or above 0.98 in the controlled test.
- Stop condition: Stop if corrected anchor-preserving fails to beat the best matched baseline on MSE across 12 seeds or if the correction only improves cosine while preserving the same magnitude distortion.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-kv-compression-on-rope-multi-token-decod-c307088567`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
