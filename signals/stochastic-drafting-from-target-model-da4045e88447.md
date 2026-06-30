# Stochastic Drafting from Target Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `stochastic-drafting-from-target-model-da4045e88447`
Run ID: `stochastic-drafting-from-target-model-da4045e88447-20260602T125912752470+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7195814c2f2d

## What looked useful

Exact target drafts accept with probability 1.0 but measured target-draft-plus-verify slowdowns were 1.096x-1.603x on distilgpt2 and 1.097x-1.583x on gpt2 for gamma 16 to 2. Stochastic target-logit transformations reduced expected acceptance to roughly 0.58-0.72 while retaining target-forward draft cost.

## Boundaries and scale limits

This was a bounded local inference probe, not a production serving benchmark or 7B+ model validation. It directly tests compute accounting and GPU primitive latency for small GPT-2-class models; larger models could change constants but not the need for one target forward per autoregressive target-drafted token under this mechanism.

## Claim scope

For cached GPT-2-class models (distilgpt2 and gpt2) on GB10 CUDA fp16 inference, using the target model itself as the speculative draft source is slower than target-only decoding once the draft target forwards and verifier pass are both counted.

## Why it stopped

Proxy-scale but direct early falsification: the tested mechanism pays the same target autoregressive draft cost as baseline generation and adds verifier work, so it is not a viable speedup under the scoped interpretation.

## Recommended next action

Stop this direct target-self-drafting line unless a new mechanism can obtain future-token drafts without one full autoregressive target forward per draft token; then benchmark that mechanism end-to-end against target-only decoding.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/stochastic-drafting-from-target-model-da4045e88447`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
