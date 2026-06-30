# Cross-domain real-trace macro compression and prediction validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-domain-real-trace-macro-compression-and-prediction-v-c726989b93`
Run ID: `cross-domain-real-trace-macro-compression-and-prediction-v-c726989b93-20260613T200842322080+0000`

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

- Parent run decision: Real-trace validation of trace-derived semantic macro-operator compression: enoch://control-plane/projects/real-trace-validation-of-trace-derived-semantic-macro-oper-440ca04dac/runs/real-trace-validation-of-trace-derived-semantic-macro-oper-440ca04dac-20260613T195328359436+0000
- Parent run decision: Trace-derived semantic operator compression for repeated agent tasks: enoch://control-plane/projects/trace-derived-semantic-operator-compression-for-repeated-agent-tasks-1d842b83671a/runs/trace-derived-semantic-operator-compression-for-repeated-agent-tasks-1d842b83671a-20260613T183928762624+0000

## What looked useful

Real temporal macros are not random: target and cross-domain macros produce small top-1 accuracy gains in 21/33 evaluations and are much better than shuffled controls, while shuffled controls lose almost everywhere. However, the practical compression and calibrated prediction claims fail under the Tier 2 baseline: 0/33 zlib compression wins for target or cross macros, and mean NLL worsens.

## Boundaries and scale limits

Only 11 aggregate feature traces from three datacenter datasets were tested; tokenization used 8 quantile bins; prediction was next-bin classification rather than continuous forecasting; macro coding and macro-prefix voting were simple prototypes, not optimized entropy coders or learned sequence models.

## Claim scope

On sampled aggregate Alibaba 2018, Google 2019, and Azure v2 datacenter utilization traces at 300-second stride, quantile-token macro dictionaries mined from target or cross-domain training splits show non-random temporal motif transfer relative to shuffled controls, but do not beat zlib compression with dictionary overhead and do not improve calibrated next-token NLL over a target-domain trigram baseline.

## Why it stopped

Tier 2 medium validation produced useful mechanism evidence but failed the direct practical thresholds: no macro configuration beat zlib with dictionary overhead, and macro prediction worsened mean NLL despite small accuracy gains.

## Recommended next action

Stop paper escalation for this macro-compression claim; a bounded deepen follow-up should test whether adaptive entropy coding plus a calibrated macro-aware predictor can convert the observed non-random motif signal into NLL or compression gains on per-entity traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive entropy-coded macros and calibrated macro prediction on per-entity traces
- Success threshold: Across fixed seeds, macro coding must beat zlib/zstd on mean bits per token or improve mean NLL by at least 0.03 bits over the best target-domain baseline, with no degradation larger than 0.01 bits on more than one domain.
- Stop condition: Stop if overhead-counted macro compression has zero wins against zlib/zstd and calibrated NLL does not improve on at least two domains.

## Evidence references

- Artifact root: `<local-path>/projects/cross-domain-real-trace-macro-compression-and-prediction-v-c726989b93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
