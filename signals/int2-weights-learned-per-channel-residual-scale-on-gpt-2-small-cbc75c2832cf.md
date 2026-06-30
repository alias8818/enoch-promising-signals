# INT2 weights + learned per-channel residual scale on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weights-learned-per-channel-residual-scale-on-gpt-2-small-cbc75c2832cf`
Run ID: `int2-weights-learned-per-channel-residual-scale-on-gpt-2-small-cbc75c2832cf-20260621T082432061871+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ad6e7f5c06bf

## What looked useful

Learned scales improved fixed INT2 by 1.2160 nats/token, but learned-scale INT2 loss was still 7.8417 versus FP32 loss 3.7966. The mechanism helps but this simple scalar-only residual scale is not viable as a paper-ready GPT-2-small INT2 method.

## Boundaries and scale limits

8 calibration blocks, 24 optimizer steps, 8 validation blocks, 1016 eval tokens; embeddings and tied lm_head left unquantized; no full WikiText-2 run, no GPTQ/AWQ baseline, no repeated seeds, no downstream generation evaluation.

## Claim scope

Bounded CPU probe on GPT-2-small projection modules: learned per-output-channel scale multipliers partially recover fixed signed INT2 per-channel quantization loss on a 1016-token WikiText-2 validation subset, but remain far worse than FP32.

## Why it stopped

Direct bounded probe found partial recovery but large residual degradation versus FP32, so the original simple hypothesis is not supported strongly enough for paper writing.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should compare the same learned-scale idea against activation-aware INT2 baselines on full WikiText-2 validation before spending larger compute.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT2 GPT-2-small scale-learning comparison
- Success threshold: Learned-scale activation-aware INT2 closes at least 50% of the fixed-INT2-to-FP32 loss gap and keeps final validation loss within 1.0 nat/token of FP32 on full WikiText-2 validation.
- Stop condition: Stop if learned scales improve fixed INT2 by less than 20% of the loss gap after the planned calibration budget or if full validation remains more than 2.0 nats/token worse than FP32.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weights-learned-per-channel-residual-scale-on-gpt-2-small-cbc75c2832cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
