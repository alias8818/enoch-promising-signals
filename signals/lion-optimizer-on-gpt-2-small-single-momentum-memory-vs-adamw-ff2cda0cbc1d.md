# Lion optimizer on GPT-2-small: single-momentum memory vs AdamW

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lion-optimizer-on-gpt-2-small-single-momentum-memory-vs-adamw-ff2cda0cbc1d`
Run ID: `lion-optimizer-on-gpt-2-small-single-momentum-memory-vs-adamw-ff2cda0cbc1d-20260610T130456514642+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/021ea2559543

## What looked useful

Lion optimizer state was 495,006,720 bytes versus AdamW's 990,014,032 bytes for a 123,751,680-parameter GPT-2-small shape, a 0.4999997 ratio. Peak CUDA allocated memory was about 1.93 GB for Lion versus 2.61 GB for AdamW in the bounded comparison.

## Boundaries and scale limits

Synthetic data only, 100 steps, batch size 2, sequence length 128, no real validation set, no LR schedule, no multi-seed robustness, no final perplexity or full pretraining run.

## Claim scope

On a GPT-2-small architecture shape trained for 100 synthetic causal-LM steps on GB10, Lion used one momentum buffer per parameter tensor and exactly half the optimizer-state bytes of AdamW, with finite improving losses at 1e-4 and 3e-4 learning rates.

## Why it stopped

Closed as no-paper useful signal: the memory mechanism is directly supported locally, but convergence evidence is synthetic and too shallow for publication-grade claims.

## Recommended next action

Run a bounded real-corpus GPT-2-small comparison with matched LR sweeps, warmup/decay, validation perplexity, and checkpointed memory telemetry before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small Lion vs AdamW memory and validation-perplexity check
- Success threshold: Lion retains at least 40% optimizer-state memory reduction and reaches validation perplexity within 2% of the best AdamW run at the same token budget.
- Stop condition: Stop if Lion is more than 5% worse in validation perplexity after LR tuning or if practical training stack memory telemetry no longer shows a material optimizer-state reduction.

## Evidence references

- Artifact root: `<local-path>/projects/lion-optimizer-on-gpt-2-small-single-momentum-memory-vs-adamw-ff2cda0cbc1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
