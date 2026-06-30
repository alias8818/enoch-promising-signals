# Quantized Tool Router for Safer Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-tool-router-for-safer-small-agents-e12bce903e45`
Run ID: `quantized-tool-router-for-safer-small-agents-e12bce903e45-20260522T012314896937+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/097ee83fc7b8

## What looked useful

Quantization was not the dominant failure mode in this bounded probe: int8 matched fp32 and int4 stayed close on clean/shifted suites with zero unsafe dangerous-tool leakage, while fp32/int8/int4/2-bit all accepted only about 6.9% of benign OOD security/admin prompts.

## Boundaries and scale limits

Synthetic template-derived prompts only; no real agent traces, no multi-turn state, no small-LM hidden-state router, no independently generated adversarial suite, and no specialized integer inference kernel.

## Claim scope

On a synthetic single-turn text-router benchmark, post-training quantization to int8 and int4 preserved the fp32 router's in-template unsafe refusal behavior, but the router family failed benign out-of-distribution security/admin usability.

## Why it stopped

No-paper useful signal: proxy evidence supports quantization stability on the toy router but early-falsifies the broader practical safety/usability claim under OOD benign security prompts.

## Recommended next action

Run a bounded hard-negative deepen test: add benign security/admin OOD coverage, evaluate int8/int4 on an independently generated prompt suite, and stop if benign OOD safe-accept remains below 90% at >=99% unsafe refusal and <=1% dangerous-tool leakage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-Negative OOD Calibration for Quantized Tool Routers
- Success threshold: int8 and int4 both achieve >=99% unsafe refusal, <=1% dangerous-tool leakage, and >=90% benign OOD safe-accept with <=2 percentage point degradation versus fp32.
- Stop condition: Stop as negative if benign OOD safe-accept is below 90% or dangerous-tool leakage exceeds 1% for either int8 or int4 across the five-seed aggregate.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-tool-router-for-safer-small-agents-e12bce903e45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
