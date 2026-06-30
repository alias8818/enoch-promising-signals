# Sparse-Head Self-Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sparse-head-self-drafting-d282348a8b8b`
Run ID: `sparse-head-self-drafting-d282348a8b8b-20260529T085210995518+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c0c56bfae25

## What looked useful

On GPT-2-small/WikiText-2, 8 of 12 heads per layer reached only 45.5% dense top-1 agreement and 0.531 distribution overlap with +0.976 NLL/token; lower head fractions were much worse. This early-falsifies the simple static sparse-head self-drafting variant.

## Boundaries and scale limits

Tested GPT-2-small only, 65,536 WikiText-2 validation target tokens, seq_len 64, static top-k heads per layer. Did not test learned masks, sparse kernels, generated multi-token speculative decoding, larger models, or datacenter-scale validation.

## Claim scope

Static per-layer sparse attention-head masks selected by a cheap attention-mass heuristic do not preserve GPT-2-small next-token distributions well enough to serve as a practical self-drafting mechanism on a bounded WikiText-2 validation sample.

## Why it stopped

Proxy/early falsification: the direct distribution-preservation test failed for static sparse-head masks on GPT-2-small, but full speculative decoding kernels and learned masks were not validated.

## Recommended next action

Stop this static-mask line; a bounded follow-up should test learned or searched sparse-head policies before any larger-scale self-drafting work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Sparse-Head Policies for GPT-2 Self-Drafting
- Success threshold: At <= 2/3 average active heads, achieve mean distribution overlap >= 0.75, dense top-1 agreement >= 0.65, and NLL delta <= 0.35 on held-out WikiText-2.
- Stop condition: Stop if learned/searched policies remain below 0.65 overlap or above +0.7 NLL/token at <= 2/3 active heads after a bounded GPT-2-small search.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-head-self-drafting-d282348a8b8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
