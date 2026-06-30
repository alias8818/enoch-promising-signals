# N-Gram Draft Speculative Decoding for CPU Inference Speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-cpu-inference-speedup-e4cf04b700c3`
Run ID: `n-gram-draft-speculative-decoding-for-cpu-inference-speedup-e4cf04b700c3-20260607T071245537359+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/af1f0231b993

## What looked useful

Natural prose accepted too few drafts to offset verifier block cost: best projected wall speedups were 0.565x on Alice and 0.536x on Sherlock. A repetitive code-like control accepted nearly all drafts and projected 2.366x at order=8, gamma=4.

## Boundaries and scale limits

No actual Transformer decoder, KV cache, tokenizer-specific BPE/SentencePiece behavior, probabilistic sampling, or serving runtime was benchmarked. Corpora were small open/proxy traces evaluated for up to 50k new tokens.

## Claim scope

Bounded trace-level evidence shows n-gram prompt-lookup speculative decoding can reduce verifier calls and project to CPU speedup on highly repetitive code-like continuations, but not on ordinary prose traces under a one-thread dense verifier-cost proxy.

## Why it stopped

Proxy/trace evidence is mixed and does not validate broad CPU inference speedup; it only supports a workload-conditional mechanism signal.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a direct CPU model-backed benchmark on code/repetitive prompts with adaptive fallback for prose.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-backed CPU benchmark for adaptive n-gram speculative decoding
- Success threshold: At least 1.3x wall-clock speedup on repetitive/code prompts with no more than 5% slowdown on prose after adaptive fallback, measured over at least 100 prompts or 50k generated tokens per class.
- Stop condition: Stop if direct CPU wall-clock speedup is below 1.1x on repetitive/code prompts or if adaptive fallback cannot keep prose slowdown within 5%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-cpu-inference-speedup-e4cf04b700c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
