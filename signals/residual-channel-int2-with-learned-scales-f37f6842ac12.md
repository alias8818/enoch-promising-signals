# Residual-Channel INT2 with Learned Scales

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-int2-with-learned-scales-f37f6842ac12`
Run ID: `residual-channel-int2-with-learned-scales-f37f6842ac12-20260528T144353789430+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9eafc81d5e7c

## What looked useful

Learned scales reduced tiny-corpus loss from 8.5104 to 7.2080 versus weight-derived INT2 scales at the same estimated 2.02 bits/weight. Adding 6.25% residual channels reduced loss further to 6.9149 and mean module MSE by 12.8% versus learned INT2, but raised estimated storage to 3.02 bits/weight. The 12.5% residual variant had diminishing returns: loss 6.8907 at 4.02 bits/weight.

## Boundaries and scale limits

Single GPT-2-small checkpoint, fixed 16-text tiny-corpus batch, 48 transformer projection modules, no packed INT2 CUDA kernel, no standard validation-corpus perplexity, no quantization-aware training, and no larger-model replication.

## Claim scope

On a bounded GPT-2-small post-training proxy, calibration-learned per-output scales materially improve fixed-code INT2 reconstruction, while shared residual input channels provide only modest additional loss and MSE reductions at substantially higher estimated bits per weight.

## Why it stopped

Bounded proxy evidence is mixed: learned scales are useful, but the tested residual-channel INT2 mechanism gives modest marginal quality improvement for a large estimated storage increase and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should compare learned-scale residual INT2 against stronger low-bit baselines on a standard validation slice before any kernel or larger-model effort.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-validation comparison of learned-scale residual INT2 against stronger low-bit baselines
- Success threshold: At matched effective bits per weight, learned-scale residual INT2 should reduce validation perplexity by at least 5% relative to the strongest tested low-bit baseline or recover at least half of the perplexity gap between plain learned-scale INT2 and FP16.
- Stop condition: Stop if residual INT2 fails to beat the strongest matched-bit baseline, if gains disappear on the standard validation slice, or if residual overhead pushes effective storage into a range where INT4 or mixed INT2/INT4 is better.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-int2-with-learned-scales-f37f6842ac12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
