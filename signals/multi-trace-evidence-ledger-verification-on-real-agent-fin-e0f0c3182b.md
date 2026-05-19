# Multi-Trace Evidence Ledger Verification on Real Agent Final Claims

Status: `useful_signal`
Project ID: `multi-trace-evidence-ledger-verification-on-real-agent-fin-e0f0c3182b`
Run ID: `multi-trace-evidence-ledger-verification-on-real-agent-fin-e0f0c3182b-20260517T172033395772+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Multi-Trace Evidence Ledger Verification on Real Agent Final Claims: internal_generated:multi-trace-evidence-ledger-verification-on-real-agent-fin-e0f0c3182b

## What looked useful

Multi-trace verification reduced false positives versus weak overlap and artifact-number baselines, averaging 0.758 accuracy and 0.799 F1 across three fixed seeds, but the report-only numeric ablation averaged slightly higher accuracy at 0.769 and F1 at 0.813.

## Boundaries and scale limits

Unsupported examples are deterministic numeric mutations rather than manually audited naturally occurring false claims; verification is numeric/lexical rather than semantic entailment; corpus is local Enoch/Codex worker artifacts, not an independent multi-agent benchmark.

## Claim scope

On 3 fixed seeds over 80 real prior Enoch projects per seed, a numeric/lexical multi-trace verifier for real agent final-report claims plus matched numeric mutations beats weak final-report-overlap and artifact-only baselines, but not a simpler report-only numeric ablation.

## Why it stopped

Medium fixed-seed validation produced a useful mechanism signal but failed the stronger ablation test: full multi-trace verification did not outperform the simpler report-only numeric verifier.

## Recommended next action

Do not write a paper from this run; run a bounded manually audited real-claim study with semantic entailment and span-level provenance before claiming multi-trace verification adds value over report-only checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Manually audited semantic multi-trace verification for real agent final claims
- Success threshold: Semantic multi-trace verifier improves accuracy by at least 10 percentage points over the best report-only baseline and keeps supported-claim recall at or above 0.90 on the audited corpus.
- Stop condition: Stop if manual audit finds fewer than 30 naturally unsupported real final claims or if report-only/semantic single-trace baselines match multi-trace accuracy within 3 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-evidence-ledger-verification-on-real-agent-fin-e0f0c3182b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
