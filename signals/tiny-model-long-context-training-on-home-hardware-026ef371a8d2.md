# Tiny Model Long-Context Training on Home Hardware

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-model-long-context-training-on-home-hardware-026ef371a8d2`
Run ID: `tiny-model-long-context-training-on-home-hardware-026ef371a8d2-20260610T023741818770+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/767dbb40cbe1

## What looked useful

8k dense-attention toy training was mechanically viable on modest CPU hardware: fixed-batch loss fell by 0.254 over 20 steps at 3.08 s/step and about 1.0 GiB RSS. Runtime scaled steeply by 32k, reaching about 50.3 s for one step.

## Boundaries and scale limits

Batch size 1, 2-layer 128-wide toy model, synthetic data only, CPU-only, short runs. 32k was a one-step boundary probe taking about 50 seconds/step; no GPT-2-small-scale, GPU, real dataset, validation benchmark, or efficient-attention baseline was run.

## Claim scope

On a CPU-only home-hardware-class worker, a 2-layer 128-wide dense-attention causal transformer can execute real backward/AdamW training steps up to 32k context and can measurably overfit a fixed synthetic 8k batch in 20 steps; this does not establish real-corpus long-context quality.

## Why it stopped

No-paper useful signal: this was a bounded CPU mechanics and short optimization probe, not a full validation of long-context training quality.

## Recommended next action

Run a bounded deepen follow-up comparing this dense baseline with one efficient long-context variant on a real or accepted synthetic long-context task at 8k-16k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dense versus efficient tiny long-context training at 8k-16k
- Success threshold: Efficient variant reaches equal or better validation metric than dense baseline within the same step budget while reducing mean step time or peak RSS by at least 25% at 16k context.
- Stop condition: Stop if the efficient variant cannot run correctly, fails to match dense validation metric, or saves less than 10% wall-clock/RSS in a controlled 16k comparison.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-model-long-context-training-on-home-hardware-026ef371a8d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
