# 2-bit PTQ with residual channel preservation on gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-ptq-with-residual-channel-preservation-on-gb10-c7e82cd76bfb`
Run ID: `2-bit-ptq-with-residual-channel-preservation-on-gb10-c7e82cd76bfb-20260613T110544656301+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b2e9f148a6b9

## What looked useful

Plain 2-bit rowwise PTQ failed under synthetic outlier channels (rel MSE about 1.6-2.5). Preserving approximately the outlier-channel fraction with activation-aware scale exclusion reduced rel MSE to 0.014-0.053 at about 2.08-2.32 estimated bits per weight, while under-preserving remained poor.

## Boundaries and scale limits

No real pretrained LLM perplexity/task benchmark, no packed 2-bit kernel, no full serving benchmark, and only synthetic calibration activations across three seeds per setting.

## Claim scope

On synthetic 4096 x 4096 transformer-like linear projections with 0.5-2% high-variance input-channel outliers, activation-aware residual channel preservation on GB10 sharply improves 2-bit rowwise PTQ reconstruction when preserved channels are excluded from scale calibration and stored separately.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic GB10 mechanism probe rather than direct LLM accuracy or optimized packed-kernel validation.

## Recommended next action

Run a bounded GPT-2-small-class PTQ deepen test using real calibration activations and perplexity metrics, comparing plain 2-bit, residual-only, and scale-excluded residual-channel preservation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small PTQ residual-channel preservation with scale exclusion
- Success threshold: At <=2.5 effective bits per weight, scale-excluded activation-scored preservation should reduce perplexity degradation by at least 30% versus plain 2-bit PTQ and outperform random-channel preservation across most transformer blocks.
- Stop condition: Stop if real-model layer reconstruction does not improve over random preservation, or if perplexity remains unusable despite matching or exceeding the measured outlier-channel fraction.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-ptq-with-residual-channel-preservation-on-gb10-c7e82cd76bfb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
