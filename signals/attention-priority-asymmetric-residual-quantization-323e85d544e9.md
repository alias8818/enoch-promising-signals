# Attention-Priority Asymmetric Residual Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `attention-priority-asymmetric-residual-quantization-323e85d544e9`
Run ID: `attention-priority-asymmetric-residual-quantization-323e85d544e9-20260531T153334964260+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58a9b8942e46

## What looked useful

At a 10% residual-slot budget over 60 trials per regime, attention-priority residual placement reduced int4 attention-output MSE by 51.4% in sparse attention and 40.0% in local attention, versus about 10% for random and 9-10% for uniform controls. Diffuse attention showed a smaller 15.9% reduction versus 10.0% random. A 2-20% budget sweep showed gains tracking selected attention mass, while low-attention selection produced near-zero benefit in concentrated regimes.

## Boundaries and scale limits

Tested only synthetic Q/K/V tensors on one attention operation, value-cache quantization only, exact residual restoration rather than a packed practical residual format, and known attention mass rather than an online predicted priority policy. No real transformer perplexity, task accuracy, latency, memory-bandwidth, or multi-layer accumulation evidence.

## Claim scope

Synthetic KV-cache attention proxy: with per-token int4 value-cache quantization and a fixed exact residual slot budget, selecting residual slots by aggregate attention mass reduces one-step attention-output MSE more than random or uniform selection, especially for sparse/local concentrated attention.

## Why it stopped

Proxy/synthetic evidence supports the allocation mechanism but does not directly validate a real model or deployable asymmetric residual quantization format.

## Recommended next action

Run a bounded direct small-transformer KV-cache experiment with matched-byte residual formats, predicted/online attention priority, random/uniform controls, and perplexity plus latency/memory metrics; stop this run as useful proxy evidence rather than paper-ready validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Transformer KV-Cache Attention-Priority Residual Quantization
- Success threshold: Attention-priority residual allocation improves perplexity or output KL/error by at least 20% relative to the random residual control's recovered error at the same byte budget, with no more than 10% decode-latency overhead in the tested small-model setup.
- Stop condition: Stop if attention-priority fails to beat random/uniform matched-byte controls by at least 10% recovered-error improvement on real KV tensors, or if metadata/scatter overhead makes the quality gain impractical.

## Evidence references

- Artifact root: `<local-path>/projects/attention-priority-asymmetric-residual-quantization-323e85d544e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
