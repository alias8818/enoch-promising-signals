# Channel-Wise 1-Bit Gradients with Local Error Residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be`
Run ID: `channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be-20260522T003143304102+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71b83696c4f4

## What looked useful

Local error residuals are the important mechanism: channel-wise 1-bit residual reached 0.9997 mean accuracy at 600 steps versus 0.9043 without residuals. However, global 1-bit residual reached 1.0000 mean accuracy with a lower estimated bit ratio, and in the LR sweep global residual also slightly beat channel-wise residual accuracy while using fewer bits.

## Boundaries and scale limits

Synthetic 3x16x16 image data, one tiny CNN family, 3-5 seeds depending on run, SGD-like optimizer only, estimated gradient payload bits only, no real dataset, no transformer, no distributed transport, and no communication wall-clock benchmark.

## Claim scope

On a small balanced synthetic CNN image-classification task, channel-wise 1-bit SGD updates with local residuals can match dense SGD accuracy and greatly outperform channel-wise 1-bit updates without residuals, but they do not beat a simpler global 1-bit residual baseline.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports residual error feedback but does not demonstrate a channel-wise advantage over the simpler global 1-bit residual control.

## Recommended next action

Run a bounded real-data follow-up on CIFAR-10 or a small transformer task comparing dense SGD, global 1-bit residual, and channel-wise 1-bit residual with tuned learning rates and measured communication payloads; do not write a paper from the current synthetic-only evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data comparison of channel-wise versus global 1-bit residual gradients
- Success threshold: Channel-wise 1-bit residual must improve validation metric by at least 1 percentage point accuracy or 3 percent relative loss/perplexity versus global 1-bit residual at equal or lower gradient payload across at least 3 seeds.
- Stop condition: Stop if a tuned global 1-bit residual baseline matches or beats channel-wise residual at lower payload on the real task, or if channel-wise residual fails to stay within 2 percentage points accuracy or 5 percent relative loss/perplexity of dense training.

## Evidence references

- Artifact root: `<local-path>/projects/channel-wise-1-bit-gradients-with-local-error-residuals-6f741f8159be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
