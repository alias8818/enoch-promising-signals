# Mixed-Regime Calibration for Robust TST Branch Proxy Ranking

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `mixed-regime-calibration-for-robust-tst-branch-proxy-ranki-68ffe6cb36`
Run ID: `mixed-regime-calibration-for-robust-tst-branch-proxy-ranki-68ffe6cb36-20260520T005644818773+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: TST Branch Oracle: Discriminative Proxy Ranking for Token-Superposition Variant Selection: enoch://control-plane/projects/tst-branch-oracle-ranking-experiment-4f7a2b8c1e3d/runs/tst-branch-oracle-ranking-experiment-4f7a2b8c1e3d-20260520T004645986645+0000
- TST Branch Oracle: Discriminative Proxy Ranking for Token-Superposition Variant Selection: https://arxiv.org/abs/2605.06546

## What looked useful

Mixed-regime linear calibration improved top-1 branch selection by 13.28 percentage points and reduced mean regret by 54.53% versus raw proxy ranking across 80 seed/mixture pairs; paired top-1 improvement 95% CI was [0.1224, 0.1431].

## Boundaries and scale limits

No real LLM, real verifier, real TST trace, or unobserved-regime inference was tested; branch rewards and proxy scores were generated from a hand-specified simulator.

## Claim scope

Controlled Tier 1 synthetic TST-like branch ranking with observed regimes, 8 branches per state, 20 seeds, and four held-out regime mixtures.

## Why it stopped

Tier 1 controlled evidence supports the mechanism but remains synthetic/no-paper; this is not full validation or paper-positive evidence.

## Recommended next action

Run the same calibration comparison on real small-model TST traces with branch outcomes from task correctness or verifier reward before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Mixed-Regime Calibration for TST Branch Ranking
- Success threshold: Mixed-regime calibration improves top-1 branch outcome by >=5 percentage points and reduces regret/error by >=10% versus raw proxy ranking on held-out real traces.
- Stop condition: Stop if real-trace mixed-regime calibration fails to beat raw proxy ranking by at least 2 percentage points top-1 or shows no regret/error reduction across paired held-out tasks.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-regime-calibration-for-robust-tst-branch-proxy-ranki-68ffe6cb36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
