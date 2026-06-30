# Anchor+sliding KV compression on GPT-2-small 8k context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-sliding-kv-compression-on-gpt-2-small-8k-context-7dd024825e50`
Run ID: `anchor-sliding-kv-compression-on-gpt-2-small-8k-context-7dd024825e50-20260611T124123221094+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a0d9ea87e241

## What looked useful

The mechanism saves substantial KV memory, but the apparent 8k quality gain is likely due to dropping harmful far context from a position-extrapolated GPT-2 rather than preserving useful long-range information. A trained-range control falsifies a quality-preserving interpretation.

## Boundaries and scale limits

Small sample count, 64-token scoring windows, synthetic plus Wikitext only, no trained 8k GPT-2-small checkpoint, no anchor/window ablation, and no comparison against sliding-only or attention-based eviction baselines.

## Claim scope

On GPT-2-small with tiled absolute position embeddings, anchor+sliding KV retention with anchor=64 and window=512 reduced 8k-context KV cache memory by about 93% and improved NLL/throughput relative to retaining the full extrapolated 8k cache; however, inside GPT-2-small's trained context range the same policy worsened Wikitext NLL and top-1 accuracy.

## Why it stopped

Moderate direct evidence shows memory savings but mixed quality, including degradation in GPT-2-small's trained context range; the 8k positive result is a proxy/extrapolation artifact, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test is a bounded follow-up on an actually 8k-capable small causal LM with anchor/window ablations and sliding-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor+sliding KV retention on an 8k-capable small causal LM
- Success threshold: At 8k context, achieve at least 75% KV memory reduction with mean NLL no more than 5% worse than full cache and throughput not lower than full cache across the evaluated long-context documents.
- Stop condition: Stop if all anchor+sliding settings exceed 5% NLL degradation versus full cache or fail to outperform sliding-only at matched retained-token budget.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-sliding-kv-compression-on-gpt-2-small-8k-context-7dd024825e50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
