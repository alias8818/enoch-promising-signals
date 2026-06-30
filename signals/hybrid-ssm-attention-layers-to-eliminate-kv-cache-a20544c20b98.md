# Hybrid SSM-Attention Layers to Eliminate KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-ssm-attention-layers-to-eliminate-kv-cache-a20544c20b98`
Run ID: `hybrid-ssm-attention-layers-to-eliminate-kv-cache-a20544c20b98-20260526T034021699854+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/acd2798a41c2

## What looked useful

Sparse retained attention appears sufficient for toy exact recall while recurrent SSM layers remove most per-layer KV state; fully eliminating attention/KV cache is not supported because the SSM-only control failed delayed recall.

## Boundaries and scale limits

Synthetic tasks only; no real language corpus, pretrained model, GPT-2-small-class baseline, optimized SSM kernel, measured serving memory, measured decode latency, long-context sweep, or robustness across seeds.

## Claim scope

In sub-million-parameter synthetic sequence models at sequence length 64, replacing three of four causal attention layers with recurrent diagonal SSM layers preserved local Markov next-token loss and delayed-copy suffix recall while reducing estimated fp16 decode cache from 98304 to 25152 bytes per sequence. A zero-attention SSM-only variant matched the local task but failed delayed-copy recall at chance-level suffix loss.

## Why it stopped

No-paper closure: this is bounded synthetic evidence that supports cache reduction but not full KV-cache elimination or publication-grade language-model validation.

## Recommended next action

Run a bounded real-corpus tiny-GPT follow-up with measured autoregressive cache and latency before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-GPT retained-attention SSM cache and perplexity validation
- Success threshold: Hybrid validation perplexity within 5% of all-attention baseline, recall-probe suffix loss within 10% of baseline, and measured decode cache memory at least 3x lower at the tested context length.
- Stop condition: Stop if hybrid perplexity is more than 10% worse than baseline after matched training compute, if recall probe collapses relative to all-attention, or if measured decode memory reduction is below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-ssm-attention-layers-to-eliminate-kv-cache-a20544c20b98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
