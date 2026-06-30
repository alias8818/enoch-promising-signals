# Prompt n-gram draft accelerates tiny model inference 1.3x

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-n-gram-draft-accelerates-tiny-model-inference-1-3x-ca120be3df33`
Run ID: `prompt-n-gram-draft-accelerates-tiny-model-inference-1-3x-ca120be3df33-20260607T123320147281+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed5c7ff6fa8c

## What looked useful

Prompt n-gram drafting is conditionally useful: repeated/mixed prompts reached 6.89x-7.10x mean speedup with 97.9%-100% draft-token acceptance and 86.46% fewer forward calls, while the low-repeat control reached only 1.01x with 12.5% acceptance and 1.04% fewer forward calls.

## Boundaries and scale limits

Single model, single GPU, synthetic prompt set, greedy decoding only, no KV-cache optimized serving baseline, no sampling, no batching, no real prompt corpus.

## Claim scope

On NVIDIA GB10 with distilgpt2 greedy decoding, prompt n-gram draft verification produced exact greedy-equivalent output and large speedups on synthetic prompts whose continuations copied repeated prompt spans; it did not materially accelerate a low-repeat control.

## Why it stopped

No-paper closure: this run produced a useful conditional mechanism signal, but the positive speedups came from synthetic/proxy repeated prompts rather than a real workload validation.

## Recommended next action

Run a bounded real-prompt follow-up using the same exact-output verifier against an optimized KV-cache baseline and require median speedup >=1.3x on prompts with measured self-repetition.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-prompt prompt n-gram draft benchmark with KV-cache baseline
- Success threshold: Median throughput speedup >=1.3x with exact greedy-equivalent outputs on the repeated-prompt bucket and no material regression on the low-repeat bucket.
- Stop condition: Stop if acceptance rate stays below 30% or median speedup is below 1.1x on repeated real prompts after at least 200 prompt/decode trials.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-draft-accelerates-tiny-model-inference-1-3x-ca120be3df33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
