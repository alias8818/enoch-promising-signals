# moonshot: Dynamic Precision Scheduling Based on Layer Sensitivity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `moonshot-dynamic-precision-scheduling-based-on-layer-sensitivity-0e2ac030aaa7`
Run ID: `moonshot-dynamic-precision-scheduling-based-on-layer-sensitivity-0e2ac030aaa7-20260610T045951789187+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6d2ab989b5e9

## What looked useful

Layer sensitivity is predictive of precision allocation quality versus reverse and random controls, but low-bit aggressiveness dominates: sensitivity-guided 5/3 allocation modestly improved loss over uniform 4-bit, whereas 6/2 allocation severely degraded accuracy and loss.

## Boundaries and scale limits

Synthetic nonlinear classification, small MLPs, five seeds, fake post-training weight quantization only; no transformer, LLM, real dataset, activation quantization, training-time scheduling, mixed-precision kernels, or serving throughput validation.

## Claim scope

In a synthetic small-MLP post-training weight-quantization proxy, layer-sensitivity ranking is useful for equal-average-bit mixed precision only when the bit spread is constrained: 5/3-bit sensitivity scheduling beat uniform 4-bit on 5/5 seeds, while aggressive 6/2-bit scheduling lost to uniform 4-bit on 5/5 seeds.

## Why it stopped

Closed as no-paper useful signal because the evidence is proxy-only and mixed: sensitivity helps under constrained bit spreads but fails under aggressive low-bit scheduling against uniform precision.

## Recommended next action

Run a bounded GPT-2-small-class language-modeling follow-up with equal-budget 5/3, 6/2, uniform, random, and reverse schedules before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small equal-budget sensitivity precision scheduling
- Success threshold: Sensitivity-guided constrained mixed precision improves validation loss or perplexity over uniform 4-bit on at least 3/3 seeds or checkpoints and beats random/reverse controls, without a larger than 1% relative runtime or memory regression in the measured proxy.
- Stop condition: Stop if sensitivity scheduling fails to beat uniform 4-bit on two independent checkpoints/seeds, or if only aggressive bit spreads show gains while constrained spreads do not.

## Evidence references

- Artifact root: `<local-path>/projects/moonshot-dynamic-precision-scheduling-based-on-layer-sensitivity-0e2ac030aaa7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
