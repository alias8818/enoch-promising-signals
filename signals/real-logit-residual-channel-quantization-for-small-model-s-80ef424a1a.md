# Real-logit residual-channel quantization for small-model speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-logit-residual-channel-quantization-for-small-model-s-80ef424a1a`
Run ID: `real-logit-residual-channel-quantization-for-small-model-s-80ef424a1a-20260527T043430201386+0000`

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

- Parent run decision: Joint Residual-Channel Quantization and Speculative Decoding for Small Agents: enoch://control-plane/projects/joint-residual-channel-quantization-and-speculative-decoding-for-small-agents-39fd40287e93/runs/joint-residual-channel-quantization-and-speculative-decoding-for-small-agents-39fd40287e93-20260524T164031044611+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c558e37ba4a

## What looked useful

Residual logit gaps are a useful channel to preserve: residual_int8_clip16 achieved mean TV 0.00655 and p95 acceptance delta 0.295 pp versus exact draft logits, while top512_tail_uniform had mean TV 0.128 and p95 acceptance delta 23.9 pp. The best tested 6-bit setting, residual_int6_clip16, missed the threshold with mean TV 0.0246, p95 acceptance delta 0.881 pp, and top-1 match 0.953.

## Boundaries and scale limits

No full multi-token speculative decoding benchmark, no serving-speed implementation, no larger model pairs, no robustness across corpora, and no adaptive/non-uniform quantizer. Evidence is direct for one-step acceptance only.

## Claim scope

Controlled Tier 1 one-token speculative-acceptance test using real logits from distilgpt2 as draft and gpt2 as target on 384 WikiText-2 validation contexts. Uniform residual logit-gap quantization at 8 bits preserves draft distribution and acceptance overlap closely; tested <=6-bit uniform residual-channel variants do not meet the predefined fidelity threshold.

## Why it stopped

Tier 1 direct evidence supports the residual-logit mechanism at 8 bits but directly falsifies the stated <=6-bit uniform residual-channel threshold in this controlled small-model setup; this is an early bounded falsification, not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test adaptive or non-uniform <=6-bit residual-gap quantization on the same real-logit acceptance harness before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive <=6-bit residual-gap quantization for small-model speculative acceptance
- Success threshold: A <=6-bit adaptive residual-channel scheme reaches mean TV <=0.01, p95 abs acceptance delta <=0.5 percentage points, and top-1 match >=0.99 on the same distilgpt2/gpt2 real-logit harness.
- Stop condition: Stop if the best adaptive <=6-bit scheme still has mean TV >0.015 or p95 abs acceptance delta >0.75 pp after a reasonable clip/codebook grid, because that would indicate the 6-bit target is too aggressive for this channel without a more complex representation.

## Evidence references

- Artifact root: `<local-path>/projects/real-logit-residual-channel-quantization-for-small-model-s-80ef424a1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
