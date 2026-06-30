# Res-INT2: Residual-Guarded INT2 GPT-2 Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `res-int2-residual-guarded-int2-gpt-2-inference-793830808c5f`
Run ID: `res-int2-residual-guarded-int2-gpt-2-inference-793830808c5f-20260523T231453964994+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71075af61b6a

## What looked useful

Across 80 medium proxy trials, targeted residual guards reduced INT2 MSE by 1.19%, 2.28%, 5.65%, and 11.16% at 1%, 2%, 5%, and 10% guarded output-channel budgets. Random guards achieved 1.02%, 1.96%, 4.99%, and 9.99%, so targeted selection consistently helped but only by 0.17 to 1.17 percentage points absolute beyond random. Unguarded INT2 relative MSE remained high at 0.668.

## Boundaries and scale limits

No pretrained GPT-2 checkpoint, no language-model loss or perplexity, no generation-quality evaluation, no packed INT2 kernel, no GPU utilization, and no end-to-end transformer residual-stream test. Results are synthetic projection evidence only.

## Claim scope

Bounded NumPy proxy on GPT-2-small-shaped linear projections with synthetic heavy-tailed activations and weights: calibration-selected FP residual corrections for INT2 output channels reduce projection error more than unguarded INT2 and slightly more than random guarded channels.

## Why it stopped

Early bounded proxy result: the residual mechanism works mechanically, but the evidence is synthetic/proxy-only and the simple channel guard mostly buys back precision through extra residual storage; it does not establish viable residual-guarded INT2 GPT-2 inference.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded direct GPT-2-small pretrained evaluation with perplexity/loss and a packed-kernel or realistic latency baseline before investing in larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small residual-guarded INT2 perplexity probe
- Success threshold: At 5-10% guarded channel budget, targeted residual-guarded INT2 should close at least half of the perplexity or NLL gap between unguarded INT2 and FP baseline, while beating random guard by at least 10% relative gap closure at comparable effective bits.
- Stop condition: Stop if pretrained GPT-2-small targeted guards fail to beat random guards by the success threshold or if residual correction latency/storage erases the intended INT2 efficiency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/res-int2-residual-guarded-int2-gpt-2-inference-793830808c5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
