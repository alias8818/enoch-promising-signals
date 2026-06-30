# Residual-Channel LoRA on a Frozen 2-bit Tiny Transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-lora-on-a-frozen-2-bit-tiny-transformer-b6900b5bea`
Run ID: `residual-channel-lora-on-a-frozen-2-bit-tiny-transformer-b6900b5bea-20260621T031822651737+0000`

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

- Parent run decision: Trainable Residual Channel LoRA on 2-bit Frozen Base: enoch://control-plane/projects/trainable-residual-channel-lora-on-2-bit-frozen-base-4a5eb53d3647/runs/trainable-residual-channel-lora-on-2-bit-frozen-base-4a5eb53d3647-20260621T025932013982+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc4ce748255b

## What looked useful

Residual-channel LoRA is a viable low-parameter adaptation mechanism for a frozen 2-bit tiny transformer in this direct small test, but the evidence supports only a bounded mechanism signal rather than a paper-ready architecture claim.

## Boundaries and scale limits

Tiny 3-layer transformer, synthetic modular next-token task, dequantized frozen 2-bit weights, short adaptation runs, no natural-language corpus, no GPT-2-small-class scale, no retention-preserving objective, and no deployment-kernel measurement.

## Claim scope

In a three-seed controlled synthetic modular-arithmetic adaptation test, residual-channel LoRA on a frozen 2-bit tiny transformer can learn a held-out stride with 4,608 trainable parameters, reducing frozen-base adaptation loss by 99.15% and reaching 100% token accuracy. It beats a parameter-near rank-1 standard LoRA baseline, but not a much larger rank-8 standard LoRA baseline.

## Why it stopped

Tier 1 direct test completed; result is useful but synthetic and mixed, with residual-channel LoRA trailing the larger rank-8 standard LoRA loss by 6.88x despite beating the parameter-near rank-1 baseline.

## Recommended next action

Run a medium parameter-matched language-modeling confirmation with residual-channel LoRA, standard LoRA, and dense adapter controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched residual-channel LoRA on a frozen 2-bit small language model
- Success threshold: Residual-channel LoRA must reduce frozen 2-bit validation loss by at least 20%, be within 10% of or better than parameter-matched standard LoRA validation loss, and preserve original-distribution loss no worse than the standard LoRA control.
- Stop condition: Stop as a no-paper negative if two or more seeds show residual-channel LoRA more than 10% worse than parameter-matched standard LoRA on validation loss or materially worse on retention after the matched update budget.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-lora-on-a-frozen-2-bit-tiny-transformer-b6900b5bea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
