# Anchor-Pinned KV-Cache Compression for Long Agent Contexts on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-kv-cache-compression-for-long-agent-contexts-on-gb10-17bf6b86d0ac`
Run ID: `anchor-pinned-kv-cache-compression-for-long-agent-contexts-on-gb10-17bf6b86d0ac-20260613T231757761440+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4d69433c599

## What looked useful

Anchor pinning preserved anchor-seeking output cosine far better than non-pinned baselines at long lengths: at 32,768 tokens, anchor_pinned achieved 0.745 cosine versus full attention, compared with 0.137 for uniform_block_recent and 0.071 for recent_only, while using 3.5% of full KV cache tokens and running 63.3x faster in the PyTorch proxy. However, middle-seeking cosine stayed near 0.15, so the method is unsuitable when exact older middle-context retrieval matters.

## Boundaries and scale limits

The evidence is synthetic and attention-only. It does not validate real transformer generation quality, full long-agent workloads, production paged-attention backends, learned compression, multi-request serving, or robustness across model families. Middle-token retrieval remains poor under the tested block-mean compression.

## Claim scope

On a synthetic single-step decode-attention proxy on NVIDIA GB10, exact pinning of the first 128 anchor KV entries plus exact recent-tail retention and 64-token middle block means preserves anchor-seeking attention outputs substantially better than uniform block compression or recent-only retention at 4k-32k sequence lengths.

## Why it stopped

Closed as a no-paper useful signal because the local proxy supports the anchor-preservation mechanism but also exposes severe middle-context retrieval loss and does not provide direct full-model long-agent evidence.

## Recommended next action

Run a bounded real-transformer follow-up on GB10 using a small open model and task prompts with explicit system/tool-schema anchors, comparing full KV, sliding-window/recent-only, uniform compression, and anchor-pinned compression on exact-match task accuracy and decode throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Anchor-Pinned KV Compression on Tool-Schema Retention Tasks
- Success threshold: At 16k or larger context length, anchor-pinned compression should recover at least 80% of full-KV task accuracy and beat recent-only and uniform compression by at least 10 percentage points on anchor-dependent tasks at a comparable KV budget, while retaining at least a 2x decode-latency or memory advantage over full KV.
- Stop condition: Stop if anchor-pinned compression fails to beat recent-only or uniform compression by at least 5 percentage points on anchor-dependent task accuracy in two independently seeded runs, or if implementation overhead eliminates the memory/latency advantage over full KV.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-kv-cache-compression-for-long-agent-contexts-on-gb10-17bf6b86d0ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
