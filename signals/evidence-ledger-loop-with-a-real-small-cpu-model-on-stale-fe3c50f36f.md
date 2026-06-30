# Evidence-ledger loop with a real small CPU model on stale-evidence QA

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-loop-with-a-real-small-cpu-model-on-stale-fe3c50f36f`
Run ID: `evidence-ledger-loop-with-a-real-small-cpu-model-on-stale-fe3c50f36f-20260605T020913909804+0000`

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

- Parent run decision: Evidence-ledger agent loop with small CPU models: enoch://control-plane/projects/evidence-ledger-agent-loop-with-small-cpu-models-39f5f714ac15/runs/evidence-ledger-agent-loop-with-small-cpu-models-39f5f714ac15-20260604T210909776239+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48518d91158f

## What looked useful

Prompt-level evidence-ledger injection failed the pre-set Tier 1 threshold on two real CPU models. Tiny GPT-2 ledger accuracy fell from 0.5833 to 0.5000 and stale-selection rose from 0.2500 to 0.2917. Flan-T5-small ledger accuracy fell from 0.5972 to 0.4167 and stale-selection rose from 0.4028 to 0.5833.

## Boundaries and scale limits

Synthetic fictional entities; 72 predictions per protocol per model for main runs; no retrieval, automatic ledger construction, natural stale-evidence corpus, free-generation parsing, larger model, or long-run robustness validation.

## Claim scope

Controlled 24-case stale/current evidence QA with candidate log-likelihood scoring on tiny GPT-2 int8 ONNX and Flan-T5-small CPU. The tested intervention was prompt-level explicit evidence ledger rows marking stale versus current evidence.

## Why it stopped

Tier 1 controlled direct test failed the success threshold on both tested CPU models; this is not a full validation of all evidence-ledger systems, but it is sufficient no-paper evidence against the scoped mechanism.

## Recommended next action

Stop this run as an early direct falsification of simple prompt-level ledger injection; the next bounded test should replace prompt-only ledger text with programmatic evidence filtering before model scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Programmatic evidence filtering before small-model stale QA scoring
- Success threshold: Filtered-ledger accuracy >= mixed-evidence baseline accuracy + 0.20 and stale-selection rate <= half the mixed-evidence baseline rate on both synthetic and natural/semi-natural subsets.
- Stop condition: Stop if filtered-ledger accuracy improves by <0.10 or stale-selection remains >75% of baseline on either subset.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-loop-with-a-real-small-cpu-model-on-stale-fe3c50f36f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
