# CPU-N-gram speculative decoding without draft model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-without-draft-model-vram-9370ed05804e`
Run ID: `cpu-n-gram-speculative-decoding-without-draft-model-vram-9370ed05804e-20260525T002807054936+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4c3c71d5549d

## What looked useful

Overall estimated verifier-call reduction was 11.3% over 768 generated tokens; structured prompts reached 27.4% and one JSON-lines prompt reached 69.8%, while code and general prose showed 0.0% call reduction. CPU lookup overhead was about 1 microsecond per step in Python.

## Boundaries and scale limits

Tested only 8 prompts x 96 generated tokens on a 0.6B model with trace replay, not an optimized serving implementation; no 7B+ model, sampling mode, concurrent serving, KV-cache verifier kernel, or end-to-end latency validation was performed.

## Claim scope

A trace-level greedy replay benchmark with Qwen/Qwen3-0.6B shows that CPU n-gram speculation without draft-model VRAM can reduce estimated verifier calls on copy-heavy structured continuations, but not reliably across a mixed prompt suite.

## Why it stopped

Bounded trace evidence supports a narrow mechanism but does not support a broad or paper-ready claim; this is not a full validation because serving latency, KV-cache verifier implementation, larger models, and sampling behavior were not tested.

## Recommended next action

Stop this run as no-paper useful signal; next concrete test is an end-to-end serving-path prototype gated on at least 15% wall-clock latency improvement on structured outputs with no more than 3% regression on mixed prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU n-gram verifier in a real serving loop
- Success threshold: At least 15% median wall-clock latency improvement on structured/copy-heavy prompts, no more than 3% median latency regression on mixed prompts, and zero draft-model VRAM use.
- Stop condition: Stop if end-to-end latency gain is below 10% on structured prompts or mixed-prompt regressions exceed 5%, even when trace-level acceptance looks favorable.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-without-draft-model-vram-9370ed05804e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
