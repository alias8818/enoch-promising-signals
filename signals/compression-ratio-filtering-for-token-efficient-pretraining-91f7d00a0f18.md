# Compression-ratio filtering for token-efficient pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `compression-ratio-filtering-for-token-efficient-pretraining-91f7d00a0f18`
Run ID: `compression-ratio-filtering-for-token-efficient-pretraining-91f7d00a0f18-20260524T214218336348+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/29310ea1ba0a

## What looked useful

Across three seeds, random sampling achieved mean validation BPB 3.0904; low40, middle60, high40, and trim-extremes compression-ratio policies were all slightly worse on average and each beat random in only 1/3 seeds. Ratio-only filtering is not supported as a standalone token-efficiency rule in this local proxy.

## Boundaries and scale limits

Single corpus, byte-level tokenizer, small model, short training horizon, three seeds, validation BPB only; not a GPT-2-small or larger tokenizer-based pretraining validation and not downstream task evidence.

## Claim scope

In a bounded WikiText-2 proxy with a tiny byte-level causal Transformer trained from scratch under equal byte-token budgets, simple gzip compression-ratio filters did not improve validation bits-per-byte over random paragraph sampling.

## Why it stopped

Proxy early falsification: bounded direct LM training evidence showed no consistent validation BPB gain from compression-ratio filtering under equal token budgets.

## Recommended next action

Stop this ratio-only filtering line unless future work embeds compression ratio as one feature in a broader quality/dedup classifier; this run is a proxy early falsification rather than full-scale validation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/compression-ratio-filtering-for-token-efficient-pretraining-91f7d00a0f18`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
