# Self-speculative decoding via early-exit layer reuse on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-layer-reuse-on-gb10-9c32d5b1190e`
Run ID: `self-speculative-decoding-via-early-exit-layer-reuse-on-gb10-9c32d5b1190e-20260628T043414745187+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65b34aa17811

## What looked useful

Across 23,726 next-token positions, early top-1 agreement was low until very late layers. The best agreement was 54.84% at hidden state 11, costing 11/12 of the model. Earlier practical exits were far worse: hidden state 6 reached 14.29% top-1 agreement and hidden state 8 reached 22.85%. Under a favorable idealized cost model, no layer/draft-length pair reached break-even speedup.

## Boundaries and scale limits

This is a bounded local probe on GPT-2 small and Wikitext-2 validation text. It does not implement full speculative serving, does not test larger LLMs, and does not test trained early-exit heads or acceptance schemes beyond top-1 agreement.

## Claim scope

On GPT-2 small fp16 running on NVIDIA GB10, reusing intermediate hidden states with the existing final LM head as early-exit draft logits produced insufficient top-1 agreement for self-speculative decoding; the best idealized speedup proxy was 0.300x, below break-even.

## Why it stopped

Proxy/early falsification rather than full validation: the directly tested early-logit agreement was too low, and the favorable speedup proxy stayed below break-even.

## Recommended next action

Stop the reuse-only final-head variant as no-paper evidence; the concrete next bounded test is to train a lightweight early-exit head and require layer <=8 to reach at least 55% top-1 agreement with an idealized speedup proxy above 1.15x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train calibrated early-exit heads for GPT-2 small self-speculative drafting
- Success threshold: Layer 8 or earlier reaches at least 55% top-1 agreement and a measured or strictly modeled speedup above 1.15x while preserving exact greedy output under verification.
- Stop condition: Stop if trained heads at layer 8 or earlier stay below 45% top-1 agreement or if measured speculative latency is not faster than cached greedy decoding after verification overhead.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-layer-reuse-on-gb10-9c32d5b1190e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
