# Quantized residual memory for safer small home agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-residual-memory-for-safer-small-home-agents-b7558d52af4d`
Run ID: `quantized-residual-memory-for-safer-small-home-agents-b7558d52af4d-20260525T070120899490+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/278e45695bb5

## What looked useful

Across 6 seeds with 800 train and 800 test episodes per seed, 4-bit quantized residual memory reduced unsafe allows from 0.4560 to 0.0485 relative to no memory, matched float residual accuracy within 0.0015 absolute, used 23.5 bytes per train episode versus 248.0 for float residual memory, and retained 0 exact sensitive tokens versus 6 for raw text replay.

## Boundaries and scale limits

No real LLM, real smart-home API, real user trace, robot actuation, optimized memory index, or adversarial extraction evaluation was run. Evidence is local synthetic proxy evidence only.

## Claim scope

In a synthetic household-control benchmark with generated user/device/context rules and a hand-coded weak base policy, 3-4 bit quantized residual memory preserved nearly all full-precision residual safety adaptation while using about an order of magnitude less storage and retaining no exact synthetic sensitive text.

## Why it stopped

Closed as no-paper useful synthetic signal: the result supports the mechanism locally but is not direct or broad enough for publication-grade validation.

## Recommended next action

Run a direct small-agent follow-up with natural-language household traces, a compact model or agent harness, optimized quantized residual lookup, and adversarial memory extraction tests before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-agent quantized residual memory on natural-language household safety traces
- Success threshold: 3-4 bit quantized residual memory must cut unsafe allows by at least 50% versus no memory, stay within 2 absolute accuracy points of full-precision residual memory, use at least 80% less storage than float residual replay, and leak fewer exact sensitive strings than raw replay.
- Stop condition: Stop if quantized residual memory fails to beat no memory on unsafe action rate, if 3-4 bit quantization loses more than 5 absolute accuracy points versus full-precision residual memory, or if adversarial extraction recovers sensitive strings at a rate comparable to raw replay.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-residual-memory-for-safer-small-home-agents-b7558d52af4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
