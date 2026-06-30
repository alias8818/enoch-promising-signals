# Real Transcript Counter-Example Audit Evaluation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-transcript-counter-example-audit-evaluation-eba8ec54ba`
Run ID: `real-transcript-counter-example-audit-evaluation-eba8ec54ba-20260611T020327716215+0000`

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

- Parent run decision: Tool-Call Evidence Ledger with Counter-Example Audit: enoch://control-plane/projects/tool-call-evidence-ledger-with-counter-example-audit-38cec9ef93e6/runs/tool-call-evidence-ledger-with-counter-example-audit-38cec9ef93e6-20260611T010459638247+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd48ab272cb1

## What looked useful

The direct real-transcript test achieved 0.625 counter-example recall@5, 1.000 no-counterexample specificity, 0.750 overall accuracy, and 0.009375 random recall@5; it beat random retrieval but failed the pre-specified recall threshold.

## Boundaries and scale limits

Small hand-labeled benchmark: 12 cases, 5 public transcript pages, one lexical retrieval method, no semantic reranker or broad transcript-domain coverage.

## Claim scope

A simple lexical TF-IDF top-5 auditor did not meet the Tier 1 threshold for retrieving labeled counter-example spans from 12 claims over real Commission on Presidential Debates transcript pages.

## Why it stopped

Direct Tier 1 real-transcript evaluation failed the pre-specified success threshold; this is an early bounded falsification of the simple lexical-audit mechanism, not a full validation or disproof of semantic transcript auditing.

## Recommended next action

Run a bounded deepen follow-up on the same benchmark using a local semantic reranker or NLI model, requiring >=0.75 recall@5 and >=0.75 specificity before scaling to more transcripts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic Reranker for Real Transcript Counter-Example Audit
- Success threshold: >=0.75 counter-example recall@5 and >=0.75 no-counterexample specificity on the existing 12-case real-transcript benchmark, with no label changes.
- Stop condition: Stop if the semantic method misses two or more of the current three failed positive cases or reduces specificity below 0.75.

## Evidence references

- Artifact root: `<local-path>/projects/real-transcript-counter-example-audit-evaluation-eba8ec54ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
