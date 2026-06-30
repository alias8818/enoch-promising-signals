# Activation Residual Channels for INT4 Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-residual-channels-for-int4-training-83a64128987f`
Run ID: `activation-residual-channels-for-int4-training-83a64128987f-20260604T093918870906+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8f397d98905f

## What looked useful

Across 5 seeds, ARC k=8 improved mean test loss versus INT4 by 0.0541 and reduced reconstruction MSE to 0.834x INT4 at about 5.33 effective bits per activation, with +0.0033 mean accuracy. A fixed-channel same-budget control showed much weaker loss and reconstruction improvement, suggesting top residual selection is the active mechanism, but accuracy remained mixed.

## Boundaries and scale limits

Small MLP only; synthetic data only; simulated INT4 activations in PyTorch tensors rather than packed INT4 kernels; no transformer, real-corpus, GPT-2-small-class, long-schedule, or production memory-bandwidth validation.

## Claim scope

On a bounded synthetic teacher-classification MLP probe, activation residual channels that preserve the largest per-sample INT4 activation residuals reduce activation reconstruction MSE and test loss versus plain simulated INT4 activation training. Accuracy gains are small and not robust enough to claim broad training improvement.

## Why it stopped

Evidence is bounded and partly proxy: the synthetic MLP results support the reconstruction/loss mechanism but do not validate transformer INT4 training or real memory-throughput benefits.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next action is a bounded small-transformer language-model follow-up with packed-storage accounting before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer ARC INT4 activation training on real text
- Success threshold: ARC must reduce validation loss by at least 2% relative to INT4 at matched training tokens and outperform the fixed-channel residual control while staying under 6 effective bits per activation.
- Stop condition: Stop if ARC does not beat INT4 validation loss in two independent seeds, if gains disappear against fixed-channel residual control, or if packed residual metadata exceeds the memory budget that makes INT4 training attractive.

## Evidence references

- Artifact root: `<local-path>/projects/activation-residual-channels-for-int4-training-83a64128987f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
