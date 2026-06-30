# Dual-Temperature HDR Inference Oracle — 10-prompt smoke

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dual-temperature-hdr-inference-oracle-10-prompt-smoke`
Run ID: `dual-temperature-hdr-inference-oracle-10-prompt-smoke-20260520T191532331908+0000`

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

- Internal Enoch project: Dual-Temperature HDR Inference Oracle — 10-prompt smoke: internal_generated:dual-temperature-hdr-inference-oracle-10-prompt-smoke

## What looked useful

input_hdr_only beat best_of_5_mid=True; dual_hdr gain vs input_hdr_only=7.7%; unit fusion beat naive merge=False; verifier reliability=moderate (canary accuracy 1.000).

## Boundaries and scale limits

Smoke-only, 2 prompts per category, one local 7B quantized model, no human labels, no full 60-prompt run, and verifier validity tested only on canaries plus internal consistency.

## Claim scope

10-prompt local oracle smoke over five specified prompting/fusion arms using Qwen2.5-7B-Instruct Q4_K_M and a deterministic rule verifier.

## Why it stopped

Completed the requested 10-prompt smoke; evidence is useful but smoke-only and verifier-limited, so it is not paper-grade validation.

## Recommended next action

Run the full 60-prompt confirmation with the same trace schema and add a second verifier or small blinded manual audit before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 60-prompt dual-temperature HDR confirmation with verifier audit
- Success threshold: dual_hdr improves unique valid actionable units per 1k generated tokens by at least 15% over input_hdr_only and best_of_5_mid, with unsupported_claim_rate and constraint_violation_rate no worse than baseline.
- Stop condition: Stop if dual_hdr fails to beat input_hdr_only by 5% or if verifier audit agreement drops below 0.8.

## Evidence references

- Artifact root: `<local-path>/projects/dual-temperature-hdr-inference-oracle-10-prompt-smoke`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
