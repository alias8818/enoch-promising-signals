# Sparse-Head Self-Speculation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `sparse-head-self-speculation-cc31c6390671`
Run ID: `sparse-head-self-speculation-cc31c6390671-20260521T214223527392+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ea20a1ed6703

## What looked useful

At 50% head density, top projection-norm head masks reached 0.406 greedy acceptance and random masks averaged 0.539 across five seeds. The only single run above 0.80 acceptance retained 83.3% of heads, leaving too little theoretical attention-head savings for a compelling sparse draft path.

## Boundaries and scale limits

One pretrained small GPT-2-class model, synthetic prompt snippets, greedy next-token acceptance, no fused sparse-head kernel, no learned/dynamic head policy, and no end-to-end speculative decoding throughput benchmark.

## Claim scope

Early behavioral falsification on distilgpt2: static sparse attention-head masks did not provide high-acceptance self-speculative draft tokens at meaningful head reductions.

## Why it stopped

Proxy/early falsification: direct masked-head behavior on distilgpt2 failed the practical acceptance threshold at meaningful sparsity; full validation would require larger models, learned/dynamic selection, and fused sparse serving benchmarks.

## Recommended next action

Stop this naive static sparse-head self-speculation line unless a future run tests a learned or dynamic head policy with >=0.80 acceptance at <=50% head density and an actual sparse-kernel speedup.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/sparse-head-self-speculation-cc31c6390671`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
