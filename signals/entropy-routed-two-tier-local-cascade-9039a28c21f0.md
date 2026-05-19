# Entropy-Routed Two-Tier Local Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-routed-two-tier-local-cascade-9039a28c21f0`
Run ID: `entropy-routed-two-tier-local-cascade-9039a28c21f0-20260516T110319405213+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bf84e6e5d49a

## What looked useful

Entropy routing beat random routing at matched route fractions, but margin and max-probability uncertainty slightly outperformed entropy. The mechanism signal is uncertainty routing, not entropy as a uniquely superior router. Routing can hurt when Tier 2 is not stronger.

## Boundaries and scale limits

Evidence is limited to small sklearn datasets, a logistic-regression first tier, an ExtraTrees second tier, and a simple predict-time cost proxy. It does not validate LLM, transformer, GPU-serving, batching, or production-local cascade behavior.

## Claim scope

Small local sklearn classification proxy: an uncertainty-routed two-tier local cascade can recover part of a stronger local second tier's accuracy at lower second-tier call rates when the second tier is actually stronger.

## Why it stopped

No-paper closure: this is a proxy/local sklearn result with mixed entropy-specific evidence, not a publication-grade validation of the architecture.

## Recommended next action

Run a bounded direct-evidence follow-up on a real local neural inference task with validation-selected thresholds and measured serving latency, comparing entropy against margin, max-probability, random, always-tier1, and always-tier2 controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local neural validation of uncertainty-routed two-tier cascades
- Success threshold: At a fixed Tier 2 call rate of 20-35%, the best uncertainty router should recover at least 50% of the always-tier2 accuracy gain over Tier 1 while reducing measured Tier 2 calls by at least 65%; entropy should be considered supported only if it is within 0.2 percentage points of the best uncertainty control or better.
- Stop condition: Stop as negative if Tier 2 is not stronger on the selected task, if uncertainty routing fails to beat random by at least 0.5 accuracy points at matched call rate, or if entropy is consistently worse than simpler uncertainty controls by more than 0.5 accuracy points.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-routed-two-tier-local-cascade-9039a28c21f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
