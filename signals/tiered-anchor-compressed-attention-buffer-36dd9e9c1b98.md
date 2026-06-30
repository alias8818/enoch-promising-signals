# Tiered Anchor-Compressed Attention Buffer

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tiered-anchor-compressed-attention-buffer-36dd9e9c1b98`
Run ID: `tiered-anchor-compressed-attention-buffer-36dd9e9c1b98-20260526T062241086811+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2df4cd4f2a67

## What looked useful

The tested tiered anchor-compressed buffer beat recency-only truncation but was dominated by simpler same-budget controls: it won 0/90 five-seed matched cases; single-level compression won 51/90 and uniform exact anchors won 39/90.

## Boundaries and scale limits

No real language-model training or evaluation, no learned compression, no GPT-2-small-class baseline, no production fused attention kernel, and no corpus perplexity or long-context retrieval benchmark.

## Claim scope

Five-seed synthetic PyTorch proxy benchmark of fixed deterministic tiered anchor-compressed KV buffers against recent-only, uniform exact, and single-level compressed buffers for approximating full attention outputs at sequence lengths 2048, 4096, and 8192 with budgets 512 and 1024.

## Why it stopped

Proxy early falsification: the exact tested deterministic tiered buffer did not outperform simpler equal-budget controls and never won across the five-seed synthetic sweep.

## Recommended next action

Stop this deterministic tiered layout as no-paper evidence; any future work should first test a salience-aware or learned anchor policy on the same bounded benchmark before scaling to language models.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tiered-anchor-compressed-attention-buffer-36dd9e9c1b98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
