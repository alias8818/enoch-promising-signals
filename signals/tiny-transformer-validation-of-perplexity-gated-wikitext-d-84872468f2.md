# Tiny Transformer validation of perplexity-gated WikiText data selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-transformer-validation-of-perplexity-gated-wikitext-d-84872468f2`
Run ID: `tiny-transformer-validation-of-perplexity-gated-wikitext-d-84872468f2-20260526T183411305629+0000`

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

- Parent run decision: Perplexity-Gated Local Pretraining Data Selection: enoch://control-plane/projects/perplexity-gated-local-pretraining-data-selection-36d999af057a/runs/perplexity-gated-local-pretraining-data-selection-36d999af057a-20260525T173101580183+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/788a76666a85

## What looked useful

Low-perplexity-only gating was 8.05% worse than random mean validation perplexity at equal token budget; high-perplexity-only selection was also 6.38% worse, suggesting scorer-perplexity extremes can reduce useful data coverage in this setup.

## Boundaries and scale limits

Small model, short training horizon, WikiText-2 only, 4725 scored non-empty train lines, two seeds, distilgpt2 scorer. This does not rule out band-pass filtering, high-perplexity-tail removal, longer training, larger models, or WikiText-103/full-corpus behavior.

## Claim scope

Tier 1 direct WikiText-2 small-model test: low distilgpt2-perplexity line selection for a 120k-token training subset did not improve held-out WikiText-2 validation perplexity for a 4-layer 128-hidden tiny Transformer trained for 450 steps.

## Why it stopped

The Tier 1 direct controlled test failed the success threshold: low-perplexity gating needed at least 3% lower validation perplexity than random but was 8.05% worse.

## Recommended next action

Stop this low-perplexity-only follow-up as an early direct falsification; if continuing locally, run a separate bounded deepen test for band-pass or high-tail-exclusion gating against random.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Band-pass WikiText perplexity gating vs random equal-token selection
- Success threshold: A gated arm reaches at least 3% lower mean held-out WikiText validation perplexity than random at equal token budget, without one seed regressing versus its random counterpart.
- Stop condition: Stop if both band-pass and high-tail-exclusion arms fail to beat random by 3% mean validation perplexity or if either is consistently worse across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-validation-of-perplexity-gated-wikitext-d-84872468f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
