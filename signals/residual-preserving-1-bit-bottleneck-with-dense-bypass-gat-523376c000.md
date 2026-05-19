# Residual-preserving 1-bit bottleneck with dense bypass gate

Status: `useful_signal`
Project ID: `residual-preserving-1-bit-bottleneck-with-dense-bypass-gat-523376c000`
Run ID: `residual-preserving-1-bit-bottleneck-with-dense-bypass-gat-523376c000-20260518T105208128565+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b7309050a869

## What looked useful

On the stricter sinusoidal residual task, the 16-bit gated model reduced MSE by 50.4% versus plain 1-bit and 22.3% versus linear bypass-only but missed the R2 threshold. Width ablation passed the direct-task threshold at 32 and 64 one-bit units, reaching R2 0.808 and 0.887 respectively, while still trailing dense MLP by a large margin.

## Boundaries and scale limits

No transformer, natural-language, GPT-2-small-class, latency, memory, or long-training validation was run. Dense MLP remained 10.5x to 23.6x lower MSE than the proposed model on the stricter task.

## Claim scope

Controlled synthetic residual-regression task only: a sign-STE 1-bit bottleneck branch with a learned dense bypass gate improves over plain 1-bit and linear-bypass-only controls, with the effect increasing as bottleneck width grows.

## Why it stopped

Tier 1 direct synthetic evidence supports the mechanism but is insufficient for paper readiness; the proposed model remains far behind dense MLP and has not been validated in model training.

## Recommended next action

Stop as no-paper useful signal; next bounded action would be a small transformer adapter validation comparing gated 1-bit, plain 1-bit, and parameter-matched dense adapters on validation loss plus gate/branch diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small transformer adapter validation for residual-preserving gated 1-bit bottlenecks
- Success threshold: Gated 1-bit adapter improves validation loss by at least 2% versus both plain 1-bit and linear bypass-only controls across mean of 3 seeds, with no training instability and diagnostics showing nontrivial use of both bypass and bit branch.
- Stop condition: Stop if the gated 1-bit adapter does not beat both controls on mean validation loss, if the learned gate collapses to bypass-only behavior, or if the bit branch shows unstable/collapsed codes.

## Evidence references

- Artifact root: `<local-path>/projects/residual-preserving-1-bit-bottleneck-with-dense-bypass-gat-523376c000`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
