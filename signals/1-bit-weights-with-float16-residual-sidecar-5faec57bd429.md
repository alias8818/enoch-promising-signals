# 1-bit weights with float16 residual sidecar

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-weights-with-float16-residual-sidecar-5faec57bd429`
Run ID: `1-bit-weights-with-float16-residual-sidecar-5faec57bd429-20260525T224551499557+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/85f01aa3b2bb

## What looked useful

Across three seeds, dense validation loss/token accuracy averaged 0.452/0.873. A 35% residual sidecar used 7.60 bits/weight, about 2.11x compression versus fp16, but still had loss 1.011 and token accuracy 0.686. A high-sidecar probe recovered near-dense quality only at 80% residuals, 14.80 bits/weight and about 1.08x compression.

## Boundaries and scale limits

Toy/local deterministic corpus, small Transformer, post-training quantization only, no pretrained GPT-2-small-class baseline, no quantization-aware training, no production kernel or speed measurement.

## Claim scope

For a locally trained small character-level causal Transformer, simple post-training tensorwise 1-bit sign weights plus a sparse fp16 top-k residual sidecar improves monotonically with sidecar size but does not preserve dense quality at meaningful fp16 compression.

## Why it stopped

Proxy/local early falsification: the residual sidecar mechanism helps, but post-training recovery is not strong enough at useful compression; this is not full large-model validation.

## Recommended next action

Stop this post-training version as no-paper useful negative evidence; the only bounded next test worth running is quantization-aware training or distillation with the same storage budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware training for 1-bit weights with sparse fp16 residual sidecar
- Success threshold: At <=8 bits/weight, quantization-aware sidecar model is within 10% relative validation loss and within 3 percentage points token accuracy of the dense model across at least three seeds.
- Stop condition: Stop if QAT/distillation remains more than 20% worse in validation loss or more than 8 percentage points worse in token accuracy at <=8 bits/weight after a bounded local training sweep.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-float16-residual-sidecar-5faec57bd429`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
