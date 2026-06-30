# Latent Memory Tokens: 2-bit Compressed with FP8 Residual Anchors

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `latent-memory-tokens-2-bit-compressed-with-fp8-residual-anchors-12db9f406d56`
Run ID: `latent-memory-tokens-2-bit-compressed-with-fp8-residual-anchors-12db9f406d56-20260629T160950396349+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10d46b4777d6

## What looked useful

Sparse FP8 residual anchors monotonically improve plain 2-bit memory-token reconstruction, but the improvement is too small to beat a simple int4 baseline. At 64 anchors/token, storage is 4.156 bits/value versus int4 at 4.031 bits/value, while attention-output error is 20x, 30.5x, and 363x worse than int4 on gaussian, low-rank clustered, and heavy-tail synthetic memories respectively.

## Boundaries and scale limits

No full transformer training, no learned latent-memory tokens, no perplexity evaluation, no packed-kernel bandwidth measurement, and no datacenter-scale model validation. Results cover vector reconstruction and retrieval/attention-output preservation only.

## Claim scope

GPU-vectorized synthetic latent-memory proxy with 4096 normalized memory vectors, width 512, 512 noisy retrieval queries, and honest storage accounting for 2-bit payloads, fp16 scales, FP8 residual anchors, and anchor indices.

## Why it stopped

Early proxy falsification: the tested compression/retrieval mechanism improves over plain 2-bit but is not competitive with int4 at comparable storage. This is not a full transformer validation or universal impossibility result.

## Recommended next action

Stop this variant as no-paper evidence; do not scale 2-bit plus sparse FP8 residual anchors unless a new equal-budget encoding removes index overhead or demonstrates task-loss gains over int4 in a learned-token model.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/latent-memory-tokens-2-bit-compressed-with-fp8-residual-anchors-12db9f406d56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
