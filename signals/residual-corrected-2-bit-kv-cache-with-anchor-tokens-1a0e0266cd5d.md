# Residual-Corrected 2-Bit KV Cache with Anchor Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-corrected-2-bit-kv-cache-with-anchor-tokens-1a0e0266cd5d`
Run ID: `residual-corrected-2-bit-kv-cache-with-anchor-tokens-1a0e0266cd5d-20260526T064301036597+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f3b0287cf4b3

## What looked useful

Exact anchor tokens consistently reduced 2-bit KV attention-output relative L2 error on distilgpt2 by 25.14%-33.35% versus plain 2-bit. The residual-corrected variant improved over plain only by 3.58%-20.25% and was worse than exact anchors alone in all 9 stride/window settings, so the residual component is not supported as an additive mechanism.

## Boundaries and scale limits

No packed kernel, latency, memory-bandwidth, perplexity, long-context, or 7B+ validation; residual method is a simple nearest-anchor estimator rather than a learned/gated correction.

## Claim scope

Bounded local reconstruction and attention-output probe on synthetic KV tensors and distilgpt2 KV activations from fixed prompts; tests plain 2-bit, exact anchor tokens, and nearest-anchor residual correction.

## Why it stopped

No-paper useful signal: this bounded direct/proxy probe supports exact anchors but early-falsifies the tested residual-correction rule as an additive improvement over anchors alone.

## Recommended next action

Stop the paper path for nearest-anchor residual correction; if continuing, run a bounded gated-residual follow-up that must beat exact anchors alone at matched storage budget on dataset-level GPT-2-small metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated Residual Correction Versus Exact Anchors at Matched KV Budget
- Success threshold: Gated residual correction improves attention-output relative L2 and dataset next-token loss versus exact anchors alone by at least 5% relative at matched storage budget in at least 2 of 3 anchor densities, with no density worse than exact anchors.
- Stop condition: Stop if residual correction fails to beat exact anchors alone on either attention-output relative L2 or dataset next-token loss in the first two anchor densities.

## Evidence references

- Artifact root: `<local-path>/projects/residual-corrected-2-bit-kv-cache-with-anchor-tokens-1a0e0266cd5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
