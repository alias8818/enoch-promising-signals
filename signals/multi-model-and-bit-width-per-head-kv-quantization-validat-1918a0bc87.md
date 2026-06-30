# Multi-model and bit-width per-head KV quantization validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-model-and-bit-width-per-head-kv-quantization-validat-1918a0bc87`
Run ID: `multi-model-and-bit-width-per-head-kv-quantization-validat-1918a0bc87-20260523T093104546228+0000`

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

- Parent run decision: Standard-corpus per-head KV quantization validation: enoch://control-plane/projects/standard-corpus-per-head-kv-quantization-validation-f03eefa015/runs/standard-corpus-per-head-kv-quantization-validation-f03eefa015-20260523T071914512907+0000
- Parent run decision: Per-Head KV Quantization: enoch://control-plane/projects/per-head-kv-quantization-bfca23eac609/runs/per-head-kv-quantization-bfca23eac609-20260523T051744474729+0000

## What looked useful

Uniform per-head 4-bit K+V quantization had modest PPL increases on distilgpt2 and gpt2 (1.122x and 1.202x), much better than per-tensor 4-bit (1.510x and 1.968x). Mixed average-4-bit schedules were much worse (2.458x-10.645x PPL ratios), and K-only ablations showed keys are the more fragile target.

## Boundaries and scale limits

Tested activation fake quantization during forward-pass perplexity only: sshleifer/tiny-gpt2, distilgpt2, and gpt2; 96 chunks of length 256; 3 fixed seeds. No 7B+ checkpoints, learned allocator, long-context generation, real compressed KV-cache kernel, latency, or memory benchmark.

## Claim scope

On WikiText-2 validation with GPT-2-family checkpoints, per-head KV scaling improves 4-bit activation quantization versus per-tensor scaling, but naive average-4-bit mixed per-head schedules with 2/4/8-bit heads are worse than uniform per-head 4-bit.

## Why it stopped

Tier-2 validation produced a useful but no-paper result: the tested naive mixed-bit per-head schedules fail against the real uniform per-head 4-bit baseline, while per-head scaling itself remains useful.

## Recommended next action

Run a bounded calibrated-allocation follow-up that forbids 2-bit keys and compares sensitivity-based per-head K/V bit assignment against uniform per-head 4-bit on the same models and a longer-context generation-cache metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated no-2-bit-key per-head KV bit allocation
- Success threshold: Calibrated mixed allocation has mean PPL ratio no more than 1.03x uniform per-head 4-bit and at least 10% lower average KV bit budget, with no model worse than 1.05x uniform per-head 4-bit.
- Stop condition: Stop if calibrated mixed allocation exceeds 1.10x the uniform per-head 4-bit PPL ratio on either distilgpt2 or gpt2, or if key sensitivity requires all heads at 4-bit or higher and eliminates the target memory saving.

## Evidence references

- Artifact root: `<local-path>/projects/multi-model-and-bit-width-per-head-kv-quantization-validat-1918a0bc87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
