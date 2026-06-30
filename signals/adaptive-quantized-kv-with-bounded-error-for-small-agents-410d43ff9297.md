# Adaptive Quantized KV with Bounded Error for Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-quantized-kv-with-bounded-error-for-small-agents-410d43ff9297`
Run ID: `adaptive-quantized-kv-with-bounded-error-for-small-agents-410d43ff9297-20260525T082231326463+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ed250168d09

## What looked useful

Strict 3-10% relative attention-output certificates were not achievable even with 8-bit KV, so the adaptive bounded allocator could not save memory under practical strict budgets. Very loose 50-100% certificates did pass and saved 10.69-24.37% bits versus the lowest bound-passing uniform scheme, but those budgets are too weak for a paper-ready quality guarantee.

## Boundaries and scale limits

No full model generation, no real transformer KV traces, no multi-layer accumulation, no hardware serving benchmark, and no datacenter-scale validation. Results address the tested bounded allocator, not all KV quantization methods.

## Claim scope

Synthetic one-step small-agent decode attention probe with sequence length 512, head dimension 64, per-vector symmetric K/V quantization, and a conservative query-conditioned analytic attention-output error surrogate.

## Why it stopped

Proxy early falsification: in the direct synthetic attention-output test, the conservative bounded allocator saturated at 8 bits and still failed 3-10% certification, while memory savings appeared only for very loose 50-100% certificates.

## Recommended next action

Stop this run as a no-paper useful negative; next bounded work should test a tighter or calibrated probabilistic bound on real small-transformer KV traces before any serving-scale benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated probabilistic KV error bounds on real small-transformer traces
- Success threshold: At eps_rel between 0.03 and 0.10, achieve at least 99% bound satisfaction, 100% actual-error pass rate on held-out traces, and at least 20% mean-bit reduction versus the lowest uniform bitwidth satisfying the same bound.
- Stop condition: Stop if no tested calibrated bound achieves any mean-bit reduction versus uniform 8-bit while satisfying at least 99% of 3-10% certificates on held-out real traces.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-quantized-kv-with-bounded-error-for-small-agents-410d43ff9297`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
