# Anchor-KV: Exact Token Retention with Compressed Filler

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-kv-exact-token-retention-with-compressed-filler-a47715bcc6e4`
Run ID: `anchor-kv-exact-token-retention-with-compressed-filler-a47715bcc6e4-20260528T222613221801+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dcdcd6c75d7c

## What looked useful

Anchor+compressed filler consistently lowered full-attention L2 error relative to anchor-only sparse retention at the same exact-anchor set. With 16 anchors and chunk size 16 on 512-token synthetic sequences, the compressed cache averaged 47 tokens (10.89x reduction) and cut mean L2 error by about half versus anchor-only across anchor retrieval, filler competition, and distributed filler scenarios. Chunk sweeps showed a clear compression-fidelity tradeoff: chunk size 4 gave much lower error at 3.66x compression, while chunk size 64 reached 21.33x compression but approached anchor-only fidelity.

## Boundaries and scale limits

No real transformer evaluation, no learned anchor selector, no real long-context data, no perplexity or generation-quality metrics, and no serving-latency benchmark. Filler compression was simple mean pooling.

## Claim scope

Synthetic single-head attention probe with oracle target anchors: exact anchor retention plus mean-compressed filler reduced KV cache by 3.66x to 21.33x and improved approximation to full attention versus anchor-only and random-exact controls.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct model evidence; it should not be treated as paper-positive.

## Recommended next action

Run a bounded direct follow-up on a small pretrained transformer using real KV traces, comparing full KV, anchor-only, anchor+compressed filler, and standard eviction on perplexity and retrieval tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-KV on Real Small-Transformer KV Traces
- Success threshold: At a matched cache budget of at least 8x reduction versus full KV, anchor+compressed filler must reduce perplexity degradation by at least 25% versus anchor-only and preserve retrieval accuracy within 5 percentage points of full KV on the tested small-model workload.
- Stop condition: Stop if anchor+compressed filler is not better than anchor-only on either perplexity degradation or retrieval accuracy under matched cache budgets, or if implementation overhead prevents a fair cache-budget comparison.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-kv-exact-token-retention-with-compressed-filler-a47715bcc6e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
