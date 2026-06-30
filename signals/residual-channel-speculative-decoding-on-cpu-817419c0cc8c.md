# Residual-Channel Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-speculative-decoding-on-cpu-817419c0cc8c`
Run ID: `residual-channel-speculative-decoding-on-cpu-817419c0cc8c-20260604T152151107807+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5996c637976a

## What looked useful

Raw residual-channel subsets were not viable: high-recall settings required 384/768 channels and were slower than full dense logits. An optimistic SVD-rotated basis reached 0.961 top-8 recall with 1.28x logit speedup at vocab 8192 but fell to 0.908 top-8 recall at vocab 32768, below the success threshold.

## Boundaries and scale limits

Does not test real pretrained transformer residual activations, autoregressive decoding, verifier acceptance, KV-cache interactions, or end-to-end tokens per second.

## Claim scope

NumPy CPU proxy benchmark of reduced residual-channel LM-head logits on synthetic dense hidden states and vocabularies of 8192 and 32768 tokens.

## Why it stopped

Proxy evidence early-falsifies naive raw residual-channel drafting on CPU and leaves only a mixed learned-basis signal that is not publication-grade without direct real-model acceptance and end-to-end throughput evidence.

## Recommended next action

Stop this proxy run; run a bounded real-model follow-up on GPT-2-small-class residual activations comparing learned rotated-channel drafts against greedy decode and a small-draft speculative baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model residual-channel draft acceptance on CPU
- Success threshold: At least 95% full-top-token recall inside draft top-8, at least 80% verifier acceptance under the chosen decoding rule, and at least 1.25x end-to-end CPU tokens/s versus full decode without losing output equivalence for deterministic decoding.
- Stop condition: Stop if held-out real residual activations require more than half the residual width for 95% top-8 recall or if end-to-end CPU throughput is not at least 1.10x after including draft overhead.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-speculative-decoding-on-cpu-817419c0cc8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
