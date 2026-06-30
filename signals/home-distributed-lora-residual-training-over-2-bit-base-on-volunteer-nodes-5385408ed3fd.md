# Home distributed LoRA + residual training over 2-bit base on volunteer nodes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-distributed-lora-residual-training-over-2-bit-base-on-volunteer-nodes-5385408ed3fd`
Run ID: `home-distributed-lora-residual-training-over-2-bit-base-on-volunteer-nodes-5385408ed3fd-20260621T080411923410+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/114ecde8251c

## What looked useful

Across three calibrated seeds, async LoRA rank-4 plus sparse residual improved test MSE by 8.10% over the frozen 2-bit base, compared with 2.29% for async rank-4 LoRA and 6.10% for async rank-11 parameter control. A staleness-32 stress seed preserved the residual advantage at 7.66% vs 5.93% for the rank-11 control.

## Boundaries and scale limits

No transformer, no real text objective, no real network transport, no client churn/failure, no privacy/security layer, no optimizer compression, no heterogeneous hardware, and residual storage is implemented as a dense masked tensor despite sparse effective degrees of freedom.

## Claim scope

Synthetic linear-teacher probe on GB10: a frozen per-row 2-bit base with LoRA rank-4 plus learned fixed-support sparse residual correction trains under centralized and simulated asynchronous non-IID volunteer updates, and beats LoRA-only and parameter-matched higher-rank LoRA controls on test MSE across three seeds.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and cannot validate home distributed LLM training at publication strength.

## Recommended next action

Run a bounded GPT-2-small-class transformer follow-up with real token loss, quantized linear layers, trainable LoRA plus sparse residual adapters, and a multi-process async client emulator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small async LoRA plus sparse residual over 2-bit quantized layers
- Success threshold: LoRA plus sparse residual improves validation loss by at least 3% relative to the frozen 2-bit base and beats a parameter-matched LoRA-only control by at least 1% under async staleness without divergence in 3 of 3 seeds.
- Stop condition: Stop if the residual branch fails to beat parameter-matched LoRA in two seeds, async staleness causes divergence that centralized training does not, or the bounded transformer run exceeds local GB10 memory/time calibration.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-lora-residual-training-over-2-bit-base-on-volunteer-nodes-5385408ed3fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
