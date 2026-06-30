# Replay evidence ledger on labeled held-out agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `replay-evidence-ledger-on-labeled-held-out-agent-traces-89015bbc3e`
Run ID: `replay-evidence-ledger-on-labeled-held-out-agent-traces-89015bbc3e-20260604T140647164932+0000`

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

- Parent run decision: Replay Evidence Ledger on Natural-Language Agent Traces: enoch://control-plane/projects/replay-evidence-ledger-on-natural-language-agent-traces-0eed314780/runs/replay-evidence-ledger-on-natural-language-agent-traces-0eed314780-20260604T091917440256+0000
- Parent run decision: Tiny Agent Evidence Ledger for Tool Calls: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b/runs/tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b-20260604T065304736695+0000

## What looked useful

Ledger replay produced a reproducible controlled-benchmark signal: held-out F1 0.6599 +/- 0.0170 versus event-count baseline 0.6177 +/- 0.0197, with paired F1 delta +0.0422 and 95% CI +0.0154 to +0.0690. This is useful mechanism evidence but not paper-positive validation on real traces.

## Boundaries and scale limits

No real labeled agent trace corpus was available in the workspace; labels and traces were simulator-generated. Ablation support for specific ledger channels was weak to mixed, with paired confidence intervals crossing zero for temporal, negative-evidence, verification, and shuffled controls.

## Claim scope

On deterministic generated labeled agent traces with fixed train/validation/held-out splits, replay-derived evidence ledger features improved held-out success/failure prediction over majority, final-only, event-count, and text bag-of-words baselines by mean held-out F1 +0.042 versus the best non-ledger F1 baseline across five seeds.

## Why it stopped

Closed as no-paper useful signal because the Tier 2-style validation used generated labeled traces rather than real held-out agent traces, and ablations did not strongly isolate the full ledger mechanism.

## Recommended next action

Run the same replay-ledger, baseline, and ablation harness on a curated real held-out set of labeled Enoch/Codex agent traces before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence ledger on real labeled Enoch/Codex held-out traces
- Success threshold: Ledger replay beats the strongest non-ledger baseline by mean held-out F1 >= 0.03 across fixed seeds, ledger is better on at least 4/5 seeds, and at least one mechanism ablation reduces held-out F1 by >= 0.02 with a paired confidence interval excluding zero.
- Stop condition: Stop as unsupported if ledger replay fails to beat the best non-ledger baseline by mean held-out F1 >= 0.01, or if no ablation shows a reliable mechanism loss on the real labeled trace set.

## Evidence references

- Artifact root: `<local-path>/projects/replay-evidence-ledger-on-labeled-held-out-agent-traces-89015bbc3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
