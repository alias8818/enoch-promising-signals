# Co-training challenge tasks to probe honest contributions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `co-training-challenge-tasks-to-probe-honest-contributions-6999036d37ae`
Run ID: `co-training-challenge-tasks-to-probe-honest-contributions-6999036d37ae-20260611T054631972247+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/937adada3342

## What looked useful

IID/easy challenge scores correlated with candidate marginal validation utility at Spearman about 0.795 and detected harmful/valueless contributors with AUC 0.811-0.833. Dishonesty detection was strong across conditions with AUC 0.910-0.951. Under shifted challenges, utility detection AUC fell to 0.613, showing challenge distribution mismatch is a key failure mode.

## Boundaries and scale limits

Synthetic binary classification only; no real LLM co-training, no human contribution data, no adaptive challenge-aware agents, and no multi-round trust dynamics. Shifted challenge tasks degraded utility detection substantially.

## Claim scope

In a synthetic NumPy two-view co-training probe with 1,200 condition/behavior/seed rows, hidden challenge tasks estimated candidate honesty and marginal contribution well when challenge examples were IID or easier than the target distribution.

## Why it stopped

Closed as no-paper useful signal: the evidence is synthetic and mixed, with a clear distribution-shift limitation, so it is not publication-grade validation.

## Recommended next action

Run a bounded deepen test with small real text or small-language-model co-training tasks, including adaptive challenge-aware contributors and challenge sampling matched versus mismatched to the target distribution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive challenge probes for real small-model co-training contributions
- Success threshold: Matched challenge probes achieve AUC >= 0.80 for harmful/dishonest contributor detection and Spearman >= 0.60 with marginal downstream utility, while honest contributor false-positive rate remains <= 10%.
- Stop condition: Stop if matched challenge probes fall below AUC 0.70 or Spearman 0.40 after confidence intervals, or if adaptive contributors can pass challenges while causing negative downstream marginal utility.

## Evidence references

- Artifact root: `<local-path>/projects/co-training-challenge-tasks-to-probe-honest-contributions-6999036d37ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
