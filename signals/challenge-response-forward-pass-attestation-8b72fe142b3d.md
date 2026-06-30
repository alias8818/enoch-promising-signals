# Challenge-Response Forward-Pass Attestation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `challenge-response-forward-pass-attestation-8b72fe142b3d`
Run ID: `challenge-response-forward-pass-attestation-8b72fe142b3d-20260520T055710672234+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/080b78960275

## What looked useful

Strict challenge-response checks can reject cheap non-relay surrogates in the toy setting, but the tolerance sweep shows the margin is fragile: a ridge surrogate begins passing full sessions when output tolerance is made very loose.

## Boundaries and scale limits

Synthetic CPU-only simulation; no real transformer, production serving stack, adaptive extraction attack, live relay attacker, public-weight attacker, hardware provenance check, or cryptographic execution proof was tested.

## Claim scope

In a synthetic random ReLU MLP setting, fresh nonce-derived input challenges with strict output tolerance distinguished honest noisy forward-pass responses from constant, stale replay, nearest-neighbor, and ridge linear surrogate responders across 512 sessions of 8 challenges each.

## Why it stopped

No-paper closure: the evidence is synthetic and mechanism-scoped; it is useful for follow-up design but not direct publication-grade forward-pass attestation evidence.

## Recommended next action

Run a bounded deepen test on a small real transformer with quantized serving outputs and adaptive distillation attackers before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Challenge-Response Attestation Under Quantization and Distillation
- Success threshold: Honest pass rate at least 99% and best non-relay adaptive surrogate full-session false-accept rate below 0.1% for a predeclared realistic tolerance and challenge count.
- Stop condition: Stop if realistic serving tolerance causes honest failures above 1% or if an adaptive surrogate exceeds 0.1% full-session false accepts without requiring relay or target weights.

## Evidence references

- Artifact root: `<local-path>/projects/challenge-response-forward-pass-attestation-8b72fe142b3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
