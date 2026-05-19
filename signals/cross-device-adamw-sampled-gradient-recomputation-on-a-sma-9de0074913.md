# Cross-device AdamW sampled-gradient recomputation on a small transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-device-adamw-sampled-gradient-recomputation-on-a-sma-9de0074913`
Run ID: `cross-device-adamw-sampled-gradient-recomputation-on-a-sma-9de0074913-20260517T162803399342+0000`

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

- Internal Enoch project: Cross-device AdamW sampled-gradient recomputation on a small transformer: internal_generated:cross-device-adamw-sampled-gradient-recomputation-on-a-sma-9de0074913

## What looked useful

The cross-device AdamW control is numerically sound, and sampled updates reduce gradient transfer roughly in proportion to the sampled fraction, but naive random tensor sampling fails the quality-preservation requirement: 50% sampling averaged 0.586 final validation loss versus 0.147 for GPU/full CPU AdamW, and 25% sampling averaged 1.777.

## Boundaries and scale limits

Synthetic corpus, small model, single-host CPU/GPU offload, 100-step training budget constrained by local runtime guard; no real text, GPT-2-small-class scale, long schedule, wall-clock-matched quality target, or true multi-node cross-device optimizer placement was tested.

## Claim scope

On a 4.9M-parameter 6-layer small transformer trained for 100 steps on a deterministic held-out synthetic language task on one GB10 CPU/GPU host, full CPU-offloaded AdamW matches GPU AdamW, but naive random parameter-tensor sampled-gradient recomputation at 50% and 25% update fractions substantially worsens validation loss despite reducing gradient transfer and peak CUDA allocation.

## Why it stopped

Tier 2 fixed-seed small-transformer validation showed real transfer and memory savings but large convergence degradation versus a real GPU AdamW baseline and a full CPU-offloaded AdamW control.

## Recommended next action

Stop this naive random tensor-sampling line as no-paper evidence; only pursue a bounded deepen test if the algorithm changes to enforce deterministic or importance-weighted coverage with an explicit loss-preservation threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coverage-constrained sampled AdamW recomputation on the same small transformer
- Success threshold: Final validation loss no more than 10% above GPU AdamW/full CPU AdamW mean while reducing gradient-transfer bytes by at least 40% and not reducing throughput below the full CPU-offloaded AdamW control.
- Stop condition: Stop if the coverage-constrained sampler still exceeds a 10% validation-loss penalty or if transfer savings fall below 40%.

## Evidence references

- Artifact root: `<local-path>/projects/cross-device-adamw-sampled-gradient-recomputation-on-a-sma-9de0074913`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
