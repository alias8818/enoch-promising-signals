# CPU n-gram draft speculative decoding for single-GPU inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-n-gram-draft-speculative-decoding-for-single-gpu-inference-a0bde0c904f4`
Run ID: `cpu-n-gram-draft-speculative-decoding-for-single-gpu-inference-a0bde0c904f4-20260609T042838568588+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

The mechanism worked exactly: all rows matched cached greedy baseline output. Best ngram=2 results were 2.37x mean speedup on distilgpt2 open prompts, 2.63x on distilgpt2 copy-heavy prompts, 1.90x on gpt2 open prompts, and 3.44x on gpt2 copy-heavy prompts, with 53% to 79% mean verifier-pass reductions.

## Boundaries and scale limits

Tested only distilgpt2 and gpt2, single-prompt greedy decoding, 48 generated tokens, small prompt suites, Python research harness, no batching, no sampling, no production inference runtime, and no larger modern LLM.

## Claim scope

On GB10 single-GPU GPT-2-class greedy decoding, a CPU prompt n-gram drafter with exact target verification preserved baseline outputs and reduced verifier passes enough to improve single-prompt wall-clock latency on small open and copy-heavy prompt suites.

## Why it stopped

Not paper-ready: evidence is bounded to GPT-2-class greedy decoding in a Python harness, though it directly supports the local mechanism.

## Recommended next action

Stop this run as a useful no-paper signal; next run should implement the same CPU n-gram drafter inside a production-style inference loop for a larger single-GPU model and compare p50/p95 latency on real copy-heavy prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-style CPU prompt n-gram drafting for larger single-GPU inference
- Success threshold: Exact-output match rate 1.0 for greedy decoding and at least 20% p50 latency reduction on copy-heavy prompts without more than 5% regression on open-ended controls.
- Stop condition: Stop if exactness fails, CPU draft overhead exceeds verifier savings, or copy-heavy p50 latency improvement is below 10% after a calibrated implementation.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-speculative-decoding-for-single-gpu-inference-a0bde0c904f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
