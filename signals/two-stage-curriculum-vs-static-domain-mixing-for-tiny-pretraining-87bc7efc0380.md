# Two-Stage Curriculum vs Static Domain Mixing for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `two-stage-curriculum-vs-static-domain-mixing-for-tiny-pretraining-87bc7efc0380`
Run ID: `two-stage-curriculum-vs-static-domain-mixing-for-tiny-pretraining-87bc7efc0380-20260609T205151744192+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e1d7582ea778

## What looked useful

Exact 50/50 ordered curricula were much worse than static mixing: a_then_b equal-mix loss 4.9915 vs static 1.9244, and b_then_a 3.6300 vs static 1.9244. The only slight aggregate improvement, a_then_mix at 1.9105 vs static 1.9244, used about 301 A batches and 99 B batches, so it is confounded by domain exposure and worsened B validation loss.

## Boundaries and scale limits

Synthetic domains, 413184-parameter Transformer, 400 training steps, 3 seeds, one GB10 local GPU. This is not evidence about full natural-language/code pretraining, GPT-2-small-class models, or long-horizon real-corpus scaling.

## Claim scope

On a synthetic two-domain tiny causal-LM pretraining benchmark, simple ordered two-stage curricula do not beat static domain mixing when total domain exposure is controlled; exposure-imbalanced curricula can move aggregate loss by reallocating training toward the easier domain.

## Why it stopped

Proxy/tiny synthetic evidence early-falsified simple two-stage ordering as a clean improvement over static mixing; this is not a full-scale validation.

## Recommended next action

Stop this run as a synthetic no-paper useful signal; any next test should use matched domain exposure with replay-preserving curricula on a real tiny-pretraining corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-preserving curricula under matched domain exposure for tiny real-corpus pretraining
- Success threshold: Replay-preserving curriculum improves equal-mixture validation loss by at least 2% relative to static mixing without worsening either per-domain validation loss by more than 1%.
- Stop condition: Stop if matched-exposure curricula fail to beat static mixing after 3 seeds or if any gain only appears by sacrificing one domain's validation loss beyond the threshold.

## Evidence references

- Artifact root: `<local-path>/projects/two-stage-curriculum-vs-static-domain-mixing-for-tiny-pretraining-87bc7efc0380`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
