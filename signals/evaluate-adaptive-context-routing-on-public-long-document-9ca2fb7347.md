# Evaluate Adaptive Context Routing on Public Long-Document QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evaluate-adaptive-context-routing-on-public-long-document-9ca2fb7347`
Run ID: `evaluate-adaptive-context-routing-on-public-long-document-9ca2fb7347-20260522T024514460744+0000`

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

- Parent run decision: Context-Length Adaptive Router for Long-Document QA: enoch://control-plane/projects/context-length-adaptive-router-for-long-document-qa-bbb7b2faf727/runs/context-length-adaptive-router-for-long-document-qa-bbb7b2faf727-20260522T010245145307+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d176ef2f214d

## What looked useful

Adaptive section diversification rescued a small number of Qasper evidence misses versus static top-k: +2.5, +3.3, and +5.0 evidence-any recall points at 4, 8, and 12 chunks respectively. The primary 8-chunk run was mixed because answer-string recall and evidence-fraction recall were slightly worse than static top-k.

## Boundaries and scale limits

Small validation subset; lexical routing only; no downstream LLM answer generation; no dense retrieval/reranking baseline; no full validation/test statistical closure; one public long-document QA dataset.

## Claim scope

On a 120-example AllenAI Qasper validation subset, a simple adaptive section-aware router modestly improved any-evidence context recall over lexical static top-k under equal 4, 8, and 12 paragraph-chunk budgets, but did not consistently improve all evidence or answer-containment metrics.

## Why it stopped

Tier 1 direct test found a useful but mixed small-sample mechanism signal; this is no-paper evidence rather than full validation.

## Recommended next action

Run a bounded deepen follow-up on the full Qasper validation split with end-to-end generated QA accuracy and stronger BM25/dense reranking controls; stop if adaptive routing fails to improve answer F1 or evidence recall by at least 3 points with confidence intervals excluding zero.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-Qasper Adaptive Routing With Generation and Strong Retrieval Controls
- Success threshold: At least +3 absolute points in generated answer F1 or accepted Qasper score and at least +3 points in evidence-any recall versus the strongest retrieval baseline, with bootstrap 95% confidence interval for the primary gain excluding zero.
- Stop condition: Stop if adaptive routing does not beat the strongest retrieval baseline on either generated answer quality or evidence recall, or if gains remain confined to tie-heavy small subsets.

## Evidence references

- Artifact root: `<local-path>/projects/evaluate-adaptive-context-routing-on-public-long-document-9ca2fb7347`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
