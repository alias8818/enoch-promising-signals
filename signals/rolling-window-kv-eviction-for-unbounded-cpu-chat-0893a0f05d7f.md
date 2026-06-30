# Rolling window KV eviction for unbounded CPU chat

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-window-kv-eviction-for-unbounded-cpu-chat-0893a0f05d7f`
Run ID: `rolling-window-kv-eviction-for-unbounded-cpu-chat-0893a0f05d7f-20260604T112443173330+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3d08743ebf

## What looked useful

Rolling KV windows capped projected Llama-7B-like fp16 KV memory at 512 MiB for a 1024-token window instead of growing to 16 GiB at 32768 tokens and 512 GiB at 1048576 tokens. In the local synthetic workload, window 128 preserved the full-cache top-attention target on 100% of measured steps and improved median attention-step latency 8.70x. In the long-anchor retrieval workload, window 1024 evicted the full-cache target on 63.5% of measured steps and matched the top target only 36.5%, showing rolling-only eviction is insufficient for unbounded chat recall.

## Boundaries and scale limits

No pretrained language model, natural dialogue, generated text, multi-layer transformer cache interaction, summarization, RAG, sink-token, or pinned-memory strategy was evaluated. Main run used seq_len=4096, dim=128 synthetic NumPy attention on one 8-core CPU host.

## Claim scope

Synthetic single-query attention proxy on CPU: rolling-window KV eviction bounds memory and improves attention-step latency for recent-context workloads, but rolling-only eviction fails when generation depends on old evicted anchors.

## Why it stopped

Proxy early falsification rather than full validation: rolling-only KV eviction gives the expected memory/latency bound but loses required old context when relevant keys are evicted.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate rolling KV versus full KV on a small pretrained causal LM with long-context needle/dialogue tasks and a rolling-plus-retrieval or pinned-memory control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained small-LM rolling KV recall benchmark
- Success threshold: Rolling-only must be rejected if long-recall accuracy falls more than 20 percentage points below full KV; a repaired policy is useful if it recovers at least 80% of full-KV recall while keeping KV memory bounded by the configured window plus pinned/retrieved entries.
- Stop condition: Stop if small-LM instrumentation cannot faithfully alter KV eviction, or if rolling-only and repaired policies both fail to recover at least 50% of full-KV long-recall accuracy in a reproducible small benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-window-kv-eviction-for-unbounded-cpu-chat-0893a0f05d7f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
