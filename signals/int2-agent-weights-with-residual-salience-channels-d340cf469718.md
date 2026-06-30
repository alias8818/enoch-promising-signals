# INT2 Agent Weights with Residual Salience Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-agent-weights-with-residual-salience-channels-d340cf469718`
Run ID: `int2-agent-weights-with-residual-salience-channels-d340cf469718-20260523T112545230441+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

Plain INT2 raised distilgpt2 PPL from 88.85 to 1.15e10. Residual channels reduced weight reconstruction MSE and improved PPL at larger fractions, but 10% residual channels still had PPL 2.19e6 at 3.63 effective bits/weight, and 50% residual channels still had PPL 6094 at 10.03 effective bits/weight. Full residual restored baseline, validating the mechanism implementation while showing this salience rule is inefficient.

## Boundaries and scale limits

Single small GPT-2-class model, short fixed text sample, inference only, simulated storage estimates with dequantized FP16 execution, no packed INT2 kernel, no training or agent-task evaluation, and no activation/Hessian-aware salience.

## Claim scope

On a bounded distilgpt2 inference test over 2,032 tokens, replacing GPT-2 Conv1D weights with per-output-channel affine INT2 severely damages perplexity, and reconstruction-error-selected FP16 output-channel residuals only recover useful quality when the residual fraction is too large to preserve the intended low-bit advantage.

## Why it stopped

Proxy-limited but direct inference evidence showed that modest residual budgets do not recover usable perplexity; larger residuals recover quality only by giving up most of the compression advantage.

## Recommended next action

Stop this variant as a no-paper useful signal; the specific reconstruction-error output-channel residual rule is an early direct falsification at modest residual budgets, not a full validation of INT2 residual salience.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT2 residual salience on GPT-2 linear weights
- Success threshold: At <=4 effective bits/weight, activation-aware residual selection improves loss by at least 50% of the gap between plain INT2 and FP16 baseline and beats reconstruction-error salience at the same budget.
- Stop condition: Stop if activation-aware 10% residual remains above 2x FP16 baseline loss or fails to beat reconstruction-error salience at matched effective bits/weight.

## Evidence references

- Artifact root: `<local-path>/projects/int2-agent-weights-with-residual-salience-channels-d340cf469718`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
