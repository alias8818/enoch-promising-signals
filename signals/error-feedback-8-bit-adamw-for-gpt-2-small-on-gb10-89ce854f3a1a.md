# Error-Feedback 8-bit AdamW for GPT-2-small on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `error-feedback-8-bit-adamw-for-gpt-2-small-on-gb10-89ce854f3a1a`
Run ID: `error-feedback-8-bit-adamw-for-gpt-2-small-on-gb10-89ce854f3a1a-20260628T150431958762+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e5f1f334617b

## What looked useful

Error feedback is a plausible stabilizer for quantized AdamW moment state on GPT-2-small-class gradients, but only with small quantization blocks in this probe. Naive 8-bit AdamW was worse than FP32 and sometimes diverged; error feedback reduced the final-loss gap to FP32 in both 60-step seeds.

## Boundaries and scale limits

Synthetic deterministic data only; 60 steps only; no real-corpus pretraining, no downstream evaluation, no long-horizon stability test, no mature production optimizer comparison, and no full memory-savings accounting beyond observed GB10 execution posture.

## Claim scope

On a GB10, a self-contained GPT-2-small-class synthetic next-token probe with 123.7M parameters, sequence length 64, batch size 1, and 60 optimizer steps showed that 256-element block error-feedback 8-bit AdamW stayed much closer to FP32 AdamW than naive 8-bit AdamW across two seeds; 2048-element blocks diverged immediately.

## Why it stopped

No-paper useful signal: the local evidence supports the mechanism in a short synthetic GPT-2-small-class probe, but it is not direct or long enough to validate real GPT-2-small training.

## Recommended next action

Run a bounded real-text GPT-2-small follow-up for 1,000-5,000 steps with FP32, naive 8-bit, and error-feedback 8-bit controls plus block-size ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GPT-2-small error-feedback 8-bit AdamW confirmation
- Success threshold: Error-feedback 8-bit AdamW validation loss remains within 5% of FP32 AdamW and is at least 2x closer to FP32 than naive 8-bit AdamW at matched step count without divergence.
- Stop condition: Stop early if error-feedback 8-bit AdamW diverges, exceeds FP32 validation loss by more than 15% after warmup, or provides no clear advantage over naive 8-bit across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/error-feedback-8-bit-adamw-for-gpt-2-small-on-gb10-89ce854f3a1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
