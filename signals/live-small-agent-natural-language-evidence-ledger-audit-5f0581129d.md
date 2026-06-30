# Live Small-Agent Natural-Language Evidence Ledger Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-small-agent-natural-language-evidence-ledger-audit-5f0581129d`
Run ID: `live-small-agent-natural-language-evidence-ledger-audit-5f0581129d-20260605T122443881189+0000`

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

- Parent run decision: Live Tiny-Agent Evidence Ledger Audit Test: enoch://control-plane/projects/live-tiny-agent-evidence-ledger-audit-test-54264bcb5b/runs/live-tiny-agent-evidence-ledger-audit-test-54264bcb5b-20260605T073504909861+0000
- Parent run decision: Tiny Agent Evidence Ledger: enoch://control-plane/projects/tiny-agent-evidence-ledger-6535aa02b1ec/runs/tiny-agent-evidence-ledger-6535aa02b1ec-20260605T033943945711+0000

## What looked useful

Ledger prompting increased checkable audit surface relative to answer-only output, but exact supported quotes were only 16.7% overall / 20.8% on answerable examples, while answer accuracy dropped from 83.3% to 78.3% and unanswerable hallucination rose from 70.8% to 83.3%.

## Boundaries and scale limits

Single small instruction model, synthetic short documents, 360 total generations, no constrained decoding or external verifier, no human real-world corpus, no larger-model validation.

## Claim scope

On a 120-example fixed-seed synthetic document QA benchmark with Qwen2.5-0.5B-Instruct, natural-language evidence-ledger prompting exposed some source citations but did not reliably produce exact supported quotes and reduced answer accuracy versus an answer-only baseline.

## Why it stopped

Tier 2 fixed-seed medium validation produced mixed/negative evidence: natural-language ledger prompting alone harmed accuracy and did not produce reliable exact evidence support.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a constrained quote-extraction or verifier-repair ledger that must preserve answer-only accuracy while raising exact quote support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained Quote-Extraction Evidence Ledger for Small Agents
- Success threshold: On the same or larger fixed-seed benchmark, constrained/repaired ledger reaches at least 0.75 exact quote support on answerable examples, answer accuracy is within 0.02 absolute of answer-only, and unanswerable hallucination does not increase versus answer-only.
- Stop condition: Stop if exact quote support remains below 0.50 on answerable examples or answer accuracy drops by more than 0.05 absolute versus answer-only after prompt/schema and verifier calibration.

## Evidence references

- Artifact root: `<local-path>/projects/live-small-agent-natural-language-evidence-ledger-audit-5f0581129d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
