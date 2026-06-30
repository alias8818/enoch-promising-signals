# 1.58-bit ternary weights with low-rank dense residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-ternary-weights-with-low-rank-dense-residual-a5961c1c135e`
Run ID: `1-58-bit-ternary-weights-with-low-rank-dense-residual-a5961c1c135e-20260628T025642087562+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7886b0a92084

## What looked useful

Rank-8 ternary+low-rank reached 0.693 mean accuracy versus 0.706 dense and 0.6657 ternary-only at 3.09x estimated fp16 compression, reducing the ternary-only mean gap from 4.03 to 1.30 percentage points. Low-rank-only rank 16 reached 0.7033 at 2.42x compression, so the ternary component is not yet clearly superior to a dense low-rank baseline.

## Boundaries and scale limits

Synthetic data only; small MLP only; post-training SVD approximation only; no GPT-2-small-class model, no real dataset, no quantization-aware training, no ternary kernel speed or memory measurement.

## Claim scope

In a three-seed synthetic teacher-student MLP post-training approximation test, alpha-scaled ternary weights plus a small SVD dense residual improved task accuracy and reconstruction error relative to ternary-only weights while retaining compression versus fp16 dense weights.

## Why it stopped

Proxy evidence is mixed: the residual helps ternary-only, but the experiment is synthetic/post-training and low-rank-only is competitive, so this is not direct publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a real small benchmark with storage-matched dense, ternary-only, low-rank-only, and ternary+low-rank controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-matched real-benchmark test of ternary plus low-rank residual
- Success threshold: At a matched storage budget, ternary+low-rank should close at least half of the ternary-only accuracy/perplexity gap to dense and outperform low-rank-only by a practically meaningful margin on the primary held-out metric.
- Stop condition: Stop if ternary+low-rank fails to beat either ternary-only or storage-matched low-rank-only on the real benchmark across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-ternary-weights-with-low-rank-dense-residual-a5961c1c135e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
