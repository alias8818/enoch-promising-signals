# Domain-Stratified Sampling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-stratified-sampling-for-tiny-pretraining-43a0a1921f4c`
Run ID: `domain-stratified-sampling-for-tiny-pretraining-43a0a1921f4c-20260530T074243511585+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/38af9342d8d1

## What looked useful

Equal-domain stratification acts as a minority-domain rescue lever but overcorrects the source distribution. In the 4000-document main run it improved business by -0.0838 NLL/token and sci/tech by -0.0461, while harming world by +0.3957 and sports by +0.0437; aggregate macro NLL worsened by +0.0773.

## Boundaries and scale limits

This is a tiny/count-based language-model proxy on one public corpus, not neural transformer pretraining. It does not cover tokenizer effects, long context, downstream transfer, larger corpora, or learned optimization dynamics.

## Claim scope

On AG News with an intentionally imbalanced four-domain source pool and a fixed-budget word-level bigram language model, naive equal-domain sampling helps rare domains but does not improve aggregate heldout language-model likelihood beyond very small budgets; at 800 to 4000 sampled documents it is consistently worse than uniform sampling.

## Why it stopped

Naive equal-domain stratification was directly tested in a bounded tiny-LM proxy and failed to improve aggregate likelihood at practical budgets, so the current idea is not ready for paper writing.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is to test temperature-smoothed or target-mixture domain sampling against uniform and equal-domain controls on the same setup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Temperature-smoothed domain sampling for tiny LM pretraining
- Success threshold: Find a non-uniform mixture with macro NLL at least 0.01 lower than uniform and no more than 0.01 micro NLL worse than uniform across paired seeds, or show a Pareto improvement in worst-domain NLL without aggregate regression.
- Stop condition: Stop if all softened mixtures either match uniform within noise or reproduce the equal-domain tradeoff of improving rare domains while worsening macro or micro NLL.

## Evidence references

- Artifact root: `<local-path>/projects/domain-stratified-sampling-for-tiny-pretraining-43a0a1921f4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
