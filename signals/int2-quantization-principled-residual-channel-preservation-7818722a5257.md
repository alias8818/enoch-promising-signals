# INT2 Quantization: Principled Residual Channel Preservation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-quantization-principled-residual-channel-preservation-7818722a5257`
Run ID: `int2-quantization-principled-residual-channel-preservation-7818722a5257-20260613T035435111547+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3aa1f9434937

## What looked useful

Full INT2 collapsed teacher agreement to 0.1557 mean, while preserving 6.25% of residual output channels by targeted scores restored teacher agreement to 0.9907; random 6.25% preservation stayed collapsed at 0.1634. The proposed score tied activation-energy and weight-error controls at 6.25% and was not robust at 3.125%.

## Boundaries and scale limits

Eight-seed synthetic NumPy experiment only; no pretrained transformer, real calibration corpus, perplexity/task benchmark, INT2 kernel, throughput, or full-model layer interaction was tested.

## Claim scope

Synthetic residual MLP evidence shows that targeted preservation of a small fraction of residual output channels can prevent severe degradation from per-row affine INT2 quantization; it does not show that the proposed error-times-sensitivity ranking is superior to simpler targeted rankings.

## Why it stopped

Proxy synthetic evidence supports targeted residual-channel preservation but does not validate the principled ranking or an LLM-scale INT2 claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should apply the same channel-ranking rules to one small pretrained transformer layer or GPT-2-small-class calibration/perplexity slice before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained transformer residual-channel INT2 preservation slice
- Success threshold: At a 5-10% preserved-channel budget, a targeted preservation rule must reduce held-out perplexity or next-token loss degradation by at least 50% versus full INT2 and beat random preservation across at least three seeds or calibration slices.
- Stop condition: Stop if targeted preservation fails to beat random preservation or if all targeted rankings are indistinguishable from full INT2 on held-out perplexity/loss.

## Evidence references

- Artifact root: `<local-path>/projects/int2-quantization-principled-residual-channel-preservation-7818722a5257`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
