# INT2 weight quantization with learned micro-residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weight-quantization-with-learned-micro-residual-channels-f285c2011c5e`
Run ID: `int2-weight-quantization-with-learned-micro-residual-channels-f285c2011c5e-20260629T132715228290+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/507c09a4d15a

## What looked useful

The mechanism exists but is weak: rank 16 residual channels reduced mean output NMSE by about 7.2% at 2.66 bits/weight, while plain INT3 reached 0.045 mean output NMSE at 3.25 bits/weight. Even rank 64 used about 3.89 bits/weight and only reached 0.147 mean output NMSE, roughly 3.3x worse than INT3.

## Boundaries and scale limits

The run tested weight reconstruction and random Gaussian activation output error only. It did not test real hidden-state calibration, end-to-end perplexity, fused kernel latency, residual-factor quantization, or larger model families.

## Claim scope

On the 10 largest eligible GPT-2 weight matrices, groupwise INT2 plus SVD-learned low-rank micro-residual channels reduces reconstruction and random-activation layer-output error, but remains far worse than plain INT3 at comparable or lower bit budgets.

## Why it stopped

Early practical falsification by proxy: learned low-rank residual channels improve INT2 monotonically, but the improvement is too small and is dominated by plain INT3 under the tested bit accounting. This is not a full end-to-end validation.

## Recommended next action

Stop this SVD-low-rank residual formulation as no-paper evidence; a bounded follow-up should test activation-aware residual channels on real calibration activations against an INT3 perplexity and output-error baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT2 micro-residual channels versus INT3 on GPT-2 calibration data
- Success threshold: At no more than 3.25 effective bits/weight, activation-aware INT2 plus residual channels must reduce held-out layer-output NMSE by at least 50% versus INT2 and achieve perplexity within 10% relative of the INT3 baseline.
- Stop condition: Stop if activation-aware residual channels fail to beat SVD residual channels by at least 20% relative output NMSE or remain more than 25% relative perplexity worse than INT3 at the matched bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weight-quantization-with-learned-micro-residual-channels-f285c2011c5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
