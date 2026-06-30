# Layer-Skip Self-Distillation Spec Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layer-skip-self-distillation-spec-decoding-d6c3921a3c43`
Run ID: `layer-skip-self-distillation-spec-decoding-d6c3921a3c43-20260628T093631266797+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e49079f54af2

## What looked useful

Corrected 3000-step paired run: baseline final_acc=0.7182, LayerSkip final_acc=0.7148; exit2 top-1 agreement improved 0.7066 -> 0.9159; exit2 four-token accept proxy improved 0.5383 -> 0.8005; exit2 k=4 cost-proxy speedup improved 1.3514x -> 1.8009x. Exits 3 and 4 also improved agreement and speed proxies.

## Boundaries and scale limits

Synthetic data, small model, greedy/top-1 agreement proxies, no real tokenizer/corpus, no saved checkpoint rerun, no distribution-preserving speculative sampler, and no direct wall-clock self-speculative decoding benchmark on a production LLM.

## Claim scope

On a controlled 1.0M-parameter, 6-layer toy decoder trained on synthetic next-token data, a LayerSkip-style objective with shared-head early losses, self-distillation KL, and increasing layer dropout substantially improved early-exit top-1 agreement and conservative self-speculative acceptance/cost proxies while preserving final accuracy within 0.35 percentage points of a final-loss baseline.

## Why it stopped

No-paper closure: local mechanism evidence is useful, but this run only used a toy synthetic proxy and did not directly validate lossless speculative decoding on a real language model/corpus.

## Recommended next action

Run a bounded direct follow-up on a GPT-2-small-class model and real text, saving checkpoints and measuring exact self-speculative decoding acceptance plus wall-clock latency against autoregressive decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2-small LayerSkip self-speculative decoding benchmark
- Success threshold: LayerSkip preserves validation perplexity within 5% of baseline and achieves at least 1.25x measured decoding throughput at an exit layer with exact acceptance above 70% on held-out real text.
- Stop condition: Stop if LayerSkip hurts validation perplexity by more than 10%, exact acceptance stays below 50% at all exits, or measured self-speculative decoding is slower than autoregressive decoding after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-self-distillation-spec-decoding-d6c3921a3c43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
