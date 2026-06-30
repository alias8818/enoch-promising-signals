# Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spec-decoding-oracle-trace-ranker-20250519`
Run ID: `spec-decoding-oracle-trace-ranker-20250519-20260520T010147036783+0000`

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

- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

A simple cost_adjusted_survival ranker recovered 3.4078 selected expected utility versus 3.4388 for the expected oracle, with 0.784 top-1 expected-oracle hit rate, 0.978 top-3 hit rate, and 0.919 expected Spearman across four synthetic scenarios. The learned ridge trace ranker was weaker at 3.3868 selected expected utility and 0.739 top-1 hit rate.

## Boundaries and scale limits

No real DFlash model, hidden-state trace, tokenizer, GPU kernel, batching, quality-preservation, or wall-clock verifier throughput was tested. Results are proxy evidence only and should not be generalized to production speculative decoding without direct traces.

## Claim scope

Synthetic DFlash-like branch-ranking harness with 12 fixed branch proposals, block length 16, four trace-noise scenarios, and 80,000 contexts per scenario. Trace-derived cost-adjusted prefix survival ranked expected branch utility close to the expected-utility oracle, but learned trace ranking did not beat the simple heuristic.

## Why it stopped

Synthetic proxy evidence supports a practical baseline mechanism but not a direct or novel paper claim; real DFlash trace and throughput evidence is still required.

## Recommended next action

Stop this run as no-paper useful signal; next run should collect real DFlash branch traces and test whether any learned ranker beats cost-adjusted survival on accepted tokens per verifier step.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real DFlash Trace Ranking Against Cost-Adjusted Survival
- Success threshold: Learned trace ranker improves selected accepted-token utility or wall-clock tokens/sec by at least 2% over cost-adjusted survival on held-out real traces, with no exactness regressions.
- Stop condition: Stop if cost-adjusted survival is within 2% of the learned ranker on held-out real traces or if trace instrumentation cannot produce branch-comparable verifier outcomes.

## Evidence references

- Artifact root: `<local-path>/projects/spec-decoding-oracle-trace-ranker-20250519`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
