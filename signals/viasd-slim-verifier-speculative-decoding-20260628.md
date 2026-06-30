# VIA-SD slim-verifier tier for speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `viasd-slim-verifier-speculative-decoding-20260628`
Run ID: `viasd-slim-verifier-speculative-decoding-20260628-20260629T065258208026+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-206 frontier research issue: linear-ALI-206
- VIA-SD slim-verifier tier for speculative decoding: https://zju-xyc.github.io/VIA-SD-Project-Page/
- VIA-SD slim-verifier tier for speculative decoding: https://arxiv.org/abs/2606.12243v1

## What looked useful

Best tested pair (draft hidden 3, slim hidden 5) rescued 36.36% of draft misses, reduced exact full-call rate to 65.625%, but only reached 0.915x modeled speedup at slim cost 0.45/full cost 1.0. It would need slim cost <=0.34375 of full cost to break even.

## Boundaries and scale limits

Not a production speculative decoder, not a large-model serving benchmark, not a trained/routed VIA-SD slim verifier, and not a broad task suite. Cost is analytic rather than measured kernel latency.

## Claim scope

Bounded distilgpt2 early-exit proxy over 32 fixed prompts: slim intermediate layers sometimes rescue draft-layer top-1 misses, but exact top-1 preserving routing is slower than standard draft+full speculative decoding under the tested cost model.

## Why it stopped

Proxy early falsification of the simple early-exit slim-verifier tier: the mechanism appears but does not overcome slim-tier overhead under exact top-1 preservation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should implement an actually routed/pruned slim verifier and measure latency plus fidelity on a larger prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure routed/pruned slim-verifier latency and fidelity versus early-exit proxy
- Success threshold: Measured speedup >=1.10x over standard SD at >=99% top-1 agreement versus the full verifier, with slim tier measured at <=30% of full verifier cost.
- Stop condition: Stop if slim measured cost exceeds 40% of full verifier cost or if confidence routing cannot reach 99% top-1 agreement with full-call rate below 60%.

## Evidence references

- Artifact root: `<local-path>/projects/viasd-slim-verifier-speculative-decoding-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
