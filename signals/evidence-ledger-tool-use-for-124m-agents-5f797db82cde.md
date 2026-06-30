# Evidence-ledger tool-use for 124M agents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-tool-use-for-124m-agents-5f797db82cde`
Run ID: `evidence-ledger-tool-use-for-124m-agents-5f797db82cde-20260607T131333300711+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a5e63a14f587

## What looked useful

Across 1024 non-smoke examples and three seeds, plain transcript accuracy was 0.3672 while evidence-ledger accuracy was 0.3389, a -0.0283 ledger-minus-plain delta. The ledger was behind on every seed and had worse correct-vs-distractor margins.

## Boundaries and scale limits

Synthetic tasks only; no autonomous tool calling, no fine-tuning, no real retrieval traces, no free-form generation grading, and no larger or instruction-tuned model validation.

## Claim scope

For GPT-2 small-class 124M conditional likelihood ranking on synthetic tool-observation tasks, an explicit evidence-ledger prompt format did not improve verified answer selection over a plain tool transcript.

## Why it stopped

Proxy experiment directly tested prompt-format answer selection for a 124M pretrained model and found no ledger benefit; full claims would require trained agents or real tool traces.

## Recommended next action

Stop this prompt-only path as a paper candidate; the bounded result is an early proxy falsification, not a full validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a 124M-class control to consume evidence ledgers
- Success threshold: Ledger-trained model improves grounded answer accuracy by at least 5 absolute percentage points over transcript-trained control on held-out traces without increasing unsupported-claim rate.
- Stop condition: Stop if the ledger-trained model fails to beat the transcript-trained control by 2 absolute percentage points after matched training compute and schema/order ablations.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-tool-use-for-124m-agents-5f797db82cde`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
