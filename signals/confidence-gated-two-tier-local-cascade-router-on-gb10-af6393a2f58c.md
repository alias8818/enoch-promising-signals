# Confidence-Gated Two-Tier Local Cascade Router on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-two-tier-local-cascade-router-on-gb10-af6393a2f58c`
Run ID: `confidence-gated-two-tier-local-cascade-router-on-gb10-af6393a2f58c-20260629T133732437341+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/75d15a93c823

## What looked useful

The mechanism worked on a bounded classifier proxy: confidence gating routed only 9.86% of examples to the larger model, captured 22 large-model corrections, incurred 12 fallback regressions, preserved near-large accuracy, and improved actual routed throughput from 1120.67 to 1779.75 examples/s.

## Boundaries and scale limits

Single binary sentiment classification task, 872 validation examples, two fine-tuned encoder classifiers, one GB10 host, single-process batch inference. Not validated for open-ended generation, multi-domain prompts, 7B+ local LLMs, concurrent serving, tail latency, or human/judge-scored answer quality.

## Claim scope

On GLUE SST-2 validation with DistilBERT SST-2 as tier 1 and BERT-base SST-2 as tier 2 on NVIDIA GB10, a confidence threshold of 0.975 let the small model handle 90.14% of examples while the actual routed cascade reached 0.92202 accuracy, within 0.00229 absolute accuracy of large-only, and ran 1.59x faster than large-only inference.

## Why it stopped

No-paper closure: this is a reproducible proxy useful signal, not direct/full validation of local LLM cascade routing.

## Recommended next action

Run a bounded generative follow-up on GB10 with two local instruction models, judged answer quality, actual routed serving latency, and a large-only control; do not claim paper readiness from the classifier proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Generative GB10 cascade router with judged answer quality
- Success threshold: Cascade quality is within 1 percentage point or equivalent judge-score margin of large-only while routing at least 50% of prompts to the small model and improving p50 latency by at least 25% versus large-only.
- Stop condition: Stop if confidence is poorly calibrated enough that no threshold reaches the quality margin while routing at least 25% to the small model, or if routed serving latency is not faster than large-only after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-two-tier-local-cascade-router-on-gb10-af6393a2f58c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
