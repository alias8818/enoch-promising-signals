# Evidence Ledger Agent for Falsifiable Reliability Logging

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-for-falsifiable-reliability-logging-10559149a965`
Run ID: `evidence-ledger-agent-for-falsifiable-reliability-logging-10559149a965-20260609T152602839538+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11df40c64e18

## What looked useful

Across 20,000 main-run tasks, the ledger detected 2,930/2,930 unsupported claims, 1,350/1,581 incorrect outputs as failed verified results, and all 1,038 tampered records through integrity failures. Untouched ledgers were structurally valid in 20/20 main trials and 5/5 no-fault control trials; no-fault controls produced zero unsupported or failed findings. Mean throughput was about 40.6k records/s with about 531 bytes/record.

## Boundaries and scale limits

The experiment used synthetic arithmetic tasks, deterministic oracle checks, and scripted tampering only. It did not test real LLM agents, noisy tool outputs, adversarial natural-language evidence, distributed logs, or long-running production traces.

## Claim scope

In a deterministic synthetic arithmetic harness, a minimal structured hash-chained evidence ledger made unsupported claims, failed verified results, and post-hoc tampering machine-detectable with low runtime cost.

## Why it stopped

The result is a synthetic/proxy validation of the logging mechanism, not a direct reliability result on real agents; it supports a bounded follow-up but is not publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should replay real or realistic agent traces with hidden fault labels and compare ledger-based auditing against free-form logs and existing observability traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger audit on realistic agent traces with hidden fault labels
- Success threshold: Ledger audit improves unsupported-claim and tamper-detection recall by at least 25 percentage points over baseline at precision >= 0.9, with storage overhead below 2 KB per step and no-fault false-positive rate below 2%.
- Stop condition: Stop if ledger recall is not materially better than baseline, if false positives exceed 10% on no-fault traces, or if per-step overhead exceeds 5 KB without a compensating audit-quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-for-falsifiable-reliability-logging-10559149a965`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
