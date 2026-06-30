# GPT-2 residual-channel preservation against established INT4 PTQ baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `gpt-2-residual-channel-preservation-against-established-in-7723b903b4`
Run ID: `gpt-2-residual-channel-preservation-against-established-in-7723b903b4-20260607T042508319195+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: All-layer GPT-2 INT4 residual-channel preservation with perplexity validation: enoch://control-plane/projects/all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c/runs/all-layer-gpt-2-int4-residual-channel-preservation-with-pe-c1f61b833c-20260605T203225281143+0000
- Parent run decision: Seed-robust GPT-2 residual-channel INT4 preservation validation: enoch://control-plane/projects/seed-robust-gpt-2-residual-channel-int4-preservation-valid-b7df82d9c6/runs/seed-robust-gpt-2-residual-channel-int4-preservation-valid-b7df82d9c6-20260605T215358898456+0000

## What looked useful

Activation-selected residual-channel preservation recovered 30.05%, 40.58%, and 49.90% of RTN INT4 NLL degradation at 0.5%, 1%, and 2% preserved-channel budgets, respectively; random preservation recovered 0.84%-4.63% and weight-norm preservation recovered 6.35%-7.84%.

## Boundaries and scale limits

Single model family member (GPT-2 small), single dataset (WikiText-2), one fixed seed, fake quantization/dequantization modules, and RTN-only established PTQ baseline; no GPTQ/AWQ/SmoothQuant-class comparison and no packed INT4 throughput validation.

## Claim scope

For GPT-2 small on WikiText-2 with fake-quantized symmetric groupwise INT4 weight-only RTN, preserving 0.5%-2% of activation-selected residual/input channels in FP16 improves next-token NLL more than random or weight-norm channel preservation at the same preserve fraction.

## Why it stopped

No-paper useful signal: direct GPT-2 small evidence supports the mechanism against RTN and ablation controls, but the run does not include stronger established INT4 PTQ baselines or multi-dataset/multi-seed robustness.

## Recommended next action

Run one bounded deepen follow-up comparing activation-channel preservation against GPTQ/AWQ-class INT4 PTQ on GPT-2 small and medium with WikiText-2 plus one additional corpus and three seeds; stop paper escalation unless it remains better at matched effective bit budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2 activation-channel preservation against GPTQ/AWQ INT4 PTQ
- Success threshold: At matched effective bit budgets, activation-channel preservation must reduce NLL degradation versus the strongest GPTQ/AWQ-class baseline by at least 10% relative on both model sizes, or match the strongest baseline while using a simpler calibration path and showing stable selected-channel structure.
- Stop condition: Stop as negative if activation-channel preservation fails to beat random and weight-norm controls on GPT-2 small, or if it is worse than GPTQ/AWQ by more than 5% relative NLL-degradation on two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-residual-channel-preservation-against-established-in-7723b903b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
