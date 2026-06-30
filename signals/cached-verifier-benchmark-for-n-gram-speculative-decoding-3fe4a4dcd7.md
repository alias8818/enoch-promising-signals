# Cached verifier benchmark for n-gram speculative decoding on public GPT-2-small prompts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cached-verifier-benchmark-for-n-gram-speculative-decoding-3fe4a4dcd7`
Run ID: `cached-verifier-benchmark-for-n-gram-speculative-decoding-3fe4a4dcd7-20260523T063804491715+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: N-gram draft speculative decoding for GPT-2-small: enoch://control-plane/projects/n-gram-draft-speculative-decoding-for-gpt-2-small-fd39741d5fe2/runs/n-gram-draft-speculative-decoding-for-gpt-2-small-fd39741d5fe2-20260523T035905484135+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8fdc9667bbfb

## What looked useful

Cached verifier reuse materially reduced GPT-2-small verifier work for n-gram speculative decoding while preserving exact outputs in the corrected Tier 1 run: 12/12 outputs matched, 216/356 drafted tokens were accepted, verifier input tokens fell from 16,702 to 2,688, and mean speedup was 1.73x.

## Boundaries and scale limits

Single model size, one GPU host, 12 prompts, short generations, one n-gram order, one draft length, greedy decoding only, TF32 disabled for exact parity, no corpus-scale prompt sweep or production serving integration.

## Claim scope

In a controlled small GPT-2-small CUDA benchmark with 12 embedded public-style prompts, 48 generated tokens per prompt, retrieval 2-gram drafting, and draft length 5, a cached KV verifier exactly matched full-prefix greedy verifier outputs and reduced verifier input tokens by 83.9%, with 1.73x mean wall-clock speedup.

## Why it stopped

Tier 1 controlled direct evidence supports the mechanism but is too narrow for publication readiness; this is a no-paper useful signal rather than a full validation.

## Recommended next action

Run a bounded corpus-backed deepen test on a fixed WikiText/OpenWebText prompt slice with n-gram and draft-length ablations, preserving exact-output parity checks and the TF32/precision caveat.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-backed cached verifier ablation for n-gram speculative decoding
- Success threshold: All evaluated exact-inference conditions must have 100% output parity, and at least one practical condition must show mean speedup >= 1.3x with verifier input-token reduction >= 50% on the corpus prompt slice.
- Stop condition: Stop if any exact-inference condition produces output mismatches after implementation tracing, or if all practical conditions have mean speedup below 1.1x despite verifier input-token reductions.

## Evidence references

- Artifact root: `<local-path>/projects/cached-verifier-benchmark-for-n-gram-speculative-decoding-3fe4a4dcd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
