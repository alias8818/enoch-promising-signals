# Natural-language local-agent evidence ledger consistency test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `natural-language-local-agent-evidence-ledger-consistency-t-329b27ea99`
Run ID: `natural-language-local-agent-evidence-ledger-consistency-t-329b27ea99-20260604T231314004092+0000`

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

- Parent run decision: Evidence Ledger for Small Local Agent Consistency: enoch://control-plane/projects/evidence-ledger-for-small-local-agent-consistency-5d82869aecc5/runs/evidence-ledger-for-small-local-agent-consistency-5d82869aecc5-20260604T194315274376+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae645af88749

## What looked useful

The local prose-only ledger agent produced parseable audits on 91.7% of trials but had mean score 0.25, retention failure rate 91.7%, conflict accuracy 0%, and counts accuracy 0%, failing the Tier 1 threshold.

## Boundaries and scale limits

Synthetic streams only; one 0.5B local instruct model; one prompt family; short four-update ledgers; no real evidence corpus, long-horizon memory, independent verifier model, or larger-model replication.

## Claim scope

Pure natural-language local-agent evidence ledger maintenance using Qwen/Qwen2.5-0.5B-Instruct on 12 controlled four-update contradictory evidence streams did not meet the predeclared consistency threshold.

## Why it stopped

Tier 1 direct small test failed the predeclared threshold; this is an early falsification of the pure natural-language ledger claim, not a full validation of alternative structured ledger designs.

## Recommended next action

Run a bounded deepen follow-up that adds an explicit structured evidence-ID index beside the prose ledger and tests whether the retention/conflict failure disappears.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured-ID scaffold for local-agent evidence ledger consistency
- Success threshold: Prose-plus-structured-ID-index reaches mean score >= 0.90, retention failure rate <= 0.05, and conflict accuracy >= 0.90, while outperforming the prose-only baseline by at least 0.30 mean score.
- Stop condition: Stop if the scaffolded ledger still has retention failure rate > 0.10 or conflict accuracy < 0.80 after 50 trials, because the local-agent consistency mechanism remains unreliable.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-local-agent-evidence-ledger-consistency-t-329b27ea99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
