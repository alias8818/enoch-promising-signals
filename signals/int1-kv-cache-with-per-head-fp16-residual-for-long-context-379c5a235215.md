# INT1 KV-Cache with Per-Head FP16 Residual for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `int1-kv-cache-with-per-head-fp16-residual-for-long-context-379c5a235215`
Run ID: `int1-kv-cache-with-per-head-fp16-residual-for-long-context-379c5a235215-20260608T065715229781+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e2b1eb0a4bf6

## What looked useful

Residual channels monotonically improve INT1 KV reconstruction on GPT-2 activations, but the remaining attention distortion is too high at useful compression ratios: at 7.1x FP16 KV compression output NRMSE is 0.545 with attention KL 0.517, and even at 3.0x compression output NRMSE is 0.408 with attention KL 0.308.

## Boundaries and scale limits

No end-to-end perplexity, generation-quality, decode-kernel, long-context-capable model, 7B+ model, or production serving benchmark was run. GPT-2 evidence is direct activation evidence but not direct long-context evidence because GPT-2-small is position-limited to 1024 tokens.

## Claim scope

Bounded mechanism test of INT1 sign-quantized KV tensors with per-token/head FP16 scales and per-head FP16 residual channels, measured by attention-output distortion on synthetic 2048/8192-token tensors and GPT-2-small layer-0 activations capped to 1024 tokens.

## Why it stopped

Early proxy and direct GPT-2 activation tests falsified the practical hypothesis rather than providing full validation: simple per-head FP16 residual channels improve INT1 KV but do not preserve attention outputs well enough for long-context KV-cache claims.

## Recommended next action

Stop this INT1-plus-residual formulation as a paper path; only revisit if a different residual structure first reaches attention-output NRMSE below 0.10 at at least 6x FP16 KV compression on a long-context-capable model.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/int1-kv-cache-with-per-head-fp16-residual-for-long-context-379c5a235215`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
