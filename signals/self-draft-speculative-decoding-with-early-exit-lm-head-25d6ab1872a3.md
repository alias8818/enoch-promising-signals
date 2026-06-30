# Self-draft speculative decoding with early-exit LM head

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-draft-speculative-decoding-with-early-exit-lm-head-25d6ab1872a3`
Run ID: `self-draft-speculative-decoding-with-early-exit-lm-head-25d6ab1872a3-20260525T004531037498+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4c3c71d5549d

## What looked useful

Early-exit head agreement is low for tied heads (layer 9: 31.4%) and improves with distillation (layer 9: 52.4%, layer 6: 32.7%), but the best favorable speed model remains below baseline at 0.871x for layer 9 and 0.885x for layer 6.

## Boundaries and scale limits

Evidence is limited to GPT-2 small, WikiText-2 subsets, greedy top-1 agreement, one-epoch auxiliary-head distillation, and analytical speed modeling rather than a full KV-cache serving implementation or 7B+ models.

## Claim scope

On pretrained GPT-2 small with WikiText-2, tied early-exit heads and briefly distilled layer-6/layer-9 LM heads do not provide enough final-head agreement to make self-draft speculative decoding faster than plain greedy decoding under a favorable analytical speed model.

## Why it stopped

Bounded GPT-2 evidence is an early negative for speedup: even with favorable verifier-token accounting and ideal parallel verification, observed acceptance/agreement is too low to beat the baseline. This is not a full-scale negative proof for larger models.

## Recommended next action

Stop this run as no-paper useful signal; only revisit with a bounded real-latency follow-up that trains an acceptance-aware early head and demonstrates at least 1.05x measured greedy decoding speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Acceptance-aware early-exit head with real KV-cache self-draft latency
- Success threshold: At least 1.05x measured tokens/sec over plain GPT-2 greedy decoding on held-out prompts with identical greedy output and layer <= 6 average draft cost.
- Stop condition: Stop if validation top-1 agreement remains below 50% for layer <= 6 or if measured self-draft throughput is <= 1.0x after KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/self-draft-speculative-decoding-with-early-exit-lm-head-25d6ab1872a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
