# Gradient Coreset Selection for Tiny Model Home Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-coreset-selection-for-tiny-model-home-training-7592a0240576`
Run ID: `gradient-coreset-selection-for-tiny-model-home-training-7592a0240576-20260602T191454673702+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b67010670af1

## What looked useful

Gradient herding improved mean test accuracy over random by +3.13 pp at 5% subset, +1.43 pp at 10%, and +0.69 pp at 20%; naive loss top-k and gradient-norm top-k controls performed much worse, apparently overselecting noisy/hard examples.

## Boundaries and scale limits

Synthetic-only NumPy MLP evidence; no real home-training corpus, no transformer/GPT-2-small-class model, no large-scale run, and no end-to-end wall-clock/token-budget validation.

## Claim scope

On a dependency-free synthetic noisy long-tail 10-class classification benchmark, one-shot class-balanced gradient herding from initial tiny-MLP last-layer gradients selected 5-20% training subsets that outperformed random and stratified-random subsets under a fixed 500-update training budget.

## Why it stopped

No-paper closure: this run produced a useful synthetic small-probe signal, but not direct publication-grade evidence for real tiny model home training.

## Recommended next action

Run a bounded real-data deepen follow-up using a tiny transformer or small CNN with equalized update and wall-clock budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data tiny-model gradient coreset validation
- Success threshold: Gradient herding beats both random and stratified-random subsets by at least 1.0 percentage point test accuracy or a practically comparable held-out loss reduction at 10% subset budget, with no more than 20% extra selection-plus-training wall-clock.
- Stop condition: Stop as negative if gradient herding fails to beat stratified random on the primary held-out metric in at least 4 of 5 seeds or if selection overhead dominates any training savings.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-selection-for-tiny-model-home-training-7592a0240576`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
