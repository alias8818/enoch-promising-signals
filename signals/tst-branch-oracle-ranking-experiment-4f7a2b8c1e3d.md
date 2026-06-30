# TST Branch Oracle: Discriminative Proxy Ranking for Token-Superposition Variant Selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `tst-branch-oracle-ranking-experiment-4f7a2b8c1e3d`
Run ID: `tst-branch-oracle-ranking-experiment-4f7a2b8c1e3d-20260520T004645986645+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- TST Branch Oracle: Discriminative Proxy Ranking for Token-Superposition Variant Selection: https://arxiv.org/abs/2605.06546

## What looked useful

Cheap branch features contain an in-distribution ranking signal: learned mean regret was 0.341 vs 1.410 random and 0.767 for the best single heuristic. Robustness is not established: in the stress split learned regret was 1.400 vs 1.111 for proxy_alt_probability.

## Boundaries and scale limits

No real TST implementation, transformer hidden states, downstream task, or large-model training was tested. Evidence is limited to CPU-only NumPy synthetic episodes with 6 seeds, 6000 train episodes per seed, 2500 test episodes per seed, and 8 candidate branches per episode.

## Claim scope

In a synthetic TST branch-selection analogue with 512-token full-vocabulary weighted decode loss, a linear discriminative proxy improves in-distribution branch ranking over random and single-feature heuristics, but it does not remain best under a modest branch-distribution and hidden-decoder stress shift.

## Why it stopped

No-paper useful signal: matched synthetic evidence supports the mechanism, but the learned ranker loses to a cheap heuristic under stress, so this is not robust enough for a publication claim.

## Recommended next action

Run a bounded deepen experiment that trains the proxy on mixed alpha/mask and hidden-shift regimes, then require at least 15% lower regret than proxy_alt_probability on both matched and held-out stress splits before considering real-model integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixed-Regime Calibration for Robust TST Branch Proxy Ranking
- Success threshold: Learned proxy mean regret at least 15% lower than proxy_alt_probability on both matched and held-out stress splits, with no degradation below 0.75 pairwise accuracy on the matched split.
- Stop condition: Stop as no-paper negative if mixed-regime training still fails to beat proxy_alt_probability on stress or if gains only appear by weakening the stress shift.

## Evidence references

- Artifact root: `<local-path>/projects/tst-branch-oracle-ranking-experiment-4f7a2b8c1e3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
