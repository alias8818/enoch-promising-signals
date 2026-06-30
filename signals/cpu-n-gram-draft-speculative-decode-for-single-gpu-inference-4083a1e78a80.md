# CPU n-gram draft speculative decode for single-GPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-speculative-decode-for-single-gpu-inference-4083a1e78a80`
Run ID: `cpu-n-gram-draft-speculative-decode-for-single-gpu-inference-4083a1e78a80-20260601T015341924693+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e56b47024e72

## What looked useful

The repeated ticket prompt achieved exact output equality with 1.17x, 2.24x, and 3.90x median speedups for draft sizes 2, 4, and 8 by reducing model forward calls from 97 to 49/25/13. Natural prose remained exact but was slower at about 0.97x. Repeated code showed apparent speedups but failed output-hash equality, making those speedups invalid for exact greedy decoding.

## Boundaries and scale limits

Tested only 3 local prompts, 96 generated tokens, 3 repeats, distilgpt2, Hugging Face Transformers, and one GB10 GPU. Did not test production inference engines, batching, long-context real traces, or 1B-7B+ models.

## Claim scope

On GB10 with a CUDA distilgpt2 verifier and CPU prompt-lookup n-gram drafts, highly repetitive templated prompts can reduce verifier calls and improve exact greedy-equivalent latency; natural prose did not speed up, and a code-like repeated prompt exposed a correctness hazard in the cached multi-token verifier prototype.

## Why it stopped

Bounded local evidence is mixed: a clean exact speedup exists on one repeated template, but natural prose is slower and a code-like repeated prompt reveals a correctness hazard, so this is not a robust paper-ready inference result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should first implement and validate a production-grade exact KV-cache verifier, then rerun on real repeated-prompt traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact KV-cache prompt-lookup drafting on real repeated inference traces
- Success threshold: On exact-output runs, achieve at least 1.5x median latency speedup on the repetitive trace slice with less than 5% median slowdown on non-repetitive controls.
- Stop condition: Stop if exact output equality cannot be maintained across the validation prompts, or if repetitive-trace speedup remains below 1.2x after verifier correctness is fixed.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-speculative-decode-for-single-gpu-inference-4083a1e78a80`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
