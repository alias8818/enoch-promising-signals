# Speculative decoding with 1-bit draft model and residual channel recovery on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-decoding-with-1-bit-draft-model-and-residual-channel-recovery-on-cpu-34e1bafb7c22`
Run ID: `speculative-decoding-with-1-bit-draft-model-and-residual-channel-recovery-on-cpu-34e1bafb7c22-20260524T224324341407+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c751095d5e83

## What looked useful

On CPU, weight-only 1-bit sign accumulation was not faster than dense FP32. W1A1 XNOR-popcount was fast but had only 6.8-7.3% top-1 agreement at medium scale without residuals. Residual-channel recovery improved agreement up to 21.1% at 2048x512 but reduced speed to 2.52x, yielding an optimistic gamma=4 speculative speed estimate of only 0.49x. At 4096x1024, 128 residual channels reached only 14.1% top-1 agreement while draft speed fell to parity with dense.

## Boundaries and scale limits

No real transformer, tokenizer, KV cache, prompt set, sampling acceptance, or end-to-end speculative decoding server was tested. Results are an early falsification of this mechanism proxy, not a full LLM validation.

## Claim scope

Synthetic CPU projection-level benchmark of 1-bit draft logits with residual-channel recovery, using top-1 agreement with a dense FP32 projection as a greedy speculative acceptance proxy.

## Why it stopped

Proxy-level early falsification: residual recovery improved agreement but did not preserve enough CPU speed advantage to make speculative decoding plausible under the tested synthetic projection conditions.

## Recommended next action

Stop this mechanism as a no-paper early falsification; only revisit with a real trained LLM draft where hidden-state/output-head structure can be measured against a 4-bit draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure 1-bit residual draft agreement on a real tiny language model
- Success threshold: At least 50% greedy acceptance or equivalent sampling overlap with an end-to-end CPU speculative speedup of at least 1.2x over the best non-speculative CPU baseline, while retaining a material speed advantage over a 4-bit draft.
- Stop condition: Stop if real-model top-1 agreement remains below 35% at any residual budget that keeps the draft at least 4x faster than target projection, or if end-to-end speculative throughput is not above baseline.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-1-bit-draft-model-and-residual-channel-recovery-on-cpu-34e1bafb7c22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
