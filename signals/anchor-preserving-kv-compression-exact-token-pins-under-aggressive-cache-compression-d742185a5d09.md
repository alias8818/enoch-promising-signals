# Anchor-Preserving KV Compression: Exact-Token Pins Under Aggressive Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserving-kv-compression-exact-token-pins-under-aggressive-cache-compression-d742185a5d09`
Run ID: `anchor-preserving-kv-compression-exact-token-pins-under-aggressive-cache-compression-d742185a5d09-20260621T111712228913+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8350c477ab3d

## What looked useful

Exact-token pins are strongly beneficial when the pinned token is truly high-salience for the current query, but the sensitivity sweep shows they should be gated by salience or task-derived anchor rules rather than applied blindly.

## Boundaries and scale limits

No real pretrained LLM, no generation quality metric, no production KV kernel, no tokenizer-specific anchor detector, no layerwise transformer dynamics, and no latency/memory benchmark beyond synthetic effective slot counts. Weak or diffuse anchors did not benefit and sometimes had worse full-output fidelity than pooled non-pin compression.

## Claim scope

Synthetic attention-level KV compression probe with sequence length 2048, dimension 64, four known anchor tokens, chunk-mean compression for unpinned tokens, and exact K/V preservation for selected pins. Exact anchor pins preserve full-attention output fidelity for high-salience anchor-addressed queries under 0.6%-12.7% effective cache slots.

## Why it stopped

Synthetic proxy evidence supports the mechanism only for high-salience anchors and falsifies any broad claim that exact pins are universally beneficial under aggressive KV compression.

## Recommended next action

Stop this run as a proxy useful-signal result; next run should test the same pinning rule inside a small pretrained transformer on a needle/structured-anchor long-context task with attention diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of salience-gated exact KV anchor pins
- Success threshold: At the same effective KV slot budget, salience-gated exact pins improve target accuracy or target log-likelihood by at least 10% relative over compressed non-pin baselines on high-salience prompts, without degradation on weak-anchor controls.
- Stop condition: Stop if exact pins do not outperform the best same-budget non-pin baseline on high-salience prompts or if gains disappear after controlling for attention mass and recency.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-kv-compression-exact-token-pins-under-aggressive-cache-compression-d742185a5d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
