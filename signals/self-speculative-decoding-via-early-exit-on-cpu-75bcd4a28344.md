# Self-Speculative Decoding via Early Exit on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-on-cpu-75bcd4a28344`
Run ID: `self-speculative-decoding-via-early-exit-on-cpu-75bcd4a28344-20260601T023421070064+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/211246bfc7ae

## What looked useful

Early-exit self-speculation on CPU is highly sensitive to acceptance/alignment. In the learnable toy task, 100% early/full agreement yielded exact decoding and 1.30-1.61x speedup for draft lengths 4-8. In the harder recurrence, 24-54% acceptance was insufficient and throughput fell to 0.52-0.80x even while full-depth passes dropped by 41-59%.

## Boundaries and scale limits

No pretrained LLM, no real text corpus, no KV-cache-aware production implementation, no batch-serving test, and no 7B+ model evidence. Positive speedup evidence is limited to two seeds of a trivial deterministic synthetic language.

## Claim scope

On a CPU-only toy causal Transformer with an auxiliary early-exit head, exact greedy self-speculative decoding preserved full-greedy outputs. It produced speedup only when the early head was perfectly aligned on a learnable deterministic Markov task; a harder synthetic recurrence with moderate early/full agreement was slower despite reducing full-depth passes.

## Why it stopped

Bounded toy evidence supports the mechanism only under perfect early/full alignment; the more realistic harder synthetic proxy was slower, so this is not a publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a small real-text or pretrained GPT-2-class model with a KV-cache-aware early-exit verifier and require speedup over full greedy at matched output.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware early-exit self-speculation on a small real-text LM
- Success threshold: At least 1.2x mean CPU tokens/s over matched full greedy on real-text prompts with exact greedy-output preservation and acceptance rate high enough to explain the speedup.
- Stop condition: Stop as negative if acceptance below 60% or mean speedup below 1.0x across draft lengths after a correctly matched KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-on-cpu-75bcd4a28344`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
