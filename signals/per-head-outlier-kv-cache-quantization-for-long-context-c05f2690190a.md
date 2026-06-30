# Per-Head Outlier KV-Cache Quantization for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-head-outlier-kv-cache-quantization-for-long-context-c05f2690190a`
Run ID: `per-head-outlier-kv-cache-quantization-for-long-context-c05f2690190a-20260607T154425244184+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74bd16827ba8

## What looked useful

Per-head outlier KV-cache quantization showed a consistent bounded mechanism signal. In the GPT-2 synthetic 512-token run, outlier int4 reduced next-token KL to 0.0011 versus 0.5139 for tensor int4 and 0.5514 for per-head int4, with memory ratio 0.3438x fp16 and top-1 match 1.0. In the longer synthetic run averaging 657 tokens, outlier int4 reduced KL to 0.0268 versus 1.2665 and 0.6889, but top-1 match was only 0.5.

## Boundaries and scale limits

No packed int4 runtime, decode throughput, allocator memory, modern long-context model, 8k+ context, task accuracy, or perplexity validation was measured. Synthetic long-context prompts were repeated text and the real-text WikiText rows averaged only 114 tokens.

## Claim scope

On GPT-2 small KV caches up to hundreds of tokens, retaining the top 12.5% mean-absolute-value channels per head in fp16 while quantizing the remaining channels to int4 improved cache reconstruction, last-query attention-output fidelity, and held-out next-token logit fidelity versus whole-tensor int4 and plain per-head int4 baselines, at about 0.344x fp16 payload memory instead of about 0.250x.

## Why it stopped

Useful bounded mechanism signal, but no-paper closure because this run is proxy-level for long-context serving and lacks runtime and task-level validation.

## Recommended next action

Run a bounded direct follow-up with a packed or fake-packed KV-cache decode path on a locally runnable long-context model, measuring perplexity or task drift plus decode latency and real memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed Per-Head Outlier KV Decode on a Local Long-Context Model
- Success threshold: At least 2x payload memory reduction versus fp16, lower perplexity/task drift than tensor int4 and per-head int4 baselines, and no more than 10% decode throughput regression versus the best int4 baseline in the bounded local setup.
- Stop condition: Stop if packed/fake-packed outlier retention fails to improve perplexity or task drift over pure int4 baselines at any tested outlier fraction, or if metadata/runtime overhead removes most of the memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-outlier-kv-cache-quantization-for-long-context-c05f2690190a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
