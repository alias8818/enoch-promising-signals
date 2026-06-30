# Residual-channel KV-cache compression for long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-kv-cache-compression-for-long-context-inference-3ac96b5d5e65`
Run ID: `residual-channel-kv-cache-compression-for-long-context-inference-3ac96b5d5e65-20260524T160715364467+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/25c497e826a9

## What looked useful

Uniform int4 KV quantization at 25% estimated cache fraction preserved continuation behavior far better than retaining only top-energy channels; top-energy fp16 retention with int4 residuals showed a limited GPT-2 advantage over random retention at 43.75% cache fraction but was mixed across models.

## Boundaries and scale limits

Only distilgpt2/gpt2, 256-384 prompt tokens, 64-96 continuation tokens, hand-written local passages, simulated dequantized compression, no custom serving kernels, no 7B+ models, no benchmark corpus, and no true long-context memory-pressure run.

## Claim scope

Small GPT-2-family autoregressive continuation probes show that dropping residual KV channels is not viable, while exact top-energy channels plus int4 residual quantization can reduce logit drift versus random channel selection on GPT-2 at the same estimated cache fraction.

## Why it stopped

Proxy-scale early falsification for residual-channel dropping and mixed small-model support for top-energy residual quantization; not full long-context validation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen test should compare activation-aware retained-channel selection against uniform 2/3/4-bit KV quantization at matched byte budgets on a real text corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware residual-channel KV selection at matched byte budgets
- Success threshold: Residual-channel selection reduces KL vs fp16 by at least 20% relative to the best uniform quantization baseline at the same estimated cache fraction, with NLL delta no worse than 0.05 on corpus continuations in two model sizes.
- Stop condition: Stop as negative if uniform quantization matches or beats residual-channel selection on KL or NLL at matched byte budgets in either model.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-kv-cache-compression-for-long-context-inference-3ac96b5d5e65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
