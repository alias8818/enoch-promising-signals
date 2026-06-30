# Larger bounded validation of mid-perplexity selection for GPT-2-class pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `larger-bounded-validation-of-mid-perplexity-selection-for-e6dcd7b980`
Run ID: `larger-bounded-validation-of-mid-perplexity-selection-for-e6dcd7b980-20260619T180324402397+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Perplexity-quantile data selection for tiny GPT-2-class pretraining: enoch://control-plane/projects/perplexity-quantile-data-selection-for-tiny-gpt-2-class-pretraining-d983c186ba9e/runs/perplexity-quantile-data-selection-for-tiny-gpt-2-class-pretraining-d983c186ba9e-20260619T174202720095+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3dedabb33ff9

## What looked useful

Across two controlled runs, mid-perplexity selection failed to beat random selection on final validation loss. In the larger confirmation, low-perplexity was best (2.5157 mean final loss), random was 2.5365, mid was 2.5404, and high was 2.6334 over five replicates.

## Boundaries and scale limits

Small byte-level Transformer, WikiText-2 only, short teacher scoring run, 3-replicate planned run plus 5-replicate persistence check; not GPT-2-small/BPE, not web-scale corpus, not downstream-transfer validation.

## Claim scope

Small direct WikiText-2 byte-level GPT-style causal Transformer test: teacher-NLL mid-perplexity chunk selection did not improve held-out LM loss versus equal-token random or low-perplexity controls.

## Why it stopped

Bounded direct early falsification: mid-perplexity selection did not outperform random or low-perplexity controls in the Tier 1 direct test; this is not full-scale validation.

## Recommended next action

Stop this no-paper branch unless a future GPT-2-small/BPE bounded confirmation can test the same low/mid/high/random controls with multiple seeds and a predeclared practical margin.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/larger-bounded-validation-of-mid-perplexity-selection-for-e6dcd7b980`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
