# CPU Speculative Decoding Equivalence Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-speculative-decoding-equivalence-probe-d816bc58b4c4`
Run ID: `cpu-speculative-decoding-equivalence-probe-d816bc58b4c4-20260614T040712060973+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a505c71cd74a

## What looked useful

Exact enumeration found speculative-vs-baseline TV 1.3954359586246246e-16 and max absolute sequence-probability difference 1.3877787807814457e-17 over 1,024 sequences. A deliberately wrong rejection sampler had TV 0.11100555234159643, showing the probe catches a realistic implementation error.

## Boundaries and scale limits

Does not test real transformer logits, tokenizer behavior, KV-cache integration, batching, production inference numeric precision, or hardware-parallel target verification. CPU sampled throughput is from unoptimized Python and is not a serving benchmark.

## Claim scope

Exact finite-state toy LM distribution equivalence for a CPU speculative decoding sampler with vocab size 4, length 5, gamma 3, deterministic target/draft distributions, and residual rejection sampling.

## Why it stopped

Useful toy CPU equivalence signal was produced, but evidence is not publication-grade for real model serving.

## Recommended next action

Stop this run as bounded no-paper evidence; next direct test should replay saved logits from a small transformer through the same exact and empirical equivalence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Saved-logit speculative decoding equivalence check on a small transformer
- Success threshold: Speculative-vs-baseline exact/replay TV at numerical precision for the bounded replay space, empirical TV consistent with baseline Monte Carlo noise, and at least one broken control separated by 2x or more empirical TV.
- Stop condition: Stop if saved-logit replay shows reproducible speculative-vs-baseline drift above numerical tolerance after context/KV/tokenizer state bugs are ruled out.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-equivalence-probe-d816bc58b4c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
