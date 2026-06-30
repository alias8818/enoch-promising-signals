# 1-bit KV Quantization with Exact Anchor Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-kv-quantization-with-exact-anchor-preservation-c90f9957462b`
Run ID: `1-bit-kv-quantization-with-exact-anchor-preservation-c90f9957462b-20260523T182511064412+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/613e7ca7ee3d

## What looked useful

At 5% exact anchors and 0.124x fp16 KV memory, synthetic anchor-sink attention with 0.870 anchor mass reached relative MSE 0.000540 and top-1 match 1.0, but uniform random attention stayed at relative MSE 0.480 and GPT-2 small activations stayed at relative MSE 0.426-0.429. GPT-2 key-norm anchors were ineffective, with 20% anchors covering only 0.0738 attention mass and relative MSE 0.536.

## Boundaries and scale limits

Tested synthetic scaled-dot-product attention at sequence length 1024, dimension 64, 10 seeds per slice, plus GPT-2 small cached activations on four short text snippets and layers 0/6/11. No end-to-end perplexity, generation, long-context task, larger model, or production KV-cache latency validation was run.

## Claim scope

Bounded synthetic attention and cached GPT-2 small activation probes show that exact anchor preservation can make 1-bit per-token-scale KV quantization accurate only when anchors cover most full-precision attention mass; it does not by itself make general 1-bit KV compression accurate across uniform, non-anchor retrieval, or GPT-2 activation regimes.

## Why it stopped

No-paper closure: bounded direct attention-output evidence is mixed; exact anchors are useful when attention mass is anchored but residual distortion remains high on general and GPT-2 activation regimes.

## Recommended next action

Run a bounded end-to-end GPT-2 small perplexity and long-context retrieval follow-up with actual incremental KV-cache quantization, comparing fp16, int8, no-anchor 1-bit, prefix anchors, and adaptive attention-mass anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 KV-cache validation of exact anchor 1-bit quantization
- Success threshold: At <=0.20x fp16 KV memory, anchored 1-bit KV should recover at least 80% of the perplexity gap between no-anchor 1-bit and fp16 while not degrading long-context retrieval accuracy by more than 5 percentage points versus fp16 on the bounded task.
- Stop condition: Stop if anchored 1-bit improves GPT-2 small perplexity by less than 25% of the no-anchor-to-fp16 gap or fails the non-prefix retrieval task at 20% anchors.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-kv-quantization-with-exact-anchor-preservation-c90f9957462b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
