# N-gram Suffix Matching for Speculative Decoding in Resource-Constrained Envs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-matching-for-speculative-decoding-in-resource-constrained-envs-823651aa8607`
Run ID: `n-gram-suffix-matching-for-speculative-decoding-in-resource-constrained-envs-823651aa8607-20260621T065301951514+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/c306aceb6219

## What looked useful

Use n-gram suffix matching only behind workload/acceptance gating in resource-constrained deployments. Conservative max_n=2-4 captured most benefit; max_n=8 increased memory sharply, reaching about 498 MB peak traced allocation on the low-overlap 64k/16k negative control with 1.0x pass reduction.

## Boundaries and scale limits

No target LLM was run; metrics are oracle-stream proposer acceptance and pass-reduction upper bounds, not end-to-end GPU serving speedups. Workloads are synthetic/proxy, single-process Python, up to 65,536 prompt tokens and 16,384 output tokens.

## Claim scope

A bounded synthetic/proxy benchmark shows online n-gram suffix matching can produce large verifier-pass reduction upper bounds on copy-heavy, structured, and repetitive token streams with low query overhead when n-gram length is capped, but gives no benefit on low-overlap streams.

## Why it stopped

Proxy evidence supports the mechanism only for overlap-heavy workloads and falsifies generic low-overlap usefulness; it is not direct full validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should integrate the capped proposer into a real small-model inference loop and measure wall-clock latency against no speculation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model latency validation for gated n-gram suffix speculation
- Success threshold: At least 20% end-to-end tokens/sec improvement on overlap-heavy workloads, less than 5% regression on low-overlap workloads, and proposer memory under 100 MB at 64k prompt tokens.
- Stop condition: Stop if real-model speedup is under 10% on copy-heavy workloads or low-overlap prompts regress by 5% or more after gating.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-matching-for-speculative-decoding-in-resource-constrained-envs-823651aa8607`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
