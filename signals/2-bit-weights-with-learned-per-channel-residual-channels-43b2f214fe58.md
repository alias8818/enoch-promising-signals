# 2-bit weights with learned per-channel residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weights-with-learned-per-channel-residual-channels-43b2f214fe58`
Run ID: `2-bit-weights-with-learned-per-channel-residual-channels-43b2f214fe58-20260630T093852051318+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c56e9ba79ba4

## What looked useful

Across three seeds, QAT best validation accuracy averaged 0.6004 for pure 2-bit, 0.5988 for rank-2 residual, and 0.5964 for rank-4 residual. Posthoc SVD residual correction improved from 0.5579 at q2 rank 0 to 0.5814 at rank 8 and 0.5874 at rank 16, but those settings used about 5.75 and 9.42 mean stored bits/weight.

## Boundaries and scale limits

Synthetic teacher-student classification and dense-layer residual approximation only; no GPT-2-small-class language modeling, pretrained transformer quantization, latency, perplexity, or optimized kernel evidence.

## Claim scope

Small CUDA teacher-student MLP probes show that low-rank residual corrections can carry useful post-training quantization error information, but learned rank-2/rank-4 residual channels did not improve over pure 2-bit QAT at this scale.

## Why it stopped

Bounded proxy evidence did not support the practical 2-bit-plus-small-residual claim; residual capacity helped only at substantially higher effective bit budgets, so this is an early no-paper falsification rather than full LM validation.

## Recommended next action

Stop this run as no-paper useful signal; if pursued, run a bounded tiny language-model follow-up with storage-matched 2-bit residual, pure 2-bit, 3-bit, and 4-bit baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-matched tiny language-model test of 2-bit residual channels
- Success threshold: Residual 2-bit must improve validation perplexity by at least 5% over pure 2-bit and match or beat the closest same-storage 3-bit/4-bit baseline within the bounded tiny-LM setting.
- Stop condition: Stop if residual 2-bit fails to beat pure 2-bit by 5% perplexity improvement or requires more storage than the comparison 3-bit/4-bit baseline for similar quality.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weights-with-learned-per-channel-residual-channels-43b2f214fe58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
