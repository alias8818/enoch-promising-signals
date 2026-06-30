# Confidence-Entropy Cascade Router for Local Model Tiers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-entropy-cascade-router-for-local-model-tiers-d83780ee1609`
Run ID: `confidence-entropy-cascade-router-for-local-model-tiers-d83780ee1609-20260614T044806073516+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/353f49aa9e91

## What looked useful

The router found a low-escalation operating point, and oracle cascade accuracy around 0.89 shows complementary tier errors. The negative signal is that a larger local tier must first be verified as consistently better; otherwise confidence/entropy routing can appear to help only because the small tier is already stronger.

## Boundaries and scale limits

Not a 7B+ local LLM experiment, not a generative quality benchmark, not a full serving-system latency study, and only three seeds on one text classification dataset. The larger proxy tier was not consistently better than the smaller tier, so the central cascade prerequisite was not met robustly.

## Claim scope

Bounded AG News classifier-tier proxy on one GB10 host: confidence/entropy routing can route about 2.1% to 3.45% of samples and stay within 1 percentage point of large-only accuracy with about 1.15x estimated inference speedup, but only when interpreted against classifier tiers rather than generative LLM serving.

## Why it stopped

Closed as no-paper useful signal: this proxy found a router operating point but also falsified the stable large-tier-dominance prerequisite in 2 of 3 seeds, so it is not a full validation of local model-tier cascade routing.

## Recommended next action

Run a bounded deepen test with a demonstrably stronger upper tier, then compare confidence-only, entropy-only, combined, and random routing against quality and measured end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-Entropy Routing with a Verified Strong Upper Tier
- Success threshold: Combined confidence+entropy routing preserves at least 99% of upper-tier quality while reducing upper-tier invocations by at least 20% and beating confidence-only, entropy-only, and random routing at matched cost.
- Stop condition: Stop as negative if the upper tier is not consistently stronger than the lower tier, or if combined routing cannot beat random routing at matched escalation rate.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-entropy-cascade-router-for-local-model-tiers-d83780ee1609`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
