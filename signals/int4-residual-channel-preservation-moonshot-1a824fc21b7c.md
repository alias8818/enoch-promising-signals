# INT4 Residual Channel Preservation Moonshot

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int4-residual-channel-preservation-moonshot-1a824fc21b7c`
Run ID: `int4-residual-channel-preservation-moonshot-1a824fc21b7c-20260614T064201795476+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/86dcdadd867f

## What looked useful

Importance-selected fp16-equivalent preservation of 16/512 residual channels reduced relative MSE from 0.02955 to 0.01711 on average, a 42.05% error reduction across 5/5 seeds; random preservation only reduced error by 3.26%.

## Boundaries and scale limits

Proxy-only NumPy experiment: no real transformer activations, no language-model perplexity, no packed INT4 kernel, no latency or memory-bandwidth measurement, and only five seeds at dim=512/layers=8.

## Claim scope

In a synthetic frozen residual-block stack with injected high-impact residual channels, preserving the top 3.125% of channels selected by calibration importance reduced held-out downstream relative MSE versus all-channel groupwise INT4 and random/variance-only preservation controls.

## Why it stopped

Stopped at no-paper useful signal because the evidence is synthetic/proxy-only; it supports the mechanism but does not validate real model quality or systems overhead.

## Recommended next action

Run a bounded real-transformer follow-up on GPT-2-small-class activations comparing perplexity/loss for all-channel INT4, importance-preserved INT4, random preservation, and matched-overhead baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer residual channel preservation INT4 probe
- Success threshold: At least 20% reduction in INT4-induced perplexity/loss degradation versus all-channel INT4, beating random preservation and a matched-overhead control on at least 3 seeds or calibration splits.
- Stop condition: Stop if importance-selected preservation fails to beat random preservation or matched-overhead controls on real transformer held-out loss.

## Evidence references

- Artifact root: `<local-path>/projects/int4-residual-channel-preservation-moonshot-1a824fc21b7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
