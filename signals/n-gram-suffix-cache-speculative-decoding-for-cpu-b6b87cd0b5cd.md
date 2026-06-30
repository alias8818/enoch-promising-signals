# N-gram Suffix Cache Speculative Decoding for CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-cache-speculative-decoding-for-cpu-b6b87cd0b5cd`
Run ID: `n-gram-suffix-cache-speculative-decoding-for-cpu-b6b87cd0b5cd-20260527T181850992248+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4449d4107a57

## What looked useful

Prompt-local suffix speculation sped up a repetitive-template workload by 1.87x with 98.3% acceptance and reduced target calls from 1024 to 136, but regressed on code-like reuse at 0.477x with 11.1% acceptance and on random control at 0.785x with 0% acceptance. Training-seeded cache upper bound reached 1.67-1.85x on structured workloads, indicating cache coverage is the main limiter.

## Boundaries and scale limits

Not a pretrained-transformer result; no production KV cache, tokenizer, probability-correct sampling, multi-thread scaling, or natural corpus evaluation. The target decoder is a deterministic suffix oracle with an expensive vectorized verification kernel.

## Claim scope

Controlled NumPy CPU mechanism benchmark for exact greedy n-gram suffix-cache speculative decoding over synthetic repetitive, code-like, and random token workloads.

## Why it stopped

Proxy/mechanism evidence is mixed: conditional speedup exists only at high suffix acceptance, while realistic prompt-local coverage can produce slowdowns. This is useful no-paper evidence, not full validation.

## Recommended next action

Run a bounded direct follow-up against a small real CPU transformer with KV-cache greedy baseline, batched draft verification, and dynamic disable threshold; do not write a paper from this proxy result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer N-gram Suffix Draft Verification
- Success threshold: At least 1.20x geometric-mean throughput improvement on structured prompts with exact outputs and no more than 5% slowdown on low-acceptance controls after gating.
- Stop condition: Stop if acceptance-gated real-transformer runs fail to exceed 1.05x on structured prompts or still exceed 5% slowdown on controls.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-cache-speculative-decoding-for-cpu-b6b87cd0b5cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
