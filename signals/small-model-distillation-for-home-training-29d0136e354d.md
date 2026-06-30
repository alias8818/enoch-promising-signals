# Small Model Distillation for Home Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-model-distillation-for-home-training-29d0136e354d`
Run ID: `small-model-distillation-for-home-training-29d0136e354d-20260610T141729113733+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e459d80f48bf

## What looked useful

Distillation improved mean student NLL from 3.7737 to 3.7589 and reduced perplexity from 43.5390 to 42.9014 across three seeds, with all per-seed NLL deltas negative (-0.0139 to -0.0153).

## Boundaries and scale limits

Synthetic data only; one teacher size; one student architecture; 260 teacher steps and 260 student steps; no real corpus, tokenizer, pretrained teacher, GPT-2-class baseline, instruction data, quantization, or long-run validation.

## Claim scope

On a reproducible synthetic language generator, a 340k-parameter causal Transformer student trained with 50% hard-label loss plus 50% teacher-logit KL at temperature 2.0 achieved lower held-out next-token NLL than the same student trained with hard labels only across three paired seeds under a short GB10 home-training budget.

## Why it stopped

This run produced a useful synthetic mechanism signal, but it is not paper-ready because the evidence is proxy-only and small-scale rather than a real-corpus validation.

## Recommended next action

Run a bounded real-data deepen test using the same paired protocol on a small public corpus with a fixed teacher and report held-out NLL deltas over at least three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Home Distillation Check
- Success threshold: Distilled students must beat hard-label students in mean held-out NLL by at least 0.01 with all or nearly all paired seeds non-worse under equal token budget.
- Stop condition: Stop if the real-corpus mean NLL delta is within +/-0.005 or favors hard-label training in two or more paired seeds.

## Evidence references

- Artifact root: `<local-path>/projects/small-model-distillation-for-home-training-29d0136e354d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
