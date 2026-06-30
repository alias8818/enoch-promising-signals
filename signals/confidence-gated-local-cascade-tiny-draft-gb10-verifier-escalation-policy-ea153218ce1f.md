# Confidence-gated local cascade: tiny draft, GB10 verifier, escalation policy

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-local-cascade-tiny-draft-gb10-verifier-escalation-policy-ea153218ce1f`
Run ID: `confidence-gated-local-cascade-tiny-draft-gb10-verifier-escalation-policy-ea153218ce1f-20260611T093805337053+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d6ec3c49fcf5

## What looked useful

Five 200k-request synthetic sweeps found stable lowest-latency feasible policies at mean accuracy 0.8611 versus verifier-only 0.8297, mean escalation rate 0.1455, and mean expected latency 123.74 ms with 850 ms remote latency. The draft stage was accepted for only about 5.6% of requests in the latency-optimal policy, so the useful mechanism is primarily verifier confidence gating plus escalation.

## Boundaries and scale limits

The quality/correctness side is synthetic and does not validate real LLM calibration, token-level latency, batching, KV-cache effects, task utility, or production remote escalation. CUDA timings are microbenchmarks, not full model inference.

## Claim scope

On this GB10 host, a bounded synthetic confidence/correctness workload plus measured CUDA proxy costs supports a narrow cascade mechanism: verifier-mostly local serving with escalation on low verifier confidence can exceed verifier-only synthetic accuracy while escalating about 14.6% of requests.

## Why it stopped

Closed as no-paper useful signal: the run produced direct GB10 compute calibration and stable synthetic policy evidence, but the central LLM quality claim remains proxy-only rather than full validation.

## Recommended next action

Run a bounded direct validation with real local tiny and verifier models on a small QA/classification set, measuring calibration, end-to-end latency, and escalation rate against verifier-only and remote-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny/verifier cascade validation on real prompts
- Success threshold: At least 3 percentage points accuracy gain over verifier-only or matched accuracy with at least 30% lower expected latency than remote-only, with escalation rate below 25% on at least 500 real examples.
- Stop condition: Stop if real confidence calibration fails to separate correct from incorrect outputs enough to reach the target quality below 40% escalation, or if local end-to-end verifier latency dominates expected latency enough that remote-only is faster at matched quality.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-local-cascade-tiny-draft-gb10-verifier-escalation-policy-ea153218ce1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
