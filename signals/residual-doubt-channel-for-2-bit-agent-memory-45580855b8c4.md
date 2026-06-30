# Residual-Doubt Channel for 2-Bit Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-doubt-channel-for-2-bit-agent-memory-45580855b8c4`
Run ID: `residual-doubt-channel-for-2-bit-agent-memory-45580855b8c4-20260531T222020890297+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ca8057bf4126

## What looked useful

Across five seeds and 90 seed-condition combinations, a 2-bit residual confidence channel improved reward in 90/90 combinations with mean gain about +0.0425; continuous confidence improved 90/90 with mean gain about +0.0492. A 1-bit channel improved 80/90 but regressed slightly in some easy high-accuracy settings.

## Boundaries and scale limits

Evidence is synthetic and analytic, not from learned neural agents, language-model agents, real-world memory traces, or long-horizon tasks. Reward function explicitly values deferral, and equal-capacity alternative memory allocations were not exhaustively tested.

## Claim scope

In a synthetic 4-state noisy-cue POMDP where 2-bit memory stores only the MAP latent class, a low-bandwidth residual confidence/doubt channel improves risk-sensitive commit/defer reward versus a commit-all 2-bit-memory baseline.

## Why it stopped

Bounded synthetic evidence supports the mechanism, but it is not direct/full validation for learned agents or broad 2-bit memory architectures.

## Recommended next action

Stop this run as no-paper useful signal; next run should train parameter-matched learned agents with a hard 2-bit state and residual doubt channel on the same task family.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned 2-bit recurrent agents with residual doubt on noisy commit/defer tasks
- Success threshold: Residual-doubt learned agents achieve positive held-out reward gain over the 2-bit-only baseline in at least 80% of tested noise/cue settings and at least half of the oracle analytic gain on average.
- Stop condition: Stop as negative if the learned residual channel fails to beat equal-capacity baselines or if gains appear only in one seed or one hand-picked noise setting.

## Evidence references

- Artifact root: `<local-path>/projects/residual-doubt-channel-for-2-bit-agent-memory-45580855b8c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
