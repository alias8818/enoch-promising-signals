# Direct n-gram speculative decoding test on a small 2-bit transformer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-n-gram-speculative-decoding-test-on-a-small-2-bit-t-be948c0561`
Run ID: `direct-n-gram-speculative-decoding-test-on-a-small-2-bit-t-be948c0561-20260529T042513349230+0000`

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

- Parent run decision: N-gram spec decoding against 2-bit model: enoch://control-plane/projects/n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4/runs/n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4-20260528T233200932446+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/862178abae9a

## What looked useful

Dynamic prompt-lookup n-gram speculation can exploit repeated context in a small 2-bit transformer to reduce verifier target forwards while preserving exact greedy output; generic static corpus n-grams did not help.

## Boundaries and scale limits

Small prompt set, CPU-only PyTorch execution, fake 2-bit value quantization rather than packed int2 kernels, degraded/repetitive quantized model outputs, and no KV-cache-optimized serving implementation.

## Claim scope

On a 12-prompt, 32-token controlled test with distilgpt2 fake-quantized to 2-bit per-row weight values, dynamic context n-gram speculative decoding preserved exact greedy outputs and reduced target-model forward calls by 39.84375%; a static corpus n-gram control reduced 0%.

## Why it stopped

Tier 1 direct test produced a useful mechanism signal but not paper-ready evidence because the fake-quantized model is degraded and the timing stack is not realistic serving.

## Recommended next action

Run a bounded deepen test on a healthier group-wise or packed 2-bit small transformer with a broader prompt suite and KV-cache-aware timing; stop if exact-match forward reduction falls below 15%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dynamic n-gram speculative decoding on a healthier group-wise 2-bit small transformer
- Success threshold: All prompts exact-match greedy output and aggregate target-forward reduction >= 15% without relying on visibly degenerate repetitive output.
- Stop condition: Stop if exact-match fails, aggregate target-forward reduction is below 15%, or repetition diagnostics show the gain is dominated by quantization-induced degenerate loops.

## Evidence references

- Artifact root: `<local-path>/projects/direct-n-gram-speculative-decoding-test-on-a-small-2-bit-t-be948c0561`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
