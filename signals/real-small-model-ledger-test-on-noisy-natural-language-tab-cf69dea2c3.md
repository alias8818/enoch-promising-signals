# Real small-model ledger test on noisy natural-language tabular QA

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-small-model-ledger-test-on-noisy-natural-language-tab-cf69dea2c3`
Run ID: `real-small-model-ledger-test-on-noisy-natural-language-tab-cf69dea2c3-20260531T131803768335+0000`

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

- Parent run decision: Falsifiable claim-verification ledger for small reasoning agents: enoch://control-plane/projects/falsifiable-claim-verification-ledger-for-small-reasoning-agents-5d70b2f06bc3/runs/falsifiable-claim-verification-ledger-for-small-reasoning-agents-5d70b2f06bc3-20260530T085753691945+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8408ff0055b8

## What looked useful

The ledger prompt scored 23.6% exact match versus 34.0% for raw noisy prose, delta -10.4 percentage points. Raw-only wins outnumbered ledger-only wins 64 to 34; the paired sign-test p-value was 0.00319. The result directly falsifies the predefined Tier 1 threshold for this ledger format.

## Boundaries and scale limits

288 evaluated cases across three seeds, one small instruction-tuned model, one ledger encoding, greedy decoding, synthetic generated tables rather than a public real-world tabular QA dataset.

## Claim scope

For google/flan-t5-small on a controlled generated noisy natural-language tabular QA benchmark with five-column sales rows, the tested pipe-delimited deterministic ledger prompt did not improve exact-answer accuracy over raw noisy prose prompts.

## Why it stopped

Direct controlled small-model test failed the predefined success threshold across smoke plus three 96-case seeds; this is an early direct falsification for the tested format, not a full validation of all ledger methods.

## Recommended next action

Stop this ledger-format claim; a bounded deepen follow-up should test alternative structured encodings with row IDs or JSON/XML fields before considering any larger real-dataset validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Encoding ablation for small-model ledger tabular QA
- Success threshold: An alternative ledger encoding beats raw exact match by at least 15 percentage points and reaches at least 50% aggregate exact match, with no numeric lookup subtask below raw by more than 5 points.
- Stop condition: Stop if no alternative encoding beats raw by at least 5 percentage points after 288 paired cases, or if numeric lookup remains below raw for all structured encodings.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-model-ledger-test-on-noisy-natural-language-tab-cf69dea2c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
