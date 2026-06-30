# Per-Head KV Quantization for Multi-Turn Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-kv-quantization-for-multi-turn-local-agents-f742ecbc205e`
Run ID: `per-head-kv-quantization-for-multi-turn-local-agents-f742ecbc205e-20260604T195315379343+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae645af88749

## What looked useful

Per-head bit allocation appears objective-dependent: it can help downstream NLL under an equal average bit budget, but uniform 4-bit better preserves the FP logit distribution in this probe.

## Boundaries and scale limits

Single small GPT-2-class model; synthetic deterministic prompts; one calibrated split; dequantized quantization simulation without packed-cache kernels, latency, bandwidth, memory-pressure, real agent traces, or instruction-tuned local-agent models.

## Claim scope

On a distilgpt2 synthetic multi-turn cache-only benchmark, sensitivity-ranked mixed per-head KV quantization at an average 4-bit budget improved target-continuation NLL versus uniform 4-bit, but worsened KL divergence and top-1 flip rate against FP logits.

## Why it stopped

Closed as no-paper useful signal: small direct cache probe is mixed and insufficient for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up on one small instruction-tuned local model with real or semi-real multi-turn traces and separate NLL-optimized versus KL-optimized per-head allocation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Objective-specific per-head KV allocation on small instruction-tuned multi-turn traces
- Success threshold: NLL-ranked per-head allocation improves held-out NLL by at least 2 percent over uniform 4-bit while KL-ranked allocation matches or improves uniform 4-bit KL/top-1 flips at the same average bit budget.
- Stop condition: Stop if per-head allocation fails to beat uniform 4-bit on both downstream NLL and FP-logit preservation across the instruction-tuned trace evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-quantization-for-multi-turn-local-agents-f742ecbc205e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
