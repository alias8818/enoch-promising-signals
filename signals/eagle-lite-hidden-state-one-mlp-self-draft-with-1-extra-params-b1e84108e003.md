# EAGLE-lite: hidden-state one-MLP self-draft with <1% extra params

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `eagle-lite-hidden-state-one-mlp-self-draft-with-1-extra-params-b1e84108e003`
Run ID: `eagle-lite-hidden-state-one-mlp-self-draft-with-1-extra-params-b1e84108e003-20260619T135630235920+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/999e8a3b4411

## What looked useful

Across seeds 7 and 11, the MLP draft matched the base greedy token 15.17% on average versus 4.84% for identity and 11.45% for a trained linear residual control; top-5 agreement averaged 30.25% versus 10.91% identity and 22.98% linear. The extra parameter fraction was 0.9635%.

## Boundaries and scale limits

Only distilgpt2 was tested; training used two short 300-step KL runs with 115200 train token positions and 6144 eval token positions per seed. The run did not implement end-to-end speculative decoding, verifier acceptance, multi-token drafting, latency speedup, quality preservation, GPT-2-small-class baselines, or 7B+ behavior.

## Claim scope

On distilgpt2 with a compact local WikiText/fallback text probe, a frozen-base residual MLP with 789248 parameters, 0.9635% of base parameters, can learn a next-hidden-state draft distribution whose greedy token agrees with the base model's next-position greedy token more often than identity and trained linear residual controls.

## Why it stopped

The local proxy supports the mechanism but is not publication-grade evidence for EAGLE-lite because it measures next-position agreement rather than full speculative decoding acceptance or latency.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should implement a bounded autoregressive speculative-decoding accept/reject loop on GPT-2-small or distilgpt2 and compare wall-clock speed, acceptance, and quality against a parameter-matched draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded autoregressive acceptance test for <1% hidden-state MLP drafting
- Success threshold: At least 1.15x measured generated-token throughput over the no-draft baseline or a statistically consistent acceptance-rate improvement over linear control, with no degradation on the chosen quality proxy and auxiliary parameters below 1%.
- Stop condition: Stop as negative if MLP acceptance is within 2 percentage points of the trained linear residual control or if measured decoding latency is not improved after accounting for verifier overhead.

## Evidence references

- Artifact root: `<local-path>/projects/eagle-lite-hidden-state-one-mlp-self-draft-with-1-extra-params-b1e84108e003`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
