# Evidence Ledger Improves Small Agent Tool-Use Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-improves-small-agent-tool-use-reliability-22245f459335`
Run ID: `evidence-ledger-improves-small-agent-tool-use-reliability-22245f459335-20260604T102515626242+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05a6194bbd96

## What looked useful

Ledger prompting showed a small positive strict-success delta (+5.6 pp; ledger-only wins 8 vs baseline-only wins 6) but the paired effect was weak (exact McNemar p=0.7905) and premature finals increased from 0 to 6, suggesting ledger evidence may need controller enforcement rather than prompt text alone.

## Boundaries and scale limits

Single synthetic benchmark, one viable small model for the main run, greedy decoding, prompt-only ledger intervention, no public benchmark or production task validation; 0.5B and 1.5B smoke models were too weak for a meaningful comparison.

## Claim scope

On a deterministic 36-task synthetic customer-support tool-use benchmark with Qwen/Qwen2.5-3B-Instruct, a prompt-only evidence ledger improved strict success from 21/36 to 23/36 but introduced six premature final answers.

## Why it stopped

Prompt-only evidence ledger evidence is mixed and not paper-grade: small nonsignificant success improvement with a new premature-final failure mode on a synthetic local benchmark.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up testing ledger plus a final-answer completeness gate on the same benchmark before trying larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger With Final-Answer Completeness Gate
- Success threshold: Ledger-plus-gate improves strict success by at least 10 percentage points over baseline and has no more premature finals than baseline on the paired benchmark.
- Stop condition: Stop if ledger-plus-gate fails to beat prompt-only ledger or still produces more premature finals than baseline after the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-improves-small-agent-tool-use-reliability-22245f459335`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
