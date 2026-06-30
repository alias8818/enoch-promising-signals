# Train a Small Transformer Draft to Test Int2 Channel Residual Compensation in Real Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `train-a-small-transformer-draft-to-test-int2-channel-resid-229bfc865a`
Run ID: `train-a-small-transformer-draft-to-test-int2-channel-resid-229bfc865a-20260613T194132062745+0000`

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

- Parent run decision: Speculative Decoding with 2-bit Draft Model and Channel Residual Compensation: enoch://control-plane/projects/speculative-decoding-with-2-bit-draft-model-and-channel-residual-compensation-992034b0722a/runs/speculative-decoding-with-2-bit-draft-model-and-channel-residual-compensation-992034b0722a-20260613T185051081535+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/faf8d73e53c5

## What looked useful

Compensation vs uncompensated int2 improved mean speculative acceptance by +0.00344 absolute across five seeds and slightly improved mean NLL by -0.00263, but one seed had worse acceptance and the acceptance stdev was 0.02112, so the mechanism signal is mixed and not paper-ready.

## Boundaries and scale limits

Synthetic character corpus, frozen random backbones, trained linear heads only, five seeds, 640 proposed speculative tokens per seed, CPU-only, no optimized int2 kernels, no natural language benchmark, no fully trained GPT-style draft.

## Claim scope

In a toy NumPy speculative-decoding setup with frozen tiny Transformer backbones and trained LM heads, int2 FFN-output channel residual compensation produced a small mean acceptance lift over uncompensated int2, but with high seed variance.

## Why it stopped

Tier 1 direct speculative accept/reject evidence was completed, but the model is toy-scale/frozen-backbone and the compensation effect is small and mixed, so this is no-paper useful signal rather than publication-grade support.

## Recommended next action

Run a bounded deepen follow-up with a fully trainable small Transformer draft on a real text dataset and require compensation to improve acceptance by at least 1 percentage point over uncompensated int2 across at least 5 seeds without increasing NLL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fully Train a Tiny Transformer Draft for Int2 Residual Compensation Speculative Decoding
- Success threshold: Compensated int2 improves mean speculative acceptance by >= 0.01 absolute over uncompensated int2, is positive in at least 4/5 seeds, and does not increase mean validation NLL.
- Stop condition: Stop as negative if a fully trained draft shows <= 0.002 mean acceptance improvement or worsens NLL by > 0.01 after matched calibration and evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/train-a-small-transformer-draft-to-test-int2-channel-resid-229bfc865a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
