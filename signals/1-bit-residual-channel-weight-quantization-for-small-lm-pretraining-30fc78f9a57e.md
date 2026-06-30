# 1-bit residual-channel weight quantization for small LM pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-residual-channel-weight-quantization-for-small-lm-pretraining-30fc78f9a57e`
Run ID: `1-bit-residual-channel-weight-quantization-for-small-lm-pretraining-30fc78f9a57e-20260529T184753424870+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e63c8b435f0c

## What looked useful

Residual-channel 1-bit achieved mean validation loss 2.2639 versus 2.2996 for plain 1-bit and 2.1097 for dense across 3 seeds, recovering about 18.8% of the dense-vs-bit1 loss gap at about 14.8% of dense 2D-parameter linear-weight bits.

## Boundaries and scale limits

Toy character-level dataset, small Transformer, 2,000-step training horizon, no GPT-2-small-class model, no subword-tokenized corpus, no long convergence run, no packed 1-bit kernel or deployment memory measurement, and only one residual fraction tested.

## Claim scope

On a 2-layer 128-hidden TinyShakespeare character Transformer trained from scratch for 2,000 steps across 3 seeds, keeping 12.5% of each linear layer's output channels dense while quantizing the rest to 1-bit improves validation loss versus plain 1-bit STE training, but remains substantially worse than dense.

## Why it stopped

Bounded proxy evidence supports the residual-channel mechanism over plain 1-bit but does not validate the broader small-LM pretraining claim or close enough of the dense gap for a paper.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded residual-fraction sweep with a larger tokenizer-based small LM before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel fraction sweep for 1-bit small-LM pretraining
- Success threshold: At least one residual fraction improves mean validation loss over plain 1-bit by >=0.05 and recovers >=35% of the dense-vs-bit1 loss gap while using <=25% of dense linear-weight bits.
- Stop condition: Stop if no residual fraction beats plain 1-bit by >=0.02 mean validation loss across seeds or if the best fraction requires >25% dense linear-weight bits to reach the threshold.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-residual-channel-weight-quantization-for-small-lm-pretraining-30fc78f9a57e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
