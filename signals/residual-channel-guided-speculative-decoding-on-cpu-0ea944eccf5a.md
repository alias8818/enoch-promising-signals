# Residual-Channel-Guided Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-guided-speculative-decoding-on-cpu-0ea944eccf5a`
Run ID: `residual-channel-guided-speculative-decoding-on-cpu-0ea944eccf5a-20260527T232330933386+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/98c7eafd6b81

## What looked useful

Residual-channel summaries carried accept/reject information that draft margin did not: medium-run AUC improved from 0.6547 to 0.9148 and residual-guided throughput improved by 3.8493%. Five robustness seeds reproduced a mean +3.7364% gain vs best fixed-k.

## Boundaries and scale limits

No real transformer, tokenizer, KV cache, sampling distribution, draft/target model pair, or wall-clock inference kernel was evaluated. The result is mechanism-level synthetic evidence only.

## Claim scope

In a NumPy synthetic CPU proxy where target/draft disagreement is partly encoded in residual-channel summaries, residual-channel-guided speculative block sizing improved held-out emitted tokens per synthetic cost by about 3.7-3.9% over best fixed-k and margin-only controls.

## Why it stopped

Closed as a no-paper useful signal because the current evidence is synthetic/proxy-only, not direct validation of residual-channel-guided speculative decoding on real CPU LLM inference.

## Recommended next action

Run a bounded real-model CPU follow-up using a small draft/target transformer pair, real residual-stream features, and wall-clock speculative decoding throughput before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Model Residual-Guided Speculative Decoding Trace Test
- Success threshold: Residual-guided policy improves wall-clock tokens/sec by at least 3% over the best fixed-k baseline and at least 2% over confidence-only guidance on held-out prompts without reducing output equivalence under the chosen decoding mode.
- Stop condition: Stop if residual features fail to improve accept-prediction AUC by at least 0.05 over confidence-only features or if wall-clock throughput is not positive after tuning fixed-k and confidence-only baselines.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-guided-speculative-decoding-on-cpu-0ea944eccf5a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
