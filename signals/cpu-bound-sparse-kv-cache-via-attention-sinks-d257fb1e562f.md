# CPU-Bound Sparse KV Cache via Attention Sinks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bound-sparse-kv-cache-via-attention-sinks-d257fb1e562f`
Run ID: `cpu-bound-sparse-kv-cache-via-attention-sinks-d257fb1e562f-20260524T233240985898+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5293e1f994e2

## What looked useful

At 8,192 tokens, dense attention took 27.705 ms/token and 32 MiB KV, while 8 sinks plus a 256-token window took 0.672 ms/token and 1.03 MiB KV in the latency table. Synthetic output error was about 5.4% mean relative L2 at 95% retained attention mass and about 1.0% at 99%, but diffuse/random attention failed badly.

## Boundaries and scale limits

No real decoder LM, perplexity, generation quality, multi-layer KV eviction, tokenizer workload, or production serving stack was tested. Quality evidence is synthetic and mechanism-level only.

## Claim scope

A self-contained single-thread CPU decode microbenchmark shows that retaining 8 attention sink tokens plus a 256-token recent window can reduce single-token attention latency and KV memory substantially versus dense KV at 1k-16k sequence lengths; synthetic quality remains acceptable only when the retained subset contains about 95-99% of dense attention mass.

## Why it stopped

Proxy/mechanism evidence only: the speed and memory effect is supported locally, but real LM quality was not directly tested, so this is no-paper useful signal rather than validation.

## Recommended next action

Run a bounded real small-LM CPU decode test comparing dense KV against sink+window eviction, recording tokens/s, next-token loss or perplexity, and per-layer retained attention mass on long prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM CPU Decode Validation for Sink+Window KV Eviction
- Success threshold: At least 2x CPU decode speedup at 8k context with next-token loss or perplexity no more than 5% worse than dense KV and median retained attention mass at least 95% in most layers.
- Stop condition: Stop if loss/perplexity degrades by more than 10% at all tested sink/window settings or retained attention mass is below 90% in most layers.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bound-sparse-kv-cache-via-attention-sinks-d257fb1e562f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
