# Dynamic n-gram speculative decoding on a healthier group-wise 2-bit small transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-n-gram-speculative-decoding-on-a-healthier-group-w-22331242fa`
Run ID: `dynamic-n-gram-speculative-decoding-on-a-healthier-group-w-22331242fa-20260529T085313606602+0000`

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

- Parent run decision: Direct n-gram speculative decoding test on a small 2-bit transformer: enoch://control-plane/projects/direct-n-gram-speculative-decoding-test-on-a-small-2-bit-t-be948c0561/runs/direct-n-gram-speculative-decoding-test-on-a-small-2-bit-t-be948c0561-20260529T042513349230+0000
- Parent run decision: N-gram spec decoding against 2-bit model: enoch://control-plane/projects/n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4/runs/n-gram-spec-decoding-against-2-bit-model-917bfe30ceb4-20260528T233200932446+0000

## What looked useful

Dynamic n2-8 speculative decoding achieved 100% exact-match rate, 18.625 mean target calls for 32 generated tokens, 41.8% call reduction versus greedy, 0.830 acceptance rate, and 2.03x CPU wall speedup versus greedy. However static_n2 achieved 18.500 mean target calls, 42.2% call reduction, and 2.28x wall speedup, so dynamic did not clear the real static baseline.

## Boundaries and scale limits

Three fixed seeds over eight hand-constructed prompts and 32 generated tokens per prompt; fake fp-tensor 2-bit quantization rather than packed int2 kernels; full-context CPU verifier rather than production KV-cache/GPU serving; not a broad corpus or larger-model validation.

## Claim scope

On a CPU-only direct test using distilgpt2 with deterministic group-wise 2-bit fake-quantized non-embedding weights, prompt-lookup speculative decoding exactly matches greedy decoding and reduces target forward calls substantially versus greedy; the tested dynamic n-gram policy does not outperform the best fixed static_n2 control.

## Why it stopped

Tier 2 direct evidence supports the mechanism versus greedy but falsifies the stronger dynamic-policy superiority claim against a real static n-gram control.

## Recommended next action

Stop this branch as no-paper useful evidence; if deepened, test a learned or tuned dynamic policy against best-of-static n on a larger held-out prompt corpus with a KV-cache verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tuned dynamic prompt-lookup speculative decoding versus best static n with KV-cache verification
- Success threshold: Dynamic policy reduces mean target calls by at least 5% versus the best fixed static n baseline while preserving 100% exact greedy equivalence and not regressing wall-clock latency.
- Stop condition: Stop if dynamic fails to beat best static n by 5% target calls, any exact-match regression appears, or KV-cache wall-clock latency is worse than best static n.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-n-gram-speculative-decoding-on-a-healthier-group-w-22331242fa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
