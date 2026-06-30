# 1-Bit Weights with Learned Residual Channel Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-weights-with-learned-residual-channel-recovery-7e0db4746f2f`
Run ID: `1-bit-weights-with-learned-residual-channel-recovery-7e0db4746f2f-20260522T002634513314+0000`

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

Top-k residuals reduced teacher-logit MSE versus binary-only by 57.6% at 1.46% residual-weight overhead, 85.4% at 5.83%, and 96.0% at 23.31%; however binary-only accuracy was already 99.733% versus dense 99.917%, so no meaningful task-accuracy gain was demonstrated.

## Boundaries and scale limits

Evidence is limited to a small synthetic MLP with saturated classification accuracy. It does not validate language-model perplexity, GPT-2-small-class behavior, end-to-end quantization-aware training, downstream tasks, or hardware throughput.

## Claim scope

In a three-seed synthetic 10-class MLP teacher recovery probe, sparse learned full-precision residual weights per output channel substantially reduced teacher-logit MSE after per-output scaled 1-bit weight binarization, and top-k quantization-error channel selection outperformed a random same-budget residual control.

## Why it stopped

No-paper closure: this is a bounded synthetic mechanism signal, not direct publication-grade evidence for 1-bit model accuracy or perplexity improvement.

## Recommended next action

Run a bounded non-saturated tiny transformer or GPT-2-small-class perplexity test with dense, binary-only, random-residual, and top-k-residual controls before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Perplexity Test for 1-Bit Top-k Residual Channel Recovery
- Success threshold: Top-k residual variant closes at least 50% of the binary-only validation perplexity gap to dense and beats random residual at the same overhead on at least two of three seeds.
- Stop condition: Stop if binary-only has no measurable perplexity gap to dense, or if top-k residual fails to beat random residual at matched overhead on two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-learned-residual-channel-recovery-7e0db4746f2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
