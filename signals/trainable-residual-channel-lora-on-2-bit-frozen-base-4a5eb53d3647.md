# Trainable Residual Channel LoRA on 2-bit Frozen Base

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trainable-residual-channel-lora-on-2-bit-frozen-base-4a5eb53d3647`
Run ID: `trainable-residual-channel-lora-on-2-bit-frozen-base-4a5eb53d3647-20260621T025932013982+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc4ce748255b

## What looked useful

Across 5 seeds, combined channel residual + rank-4 LoRA reached mean test MSE 0.039701 versus rank-4 LoRA 0.112706, channel-only 0.119397, and rank-8 LoRA-only 0.067862. Combined used 864 trainable parameters, less than rank-8 LoRA's 1536.

## Boundaries and scale limits

No transformer, token dataset, language-model perplexity, downstream accuracy, or large-model memory/throughput evidence was produced. The target construction favors the proposed decomposition and should be treated as a mechanism probe only.

## Claim scope

In a controlled synthetic linear adaptation where the downstream residual on a frozen 2-bit quantized base is explicitly composed of a channel-wise residual plus a low-rank residual, a trainable residual-channel LoRA adapter recovers the target mapping better than channel-only, LoRA-only, and higher-rank LoRA-only controls tested here.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but not direct language-model evidence or publication-grade validation.

## Recommended next action

Run a bounded tiny-transformer or GPT-2-small-class language-model follow-up with a frozen 2-bit base, matched trainable-parameter LoRA controls, validation perplexity, and memory/throughput metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Channel LoRA on a Frozen 2-bit Tiny Transformer
- Success threshold: Combined residual-channel LoRA improves final validation perplexity by at least 5% relative to the best parameter-matched LoRA-only control while adding less than 10% wall-clock overhead in the bounded setup.
- Stop condition: Stop if combined fails to beat parameter-matched LoRA on validation perplexity in two independent seeds or if memory/throughput overhead exceeds 25% without accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/trainable-residual-channel-lora-on-2-bit-frozen-base-4a5eb53d3647`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
