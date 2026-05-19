# Adaptive rank-anchor KV compression on GPT-2-small-class long-prefix decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `adaptive-rank-anchor-kv-compression-on-gpt-2-small-class-l-003174ac4a`
Run ID: `adaptive-rank-anchor-kv-compression-on-gpt-2-small-class-l-003174ac4a-20260517T225043406764+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Adaptive rank-anchor KV compression on GPT-2-small-class long-prefix decoding: internal_generated:adaptive-rank-anchor-kv-compression-on-gpt-2-small-class-l-003174ac4a

## What looked useful

Direct continuation-loss validation found that stride anchors were substantially better than adaptive anchors and rank-anchor at equal cache budget. At 25% cache, rank-anchor delta CE vs full was +0.9795 versus +0.3949 for stride; at 50% cache, rank-anchor was +0.6875 versus +0.1485 for stride. Rank-anchor beat stride on 0/64 samples at both budgets.

## Boundaries and scale limits

Tested Hugging Face gpt2, WikiText-2 test split, 64 fixed samples per full run, 768-token prefixes, 128-token continuations, bfloat16 on one GB10. Does not rule out learned selectors, different rank-summary math, larger models, longer-context architectures, or production low-rank attention kernels.

## Claim scope

For this deterministic GPT-2-small-class implementation on WikiText-2 long-prefix continuation, adaptive rank-anchor KV compression does not beat a simple memory-matched stride-anchor cache at 25% or 50% cache budget.

## Why it stopped

Bounded direct validation, not a proxy-only smoke test, falsified the practical success threshold: rank-anchor failed to outperform a simple memory-matched stride-anchor baseline at both tested cache budgets.

## Recommended next action

Stop this follow-up as a no-paper negative for the tested rank-anchor mechanism; future work should only restart with a materially different selector or rank-summary formulation and must first beat stride anchors on the same GPT-2/WikiText-2 harness.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-rank-anchor-kv-compression-on-gpt-2-small-class-l-003174ac4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
