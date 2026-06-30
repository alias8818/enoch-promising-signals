# N-gram speculative draft for GPT-2-small inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-speculative-draft-for-gpt-2-small-inference-90a9e08cb5c1`
Run ID: `n-gram-speculative-draft-for-gpt-2-small-inference-90a9e08cb5c1-20260603T205654016004+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae55cc497071

## What looked useful

Acceptance was low and model-call reduction was negligible. The strongest apparent speedup was 1.029x for bigram draft length 8, but it matched strict sequential greedy output on only 25% of prompts. More exact configurations had zero or near-zero call reduction and throughput around baseline.

## Boundaries and scale limits

Tested 8 Wikitext-2 validation prompts with 48 generated tokens each on GPT-2-small using CUDA KV-cache inference on NVIDIA GB10. This is not a batched serving benchmark, not sampling, not a domain-repetition workload, and not a comparison against neural or retrieval draft models.

## Claim scope

A simple most-frequent corpus n-gram lookup drafter does not provide a practical exact greedy GPT-2-small speedup on the local Wikitext-2 prompt benchmark tested here.

## Why it stopped

Bounded direct benchmark produced a negative useful signal: low draft acceptance, negligible exact speed benefit, and strict-output divergence when chunk acceptance saved calls.

## Recommended next action

Stop this simple n-gram GPT-2-small accelerator path; use the saved benchmark as a negative control before testing stronger retrieval or neural drafters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retrieval-backed phrase drafter versus n-gram negative control for GPT-2-small
- Success threshold: At least 1.15x mean throughput versus warmed baseline with exact-match fraction 1.0 and at least 15% mean model-call reduction on the bounded prompt set.
- Stop condition: Stop if exact-match fraction is below 1.0 or model-call reduction remains below 10% after tuning retrieval window and draft length.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-gpt-2-small-inference-90a9e08cb5c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
