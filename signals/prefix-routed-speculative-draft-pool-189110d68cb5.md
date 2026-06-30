# Prefix-Routed Speculative Draft Pool

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prefix-routed-speculative-draft-pool-189110d68cb5`
Run ID: `prefix-routed-speculative-draft-pool-189110d68cb5-20260526T080421061136+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12a892dcebd7

## What looked useful

Prefix routing improved accepted-token yield in the proxy, but exact longer-prefix routing quickly became coverage limited. Route length 1 improved mean accepted tokens by +0.449 in the main run and by +0.3356 on average across five smaller seeds.

## Boundaries and scale limits

Proxy-only evidence: 5-gram target, greedy continuation matching, Wikitext-2, no transformer logits, no KV-cache or batching behavior, no latency or tokens/sec serving measurement, and no comparison to a learned neural drafter.

## Claim scope

In a Wikitext-2 n-gram speculative-decoding proxy, a fixed-size prefix-routed stored continuation pool improved mean accepted draft tokens versus a same-size global pool baseline, with route length 1 consistently best across one main run and five smaller seeds.

## Why it stopped

Proxy evidence supports the mechanism but is insufficient for a paper or deployment claim because no real transformer speculative decoding or serving throughput was measured.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should wrap the same routing idea around a small transformer target and measure accepted tokens per target forward pass plus tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of prefix-routed draft pools
- Success threshold: Route length 1 or 2 improves accepted tokens per target forward pass by at least 20% and end-to-end tokens/sec by at least 10% versus the global pool baseline in at least 3 seeds, without coverage below 30%.
- Stop condition: Stop if no route length improves accepted tokens per target forward pass by at least 10%, or if the best route's coverage is below 20% under equal memory.

## Evidence references

- Artifact root: `<local-path>/projects/prefix-routed-speculative-draft-pool-189110d68cb5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
