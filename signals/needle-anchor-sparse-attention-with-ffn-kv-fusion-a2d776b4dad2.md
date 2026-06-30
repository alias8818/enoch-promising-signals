# Needle-Anchor Sparse Attention with FFN-KV Fusion

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `needle-anchor-sparse-attention-with-ffn-kv-fusion-a2d776b4dad2`
Run ID: `needle-anchor-sparse-attention-with-ffn-kv-fusion-a2d776b4dad2-20260529T090413366728+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/65c8d6114888

## What looked useful

When true distant needles were exposed through an FFN-like salience channel, sparse local+anchor attention recovered 100% of dense top-1 retrievals; local-only recovered 0.0%, random anchors 1.39%, and FFN anchors without salience 0.35%. This supports the anchor-selection mechanism but not an end-to-end architecture claim.

## Boundaries and scale limits

No trained Transformer, no natural-language loss, no custom fused kernel, no GPT-2-small-class baseline, and timings are Python-loop proxy timings rather than optimized kernel throughput.

## Claim scope

Synthetic long-context retrieval probe only: FFN-like salience anchor selection preserved distant needle top-1 retrieval while reading 2.35% to 9.3% of dense KV positions across 2048 to 8192 token traces.

## Why it stopped

Closed as no-paper useful signal because the run is a synthetic/proxy mechanism test, not full validation of FFN-KV fusion or model quality.

## Recommended next action

Run a bounded deepen follow-up with a small trained Transformer and parameter-matched dense baseline on synthetic and semi-natural long-context retrieval before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a small Transformer with FFN-salience KV anchors on long-context retrieval
- Success threshold: Sparse FFN-salience anchor model matches at least 95% of dense retrieval accuracy while reducing measured KV reads or memory traffic by at least 4x on 4096+ token contexts, with no more than 5% regression on non-needle examples.
- Stop condition: Stop if learned salience anchor coverage remains below 80% on held-out distant needles or if quality drops more than 5% versus the dense baseline after matched training budget.

## Evidence references

- Artifact root: `<local-path>/projects/needle-anchor-sparse-attention-with-ffn-kv-fusion-a2d776b4dad2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
