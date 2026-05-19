# Residual rank and initialization ablation for ternary GPT-style language models

Status: `useful_signal`
Project ID: `residual-rank-and-initialization-ablation-for-ternary-gpt-8ce25888d5`
Run ID: `residual-rank-and-initialization-ablation-for-ternary-gpt-8ce25888d5-20260519T144608863407+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b8ef7195f471

## What looked useful

Plain ternary trailed dense by +0.0967 mean validation loss. Rank-8 SVD improved over rank-0 ternary by -0.0142 mean validation loss, rank-4 zero improved by -0.0071, rank-8 zero was nearly neutral, and rank-4 random was worse by +0.0106.

## Boundaries and scale limits

Toy char-level model, 300 optimizer steps, four seeds, CPU training, Tiny Shakespeare only; not tested on subword tokenization, GPT-2-small-class scale, longer convergence schedules, or deployment efficiency.

## Claim scope

In a 2-layer 64-wide GPT-style char-level Tiny Shakespeare Tier 1 test, trainable low-rank dense residuals added to ternary linear maps modestly reduced the validation-loss gap versus plain ternary, with rank-8 SVD initialization best on average over four seeds.

## Why it stopped

Tier 1 direct small test produced a useful but mixed no-paper signal; evidence is not broad or stable enough for publication readiness.

## Recommended next action

Run a medium direct confirmation with tokenized text, longer training, parameter-matched controls, and a focused rank/init sweep before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium tokenized GPT confirmation of low-rank residuals for ternary linear maps
- Success threshold: Best residual ternary condition improves mean validation loss versus rank-0 ternary by at least 0.03 nats or closes at least 30% of the dense-vs-ternary gap across at least three seeds, without underperforming a parameter-matched dense residual control.
- Stop condition: Stop if residual ranks fail to improve rank-0 ternary by at least 0.01 mean validation loss after the planned medium run or if gains vanish under parameter-matched controls.

## Evidence references

- Artifact root: `<local-path>/projects/residual-rank-and-initialization-ablation-for-ternary-gpt-8ce25888d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
