# Activation-aware INT2 residual salience on GPT-2 linear weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1`
Run ID: `activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1-20260523T124002690437+0000`

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

- Parent run decision: INT2 Agent Weights with Residual Salience Channels: enoch://control-plane/projects/int2-agent-weights-with-residual-salience-channels-d340cf469718/runs/int2-agent-weights-with-residual-salience-channels-d340cf469718-20260523T112545230441+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

At 2% residual density over 84,934,656 GPT-2 linear weights, activation-aware residuals reduced loss delta versus magnitude-only by 13.10% and KL by 12.37% on 128 WikiText-2 held-out sequences, while logit MSE was 11.58% worse. A 1%/2%/4% sweep showed consistent loss/KL gains and consistent logit-MSE regression.

## Boundaries and scale limits

Tested only GPT-2-small, short 128-token sequences, one WikiText-2 raw split plus a small embedded-text fixture, one calibration selection, no packed INT2 kernels, no larger models, no GPTQ/AWQ/SmoothQuant comparison, and no statistical confidence intervals across multiple corpus splits.

## Claim scope

On GPT-2-small Conv1D linear weights with a simple per-output-channel INT2 quantizer and sparse FP residuals, activation-aware residual selection improved held-out language-model loss delta and KL to the FP32 teacher versus equal-density magnitude-only residual selection on a small WikiText-2 controlled test, but worsened unweighted logit MSE.

## Why it stopped

Tier 1 direct evidence supports a useful mixed mechanism signal, but the result is no-paper because logit MSE regressed, baselines are simple, and robustness/generalization are not established.

## Recommended next action

Run a bounded deepen test with multiple WikiText-2/OpenWebText-style calibration/eval splits, layerwise output-error diagnostics, and GPTQ/AWQ-style activation-aware baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust split-and-layer diagnostic for activation-aware INT2 residual salience on GPT-2
- Success threshold: Activation-aware residuals must show a statistically consistent >=10% mean reduction in held-out loss delta or KL versus magnitude-only at 2% residual density without an unexplained large layer-local error regression, and must explain or mitigate the logit-MSE tradeoff.
- Stop condition: Stop if the >=10% loss/KL advantage disappears across split seeds, if the logit-MSE regression maps to harmful layerwise behavior, or if a stronger activation-aware baseline dominates the residual-salience rule.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-int2-residual-salience-on-gpt-2-linear-we-85cf4f46d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
