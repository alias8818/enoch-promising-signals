# W4A3 with Learned Per-Channel FP8 Activation Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `w4a3-with-learned-per-channel-fp8-activation-residual-520dca23036c`
Run ID: `w4a3-with-learned-per-channel-fp8-activation-residual-520dca23036c-20260609T101311795706+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58d8e0541c11

## What looked useful

FP8 activation residual coding sharply reduced held-out linear reconstruction MSE, but learned per-channel residual scaling was consistently worse than a fixed alpha=1 residual control by 4.5% to 7.5% MSE on medium probes. The learned coefficients collapsed near a uniform scale around 0.93, so this run does not support the learned per-channel mechanism.

## Boundaries and scale limits

No transformer or language-model perplexity run; no packed W4A3 kernel; no memory-bandwidth or serving-throughput measurement; residual branch stores an additional FP8 value per activation element, so activation traffic is not comparable to pure A3.

## Claim scope

Bounded synthetic CUDA/PyTorch linear reconstruction probe with W4 symmetric per-output-channel weights, A3 activations, and native FP8 E4M3 residual round-trip casts on normal, mixture-outlier, and Student-t activation distributions.

## Why it stopped

Early bounded/proxy falsification: the residual mechanism works as reconstruction coding, but the learned per-channel scale did not beat the trivial fixed alpha=1 control and the extra FP8 residual changes the activation-bit budget.

## Recommended next action

Stop this learned-per-channel variant as no-paper evidence; if continuing, run a bounded transformer-block or GPT-2-small-class fixed-FP8-residual coding follow-up with W4A3, W4A4, and W4A8 controls plus kernel or memory-traffic overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fixed FP8 activation residual coding in a small transformer block
- Success threshold: Fixed FP8 residual must improve model loss/perplexity over W4A4 at comparable or justified activation traffic, and learned residual must be excluded unless it beats fixed alpha=1 by at least 3% on the direct target metric.
- Stop condition: Stop if fixed FP8 residual fails to beat W4A4 on direct model quality or if measured overhead erases the quality benefit relative to W4A8/simple mixed precision.

## Evidence references

- Artifact root: `<local-path>/projects/w4a3-with-learned-per-channel-fp8-activation-residual-520dca23036c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
