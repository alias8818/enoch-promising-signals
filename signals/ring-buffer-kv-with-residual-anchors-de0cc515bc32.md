# Ring-Buffer KV with Residual Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ring-buffer-kv-with-residual-anchors-de0cc515bc32`
Run ID: `ring-buffer-kv-with-residual-anchors-de0cc515bc32-20260608T042240704259+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

Old anchors can recover long-range retrieval lost by a smaller ring-only cache, but residual-novelty anchor selection did not produce a robust advantage over equal-budget sliding windows, uniform anchors, reservoir anchors, or norm anchors.

## Boundaries and scale limits

No real transformer KV-cache integration, language-model perplexity, generation quality, or GPU decode benchmark was run. Evidence is bounded to synthetic attention approximation and retrieval probes on a CPU worker.

## Claim scope

On synthetic long-context attention traces with sequence length 512, dimension 64, a 64-token recent ring plus residual-novelty anchors improves over a smaller 64-token ring but is not consistently better than an equal-total-cache sliding window or simple anchor controls.

## Why it stopped

Proxy synthetic evidence is mixed and does not validate the residual-anchor mechanism as better than simpler equal-budget baselines.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should patch residual and uniform anchors into a small GPT-2-class KV cache and compare perplexity, long-context retrieval tasks, and decode overhead against an equal-budget sliding window.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small GPT-2 KV-cache residual-anchor validation
- Success threshold: Residual anchors must improve long-context perplexity or retrieval accuracy by at least 5% relative to equal-budget sliding window while adding no more than 10% decode latency overhead, and must beat uniform anchors on the primary metric.
- Stop condition: Stop if residual anchors fail to beat equal-budget sliding window and uniform anchors on either perplexity or retrieval accuracy after one small-model corpus/task run.

## Evidence references

- Artifact root: `<local-path>/projects/ring-buffer-kv-with-residual-anchors-de0cc515bc32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
