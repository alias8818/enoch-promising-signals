# 3-bit GPTQ with 256-step recovery tuning beats 4-bit baselines on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `3-bit-gptq-with-256-step-recovery-tuning-beats-4-bit-baselines-on-gb10-c8a89fe30bb3`
Run ID: `3-bit-gptq-with-256-step-recovery-tuning-beats-4-bit-baselines-on-gb10-c8a89fe30bb3-20260530T013213302931+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e6f3dc984d66

## What looked useful

Recovery tuning can erase the 3-bit vs 4-bit post-quantization quality gap in this bounded setup, but any stronger claim must include a 4-bit recovery-tuned control because that control won on average here.

## Boundaries and scale limits

Proxy-scale model and dataset only; no pretrained LLM, no standard benchmark, no packed GPTQ kernels, no inference throughput measurement, and only 16 random validation batches per run.

## Claim scope

On a small Tiny Shakespeare character Transformer run on GB10, a GPTQ-style 3-bit Linear-weight quantization proxy with 256 recovery-tuning steps beat a 4-bit post-quantization baseline across three seeds, but did not beat a 4-bit baseline given the same 256 recovery-tuning budget.

## Why it stopped

Bounded proxy evidence is mixed: the narrow post-quant baseline comparison is supported, but the broader beats-4-bit-baselines claim fails against an equal-budget 4-bit recovery baseline.

## Recommended next action

Stop this run as no-paper useful signal; a future bounded direct test should use a pretrained GPT-2-small-class model with real GPTQ/AWQ tooling and include both 4-bit post-quant and 4-bit recovery-tuned controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small 3-bit recovery tuning versus equal-budget 4-bit GPTQ controls
- Success threshold: 3-bit with 256 recovery steps improves over 4-bit post-quantization and is within 0.5% perplexity of, or better than, 4-bit with the same recovery budget on repeated evaluations.
- Stop condition: Stop if 3-bit recovery is worse than 4-bit recovery by more than 1% perplexity on two repeated evaluations or if real GPTQ tooling cannot run on GB10 within a bounded local budget.

## Evidence references

- Artifact root: `<local-path>/projects/3-bit-gptq-with-256-step-recovery-tuning-beats-4-bit-baselines-on-gb10-c8a89fe30bb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
