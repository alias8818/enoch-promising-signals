# Anchor-Pinned KV Compression: Keep Exact Tokens, Drop the Rest

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-pinned-kv-compression-keep-exact-tokens-drop-the-rest-b238ff1fd19b`
Run ID: `anchor-pinned-kv-compression-keep-exact-tokens-drop-the-rest-b238ff1fd19b-20260620T235203006629+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8637e62a1db0

## What looked useful

Anchor-pinned KV compression works in the narrow case where important tokens are known and retained exactly, but recovery degrades roughly in proportion to missed anchors, making anchor identification the key unresolved risk.

## Boundaries and scale limits

Synthetic attention only; oracle or near-oracle anchor labels; no pretrained LLM decode loop; no real long-context benchmark; no latency or allocator measurement beyond bounded GPU tensor execution.

## Claim scope

In a deterministic synthetic attention retrieval probe up to 32768 tokens with 64 known anchors, exact anchor-pinned KV retention preserved target retrieval at 1%-5% cache budgets while equal-budget generic retention failed when target anchors were not retained.

## Why it stopped

No-paper closure: local evidence is a useful synthetic mechanism signal, but it is oracle-dependent and not direct full validation.

## Recommended next action

Run a bounded model-facing needle/retrieval benchmark with a realistic online anchor selector and measure accuracy, KV memory, and decode latency against recent/window and streaming baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-facing anchor-pinned KV retention with realistic anchor selection
- Success threshold: At <=10% retained KV tokens, anchor-pinned retention recovers at least 90% of full-cache retrieval accuracy and beats recent-window retention by at least 20 absolute percentage points on target retrieval, with measured memory reduction.
- Stop condition: Stop if realistic anchor selection cannot exceed recent-window retrieval by 5 absolute percentage points at matched budgets or if latency overhead erases memory benefits in the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-pinned-kv-compression-keep-exact-tokens-drop-the-rest-b238ff1fd19b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
