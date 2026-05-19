# Live Tool-Trace Evidence Ledger Hallucination Test

Status: `useful_signal`
Project ID: `live-tool-trace-evidence-ledger-hallucination-test-33c9e965a2`
Run ID: `live-tool-trace-evidence-ledger-hallucination-test-33c9e965a2-20260519T012605606478+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fce03dab0611

## What looked useful

Ledger prompting reduced any unsupported output from 91.67% to 33.33%, reduced mean unsupported hits from 6.4375 to 1.9375, and improved supported-fact recall from 82.08% to 93.75% across 48 paired cases.

## Boundaries and scale limits

One small instruction model, synthetic templated traces, deterministic decoding, exact-match automatic scoring, and no real deployed tool traces or human adjudication.

## Claim scope

In a 48-case synthetic paired eval on Qwen/Qwen2.5-1.5B-Instruct, an explicit evidence-ledger prompt reduced leakage of stale, failed, and untrusted tool-trace content while improving exact supported-fact recall.

## Why it stopped

Tier 1 controlled direct evidence supports the mechanism but remains synthetic and single-model, so it is no-paper useful evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen eval across at least three model families and 100+ semi-real tool traces with human adjudication before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Model Semi-Real Evidence Ledger Hallucination Eval
- Success threshold: Ledger condition achieves at least a 40 percentage point absolute reduction in unsupported-claim rate versus baseline, supported-fact recall is no more than 5 percentage points lower than baseline, and the effect holds for at least two of three model families.
- Stop condition: Stop if the ledger reduction is below 15 percentage points on the first 50 adjudicated cases or if recall drops by more than 10 percentage points, because that would make the mechanism too brittle for this line.

## Evidence references

- Artifact root: `<local-path>/projects/live-tool-trace-evidence-ledger-hallucination-test-33c9e965a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
