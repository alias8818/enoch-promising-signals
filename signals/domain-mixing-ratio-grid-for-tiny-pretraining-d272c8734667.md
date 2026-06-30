# Domain-mixing ratio grid for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-mixing-ratio-grid-for-tiny-pretraining-d272c8734667`
Run ID: `domain-mixing-ratio-grid-for-tiny-pretraining-d272c8734667-20260628T201921302906+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3567575d683

## What looked useful

Pure single-domain training achieved low in-domain loss but failed the opposite domain. Coarse grid balanced losses were 3.984 at ratio_a=0, 2.353 at 0.25, 2.014 at 0.5, 2.038 at 0.75, and 3.901 at 1.0. A fresh-seed refinement gave balanced losses 1.986 at 0.5, 1.970 at 0.625, and 2.090 at 0.75. The exact optimum is not a strong claim, but the grid reliably detected the tradeoff and ruled out pure-domain mixtures for balanced evaluation.

## Boundaries and scale limits

Synthetic domains only; 3-layer 96-dimensional Transformer; 600 training steps per arm; no natural-language corpora, downstream tasks, tokenizer effects, long schedules, GPT-2-small-scale baseline, or multi-node/full-scale validation.

## Claim scope

In a bounded synthetic tiny causal-LM proxy with two domains sharing a 64-token vocabulary, a domain-mixing ratio grid exposed a clear specialization tradeoff and found a non-pure balanced-loss optimum near ratio_a=0.5 to 0.625 after 600 training steps.

## Why it stopped

This run produced proxy synthetic evidence only; it supports the mechanism but is not direct or broad enough for a paper-positive decision.

## Recommended next action

Run a bounded real-corpus follow-up with two public text domains, a parameter-matched tiny GPT baseline, per-domain held-out loss, and at least 3 seeds before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny LM domain-ratio grid
- Success threshold: A non-pure ratio improves balanced held-out loss by at least 0.03 nats over both pure-domain endpoints and is not worse than 50:50 by more than 0.01 nats across seed means; per-domain losses must show the expected tradeoff.
- Stop condition: Stop as a negative result if all mixed ratios are within seed noise of 50:50 or if the best mixed ratio fails to beat both pure endpoints on balanced held-out loss.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixing-ratio-grid-for-tiny-pretraining-d272c8734667`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
