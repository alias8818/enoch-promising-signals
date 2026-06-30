# Self-Speculative Decoding via Early-Exit Draft on Shared Weights

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `self-speculative-decoding-via-early-exit-draft-on-shared-weights-8da54f3f587f`
Run ID: `self-speculative-decoding-via-early-exit-draft-on-shared-weights-8da54f3f587f-20260527T132654710640+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6b0b50c36b43

## What looked useful

Auxiliary-trained exits reached 77.5%-83.3% early/final top-1 agreement and 2.90-3.15 emitted tokens per verify for gamma=4. Exit 1 and 2 had modeled speedups of 1.739x and 1.273x, while smoke and no-aux controls stayed near random agreement and below 1.0x.

## Boundaries and scale limits

Toy synthetic data only; 6-layer 192-wide transformer; greedy draft/verify only; no natural text, pretrained LLM, KV-cache serving path, sampling quality, or production wall-clock tokens/sec validation.

## Claim scope

In a compact synthetic-language causal transformer, explicitly trained auxiliary early-exit heads on shared weights can draft greedy tokens that the final head accepts often enough for a shallow-exit cost model to exceed greedy final-only decoding.

## Why it stopped

No-paper closure: the local toy evidence supports the mechanism but is not direct enough for a real LLM serving claim or paper-positive decision.

## Recommended next action

Run a bounded GPT-2-small-class follow-up on real text with trained early exits, final perplexity impact, greedy/sampling acceptance, and actual KV-cache tokens/sec versus an external draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-Small Early-Exit Self-Speculation With KV-Cache Timing
- Success threshold: Final perplexity degradation <=2%, actual greedy decoding throughput >=1.15x over final-only decoding, and no worse throughput/quality tradeoff than an external small draft baseline at comparable cost.
- Stop condition: Stop if best real-corpus exit has <60% top-1 agreement, <1.05x actual KV-cache throughput, or >2% final perplexity degradation after calibrated auxiliary-head training.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-on-shared-weights-8da54f3f587f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
