# Evidence Ledger Cuts Small Agent Hallucinations

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-cuts-small-agent-hallucinations-6481b23844aa`
Run ID: `evidence-ledger-cuts-small-agent-hallucinations-6481b23844aa-20260607T014638696692+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae5d5ea133b6

## What looked useful

Ledger formatting shifted behavior from abstention toward extraction: answerable accuracy rose from 13.0% to 82.5%, but unanswerable hallucination rate rose from 5.0% to 68.5%; total unsupported rate changed only from 46.0% to 43.0% with paired sign-test p=0.502.

## Boundaries and scale limits

Tested one 0.5B instruction model, synthetic evidence tables, greedy decoding, 400 paired examples across five seeds; no real agent traces, no larger models, no multi-hop retrieval, and no verifier/tool loop.

## Claim scope

On a synthetic single-hop evidence-dossier QA benchmark with Qwen/Qwen2.5-0.5B-Instruct, a prompt-only evidence-ledger contract did not reliably cut hallucinations; it improved answerable extraction but increased unanswerable hallucinations.

## Why it stopped

Bounded local evidence directly contradicts the prompt-only claim that an evidence ledger cuts hallucinations; the run is proxy/synthetic rather than full real-agent validation.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should add a deterministic citation verifier that rejects answers whose cited evidence line does not contain the queried entity, attribute, and answer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger With Deterministic Citation Verification
- Success threshold: Ledger-plus-verifier unanswerable hallucination rate must be at least 50% lower than ledger-only and no higher than baseline, while retaining at least 70% answerable accuracy across seeds.
- Stop condition: Stop if verifier-corrected answerable accuracy falls below 50% or if unanswerable hallucination remains above baseline on two consecutive seeds.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-cuts-small-agent-hallucinations-6481b23844aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
