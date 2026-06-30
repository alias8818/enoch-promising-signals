# Production-style CPU prompt n-gram drafting for larger single-GPU inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `production-style-cpu-prompt-n-gram-drafting-for-larger-sin-b3089b0f75`
Run ID: `production-style-cpu-prompt-n-gram-drafting-for-larger-sin-b3089b0f75-20260609T080355115195+0000`

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

- Parent run decision: CPU n-gram draft speculative decoding for single-GPU inference: enoch://control-plane/projects/cpu-n-gram-draft-speculative-decoding-for-single-gpu-inference-a0bde0c904f4/runs/cpu-n-gram-draft-speculative-decoding-for-single-gpu-inference-a0bde0c904f4-20260609T042838568588+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

The mechanism worked when prompt continuations were reusable: median speedups were 4.318x and 2.478x on repeated-code prompts for 0.5B and 1.7B models, with exact greedy equivalence. No-repeat controls fell back to baseline behavior with about 1.0x speedup and no forward-call reduction.

## Boundaries and scale limits

Synthetic prompts; one GPU; no concurrent serving; no continuous batching; no optimized inference engine integration; largest model tested was 1.7B, not 7B+; no real production prompt trace.

## Claim scope

In a bounded local Python/Hugging Face greedy decoding harness on one GB10 GPU, CPU prompt n-gram drafting preserved exact greedy output and reduced decode latency for synthetic repeated or patterned prompts on 0.5B and 1.7B causal LMs.

## Why it stopped

Tier 1 controlled direct test met the mechanism threshold but remains no-paper because prompts were synthetic and the verifier was not integrated into a production inference engine.

## Recommended next action

Run a bounded deepen follow-up inside a serving-style harness using realistic long-prompt traces and at least one 7B-class model, measuring p50/p95 latency, acceptance distribution, CPU load, and no-hit overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving-style prompt n-gram drafting on realistic long-prompt traces
- Success threshold: On at least 200 realistic long-prompt requests and one 7B-class model or production-equivalent verifier, median decode latency improves by >=1.15x with exact greedy output and no-hit overhead <=5%.
- Stop condition: Stop if exact greedy equivalence fails, if no-hit overhead exceeds 5% after implementation tuning, or if realistic traces show median speedup below 1.05x despite acceptance rates below 20%.

## Evidence references

- Artifact root: `<local-path>/projects/production-style-cpu-prompt-n-gram-drafting-for-larger-sin-b3089b0f75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
