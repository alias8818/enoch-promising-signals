# Small downstream validation of frequency-aware INT2 embedding residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-downstream-validation-of-frequency-aware-int2-embedd-079ee2f042`
Run ID: `small-downstream-validation-of-frequency-aware-int2-embedd-079ee2f042-20260610T171322255416+0000`

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

- Parent run decision: EmbRes-Q: INT2 embeddings with frequency-aware residual channel: enoch://control-plane/projects/embres-q-int2-embeddings-with-frequency-aware-residual-channel-86d2dfd1ae5f/runs/embres-q-int2-embeddings-with-frequency-aware-residual-channel-86d2dfd1ae5f-20260610T115130859962+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ff79ed4c30e8

## What looked useful

Frequency-selected 5% residual rows improved mean test accuracy from 0.8057 for no-residual INT2 to 0.8098 and mean test loss from 0.7000 to 0.6964 across five seeds; pooled random 5% residuals averaged 0.8055 accuracy and 0.7001 loss, rare 5% residuals averaged 0.8058 accuracy and 0.7002 loss. Frequency-weighted embedding MSE fell from 0.003199 to 0.000204. The 0.43 percentage point accuracy advantage over random controls missed the predeclared 0.5 point control threshold.

## Boundaries and scale limits

Small non-transformer classifier, 2334 train and 1555 test documents, 12k-token vocabulary, 64-dimensional embeddings, post-training embedding-only quantization, exact restored residual rows, no packed-runtime kernel or GPT-2-small-class validation.

## Claim scope

Five-seed Tier 1 direct downstream test on a four-class 20-Newsgroups embedding-bag classifier: row-wise affine INT2 quantization of learned token embeddings plus exact residual rows selected by token frequency improves mean loss and frequency-weighted embedding reconstruction versus equal-budget random and rare-row controls, but the held-out accuracy margin is small.

## Why it stopped

Tier 1 direct evidence is useful but mixed: mechanism support appears in loss and reconstruction, while the downstream accuracy edge over controls did not meet the predeclared threshold; this is not paper-positive.

## Recommended next action

Run a bounded deepen test on a harder direct setting where INT2 embeddings cause at least a 1 percentage point degradation, then require frequency-aware residuals to recover at least 50% of that degradation and beat random/rare controls by at least 0.5 percentage points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder direct validation of frequency-aware INT2 embedding residuals
- Success threshold: Frequency-aware residuals recover at least 50% of the no-residual INT2 downstream degradation and beat both random and rare equal-budget controls by at least 0.5 percentage points, or equivalent statistically paired perplexity/loss improvement, on the direct target metric.
- Stop condition: Stop as negative if no-residual INT2 degradation remains below 1 percentage point on the chosen direct tasks or if frequency-aware residuals fail to beat both equal-budget controls at two residual budgets.

## Evidence references

- Artifact root: `<local-path>/projects/small-downstream-validation-of-frequency-aware-int2-embedd-079ee2f042`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
