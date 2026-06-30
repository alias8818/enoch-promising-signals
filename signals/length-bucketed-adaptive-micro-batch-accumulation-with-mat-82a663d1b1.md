# Length-bucketed adaptive micro-batch accumulation with matched update count

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `length-bucketed-adaptive-micro-batch-accumulation-with-mat-82a663d1b1`
Run ID: `length-bucketed-adaptive-micro-batch-accumulation-with-mat-82a663d1b1-20260524T023343910663+0000`

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

- Parent run decision: Adaptive Micro-batch Gradient Accumulation on Real Small-LM Fine-tuning: enoch://control-plane/projects/adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228/runs/adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228-20260524T021323841800+0000
- Parent run decision: Micro-batch VRAM-Adaptive Gradient Accumulation for Home Training: enoch://control-plane/projects/micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9/runs/micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9-20260524T005309940394+0000

## What looked useful

Final corrected run over 3 seeds: bucket_adaptive vs random_adaptive reduced padding overhead from 0.7287 to 0.0735 and improved real-token throughput 1.081x, while validation loss worsened slightly from 2.4424 to 2.4460. The fixed bucket ablation was faster but processed more tokens/update, so it supports the padding mechanism but not the adaptive matched-update claim. Token-weighted accumulation was necessary; equal micro-batch averaging produced misleading diagnostics.

## Boundaries and scale limits

Small corpus, byte-level tokenizer, compact Transformer, single GB10 GPU, 3 seeds, 300 updates; not GPT-2-small-class, not multi-GPU, not mixed-precision production training, and not a full language-modeling benchmark.

## Claim scope

On a compact single-GPU causal Transformer trained for 300 matched optimizer updates on variable-length Tiny Shakespeare byte-token examples, length bucketing sharply reduces padding and gives a modest real-token throughput gain, but the tested adaptive accumulation policy is neutral to slightly worse on validation loss after token-weighted accumulation.

## Why it stopped

Medium local validation produced mixed evidence: clear padding and modest throughput support, but no validation-loss improvement for the tested adaptive accumulation policy after correcting token-weighted gradients.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should redesign the adaptive policy to jointly match real tokens/update and cap micro-batch count, then rerun the same 3-seed protocol before considering larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-budget-matched bucketed accumulation with micro-batch-count cap
- Success threshold: Across 3 seeds and at least 300 updates, bucketed adaptive must improve real-token throughput by >=10% versus random_adaptive while keeping validation loss within 0.01 NLL and real tokens/update within 5% of the baseline.
- Stop condition: Stop if matched-token bucketed adaptive remains <10% faster, exceeds +0.01 validation NLL, or needs substantially more micro-batches/update than the baseline to achieve the throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/length-bucketed-adaptive-micro-batch-accumulation-with-mat-82a663d1b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
