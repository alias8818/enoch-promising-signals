# Prompt-Adaptive N-gram Draft for Lossless CPU Speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-adaptive-n-gram-draft-for-lossless-cpu-speedup-e477a5391a96`
Run ID: `prompt-adaptive-n-gram-draft-for-lossless-cpu-speedup-e477a5391a96-20260531T173612067831+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8deb87dc73eb

## What looked useful

All lossless assertions passed. Across a 24-trial n-gram sweep, copy prompts averaged 1.59x speedup while controls averaged 0.97x. Only 3/24 trials reduced target-model forward calls, but those reduced calls by 85.7% on average and sped up by 3.18x, with a best case of 49 calls reduced to 7 and 3.72x wall speedup.

## Boundaries and scale limits

Small Hugging Face model, hand-written 8-prompt suite, 48 generated tokens, 4 CPU threads; no 7B+ models, quantized runtimes, production serving, sampling, batching, or real RAG/document-copy workload validation.

## Claim scope

On a CPU worker with distilgpt2 greedy decoding, prompt-adaptive n-gram drafting is lossless and can materially speed up prompts whose greedy continuation follows a repeated prompt span, but it did not provide broad speedup across a small mixed prompt suite.

## Why it stopped

No-paper closure: local direct evidence shows a narrow useful mechanism but mixed workload-level value; this is not a full validation of general lossless CPU speedup.

## Recommended next action

Run a bounded deepen benchmark on realistic copy-heavy CPU inference traces, such as RAG answers with citations or code/document continuation prompts, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt n-gram drafting on realistic copy-heavy CPU decoding workloads
- Success threshold: Mean speedup >= 1.25x on copy-heavy prompts, p50 speedup > 1.0x, exact equality on all prompts, and mean control slowdown <= 5%.
- Stop condition: Stop if accepted multi-token draft spans occur in under 10% of copy-heavy prompts or if controls slow down by more than 10% on average.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-adaptive-n-gram-draft-for-lossless-cpu-speedup-e477a5391a96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
