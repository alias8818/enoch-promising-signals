# Evidence Ledger for Home Agents: Direct Artifact vs Transcript Recall

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-home-agents-direct-artifact-vs-transcript-recall-d37c15bb21c6`
Run ID: `evidence-ledger-for-home-agents-direct-artifact-vs-transcript-recall-d37c15bb21c6-20260620T025202074473+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/690b94d997f1

## What looked useful

Lossless transcript control was near-perfect (0.9997 transcript accuracy vs 1.0000 ledger), but under lossy transcripts the transcript baseline fell to 0.5907 while ledger lookup remained 1.0000 across 15,000 exact queries; sensitivity runs showed transcript accuracy dropping monotonically from 0.8213 to 0.4613 as omission rose from 10% to 50%.

## Boundaries and scale limits

Synthetic artifacts and deterministic retrieval only; no real home-agent transcripts, no private household data, no multimodal artifact ingestion, no LLM transcript-QA baseline, and no long-horizon deployment reliability test.

## Claim scope

In a deterministic synthetic home-agent artifact benchmark, direct structured ledger lookup preserved exact artifact facts under lossy transcript conditions where transcript-only recall degraded substantially.

## Why it stopped

The result supports the mechanism in a synthetic benchmark but is not a full validation of real home-agent behavior or publication-grade evidence.

## Recommended next action

Stop this worker run as no-paper useful signal; run a bounded direct-evidence follow-up on real or high-fidelity home-agent traces with a strong LLM transcript-QA baseline and the same exact artifact audit queries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic home-agent trace audit: direct evidence ledger versus LLM transcript QA
- Success threshold: At least 500 exact audit queries with ledger accuracy at least 10 percentage points higher than transcript-only LLM QA, no increase in unsupported answers, and preserved advantage on identifier/total/date subgroups.
- Stop condition: Stop if transcript-only LLM QA matches ledger within 3 percentage points overall and on exact identifier/amount/date subgroups, or if no suitable trace corpus with artifact-level ground truth can be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-home-agents-direct-artifact-vs-transcript-recall-d37c15bb21c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
