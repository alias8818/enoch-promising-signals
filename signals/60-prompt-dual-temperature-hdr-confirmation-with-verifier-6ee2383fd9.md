# 60-prompt dual-temperature HDR confirmation with verifier audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `60-prompt-dual-temperature-hdr-confirmation-with-verifier-6ee2383fd9`
Run ID: `60-prompt-dual-temperature-hdr-confirmation-with-verifier-6ee2383fd9-20260520T193552763184+0000`

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

- Parent run decision: Dual-Temperature HDR Inference Oracle — 10-prompt smoke: enoch://control-plane/projects/dual-temperature-hdr-inference-oracle-10-prompt-smoke/runs/dual-temperature-hdr-inference-oracle-10-prompt-smoke-20260520T191532331908+0000

## What looked useful

HDR flags had a 7.25x higher verifier-confirmed error rate than unflagged prompts, but recall was only 0.20 versus the 0.50 threshold, with 4 of 5 verifier-confirmed errors missed because both temperatures produced the same wrong answer.

## Boundaries and scale limits

Single local 7B quantized model, one low-temperature and one high-temperature sample per prompt, 60 closed prompts, deterministic verifier aliases; no larger models, production traffic, multi-sample voting, or semantic-equivalence verifier.

## Claim scope

On a local Qwen2.5-7B-Instruct Q4_K_M 60-prompt controlled benchmark, raw low/high-temperature answer disagreement concentrated verifier-confirmed errors among flagged prompts but fired too rarely to meet the preregistered recall threshold.

## Why it stopped

Controlled direct test failed the preregistered HDR confirmation threshold: error concentration was present, but recall was too low for a reliable verifier-audited confirmation.

## Recommended next action

Stop as no-paper useful signal; run a bounded deepen test with multiple high-temperature samples and semantic-equivalence-aware disagreement before considering any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-sample semantic HDR verifier audit
- Success threshold: HDR flagged prompts have at least 2x the verifier-confirmed error rate of unflagged prompts and HDR recall for verifier-confirmed any-error prompts is at least 0.50.
- Stop condition: Stop negative if recall remains below 0.50 or if semantic HDR removes the error concentration effect below 2x flagged/unflagged error rate.

## Evidence references

- Artifact root: `<local-path>/projects/60-prompt-dual-temperature-hdr-confirmation-with-verifier-6ee2383fd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
