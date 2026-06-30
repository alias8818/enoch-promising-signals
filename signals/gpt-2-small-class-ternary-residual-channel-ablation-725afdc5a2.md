# GPT-2-Small-Class Ternary Residual Channel Ablation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-class-ternary-residual-channel-ablation-725afdc5a2`
Run ID: `gpt-2-small-class-ternary-residual-channel-ablation-725afdc5a2-20260527T191743320725+0000`

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

- Parent run decision: Ternary-Weight Residual Channels for GPT-2-Small: enoch://control-plane/projects/ternary-weight-residual-channels-for-gpt-2-small-4df2a4cf40b1/runs/ternary-weight-residual-channels-for-gpt-2-small-4df2a4cf40b1-20260527T164127117767+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe6b5049c075

## What looked useful

Learned ternary residual-channel gates beat random same-sparsity controls, indicating channel-specific structure, but they failed the stated sparse-retention threshold. Forced 50% ablation raised validation loss from 4.05119 to 7.87595 nats/token, far beyond the allowed +0.10 nats/token.

## Boundaries and scale limits

Short gate-only optimization, 128 training blocks, 64 validation blocks, sequence length 128, one seed, no base-model training, no OpenWebText-scale corpus, no downstream tasks, and no layer-selective sparsity search.

## Claim scope

Frozen GPT-2 small residual block output channels with learned ternary per-channel gates on a small Wikitext-2 held-out language-modeling test.

## Why it stopped

Tier-1 controlled direct test falsified the 50% sparse-retention threshold on frozen GPT-2-small residual channels while showing only mechanism-level signal versus random controls.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a layer-selective sparsity Pareto sweep to see whether the channel-specific signal is confined to later blocks or lower ablation fractions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-selective GPT-2 residual channel sparsity Pareto sweep
- Success threshold: Find a layer-selective ternary gate with at least 25% total residual-channel zeros, validation loss degradation <= 0.10 nats/token versus dense, and >= 0.05 nats/token advantage over random same-sparsity controls across at least three seeds.
- Stop condition: Stop if no tested layer-selective budget at or above 25% zeros achieves <= 0.10 nats/token degradation or if learned gates do not beat random controls by >= 0.05 nats/token.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-ternary-residual-channel-ablation-725afdc5a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
