# MedianK: K-of-N Gradient Median Filtering for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mediank-k-of-n-gradient-median-filtering-for-volunteer-training-70330a9ef032`
Run ID: `mediank-k-of-n-gradient-median-filtering-for-volunteer-training-70330a9ef032-20260614T112328554665+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dfd71420de4

## What looked useful

MedianK selected clean workers in 100% of retained slots in the main outlier-like attack sweep and was top in 9/12 groups, with mean accuracy delta +0.0096 versus the best non-MedianK baseline. In low-scale sign-flip stress cases it selected fewer clean workers as corruption rose and lost by up to 0.0243 accuracy, defining a practical failure boundary.

## Boundaries and scale limits

No real volunteer workers, deep neural networks, non-IID client shards, adaptive attackers, large optimizers, or full-scale distributed training were tested. The stress sweep shows low-scale sign-flip gradients can be insufficiently separable, causing MedianK to select malicious workers and underperform simpler baselines.

## Claim scope

Synthetic logistic-regression volunteer-gradient simulation with N=9 workers, K=5 MedianK filtering, up to 44% malicious workers, and mean/coordinate-median/trimmed-mean baselines. MedianK helps when malicious gradients are outliers and can preserve near-clean validation accuracy in those proxy settings.

## Why it stopped

Synthetic proxy evidence is mixed: it supports the outlier-filtering mechanism but also shows a stress-case vulnerability, so this is not full validation or paper-ready evidence.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should test MedianK on a small neural benchmark with non-IID client shards and adaptive/non-adaptive attacks before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: MedianK on non-IID neural client shards with adaptive and non-adaptive attacks
- Success threshold: MedianK should beat the best non-MedianK baseline by at least 1 percentage point accuracy or 10% relative loss in at least two non-adaptive attack settings without regressing clean training by more than 0.5 percentage points, and the diagnostic should show mostly clean worker selection.
- Stop condition: Stop if MedianK fails to beat robust baselines on non-adaptive outlier attacks, regresses clean/non-IID training materially, or adaptive low-magnitude attacks consistently collapse selected-clean fraction below 70% without a mitigation.

## Evidence references

- Artifact root: `<local-path>/projects/mediank-k-of-n-gradient-median-filtering-for-volunteer-training-70330a9ef032`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
