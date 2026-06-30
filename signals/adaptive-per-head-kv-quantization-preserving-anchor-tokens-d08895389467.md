# Adaptive Per-Head KV Quantization Preserving Anchor Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-per-head-kv-quantization-preserving-anchor-tokens-d08895389467`
Run ID: `adaptive-per-head-kv-quantization-preserving-anchor-tokens-d08895389467-20260529T134633471868+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a8589b716432

## What looked useful

Anchor preservation reduced 2-bit loss by 2.093, but adaptive_2_4_anchor had loss 6.951 versus fixed3_anchor loss 4.566 at the same 3.677 effective KV bits/element; reverse adaptive was also worse at loss 6.530.

## Boundaries and scale limits

Single model family member (gpt2), 12 short-context validation batches of 384 tokens, simulated quantization inside eager attention, no optimized serving kernel, no long-context autoregressive cache persistence, no 7B+ model validation.

## Claim scope

Bounded GPT-2-small/WikiText-2 inference probe: preserving first/recent anchor token K/V entries helps low-bit KV quantization, but the tested calibration-time reconstruction-error per-head 2/4-bit adaptive allocation is worse than uniform 3-bit at the same effective KV bit budget.

## Why it stopped

Bounded direct probe found the proposed adaptive per-head allocation rule underperforms a uniform fixed-bit baseline at equal bit budget, despite a positive anchor-preservation signal.

## Recommended next action

Stop this run as no-paper useful signal; if continued, replace reconstruction-error head ranking with direct loss or attention-output sensitivity and require it to beat fixed 3-bit anchors at matched effective KV bits before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct-sensitivity adaptive KV bit allocation under anchor preservation
- Success threshold: Adaptive policy must have validation loss no worse than fixed3_anchor by 0.05 and KL/token no worse than fixed3_anchor by 0.02 at matched effective KV bits on the same or larger GPT-2-small evaluation.
- Stop condition: Stop if direct-sensitivity adaptive allocation remains more than 0.10 loss worse than fixed3_anchor at matched effective KV bits on two independent validation slices.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-per-head-kv-quantization-preserving-anchor-tokens-d08895389467`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
