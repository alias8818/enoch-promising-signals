# Jacobi fixed-point lookahead decoding without draft weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `jacobi-fixed-point-lookahead-decoding-without-draft-weights-0d7c61c20a90`
Run ID: `jacobi-fixed-point-lookahead-decoding-without-draft-weights-0d7c61c20a90-20260528T203227668093+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0fe59159b73c

## What looked useful

Full-window Jacobi propagation accepted about jacobi_steps tokens and preserved exact full-context greedy decoding, but each outer iteration cost jacobi_steps plus one full-context verification forward. The best tested medium setting, window=8 and jacobi_steps=4, reached 4.04 accepted tokens per outer iteration but only 0.434x the wall-clock speed of KV-cache greedy and used far more model-token work.

## Boundaries and scale limits

Tested on one GB10 GPU, GPT-2 small only, batch size 1, 12 prompts for the fp16 medium probe and 4 prompts for float32 controls. This is not a full LADE n-gram-pool implementation and does not validate large-model serving kernels, sampling, batching, or long-context production workloads.

## Claim scope

On GPT-2 small with greedy decoding, a simple target-model-only Jacobi fixed-point lookahead verifier can exactly match full-context greedy outputs and accept multiple tokens per outer iteration, but it does not beat standard KV-cache greedy decoding in wall-clock time or target-forward count.

## Why it stopped

Bounded local evidence supports the exact draft-free mechanism but falsifies the practical speedup claim for the naïve Jacobi verifier; this is a proxy/early practical falsification, not a full validation of optimized Lookahead Decoding.

## Recommended next action

Stop this naïve implementation as no-paper evidence; the concrete bounded next action is to test an n-gram-pool/reuse implementation against the same GPT-2 KV-cache baseline before considering larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: N-gram-pool Jacobi lookahead versus GPT-2 KV-cache greedy
- Success threshold: Exact match on all prompts and at least 1.1x mean wall-clock speedup over KV-cache greedy without increasing target-forward count.
- Stop condition: Stop if exactness fails or if the best tuned n-gram-pool configuration remains below 1.0x mean wall-clock speedup versus KV-cache greedy on the bounded GPT-2 benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/jacobi-fixed-point-lookahead-decoding-without-draft-weights-0d7c61c20a90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
