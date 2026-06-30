# INT2 weight quantization with learned residual channels for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weight-quantization-with-learned-residual-channels-for-gpt-2-small-90c4be0ef73f`
Run ID: `int2-weight-quantization-with-learned-residual-channels-for-gpt-2-small-90c4be0ef73f-20260619T032430372229+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4434a2c467db

## What looked useful

Raw INT2 projection quantization raised loss from dense 4.1765 to 37.1766. Learned top-energy residual channels improved loss to 14.6579 at 3% residual columns and 14.1385 at 10%, while random residual controls stayed much worse. The mechanism is real but insufficient for practical GPT-2-small compression in the tested form.

## Boundaries and scale limits

Main evaluation used 8192 next-token targets, 16 calibration sequences, 128-token context, simulated affine INT2, GPT-2 Conv1D projection weights only, scalar per-channel residual gates, and independent per-module calibration rather than full end-to-end quantization-aware training. Embeddings, LayerNorms, and LM head remained dense.

## Claim scope

Bounded GPT-2-small/WikiText-2 proxy: simulated per-output INT2 quantization of GPT-2 projection weights with learned residual output channels up to 10% does not recover usable language-model loss. Top-energy residual-channel selection improves raw INT2 and random residual controls, but remains far from dense GPT-2-small.

## Why it stopped

Bounded direct GPT-2-small proxy evidence shows residual-channel selection helps, but quality remains far below dense and not practically viable; this is not a full-scale validation and not paper-positive.

## Recommended next action

Stop this run as a no-paper useful signal; a next bounded test should replace naive affine INT2 with GPTQ/AWQ-style INT2 calibration and compare residual channels against same-bit-budget low-rank residuals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPTQ-calibrated INT2 residual channels versus same-bit low-rank residuals on GPT-2-small
- Success threshold: At a matched bit budget of no more than 5.2 average bits per quantized projection weight, top-energy residual channels must reduce WikiText-2 loss to within +1.0 nat of dense GPT-2-small and beat random and same-bit low-rank controls by at least 0.5 nat.
- Stop condition: Stop if activation-aware INT2 plus residual channels remains above 2x dense loss or fails to beat same-bit controls at two residual budgets.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weight-quantization-with-learned-residual-channels-for-gpt-2-small-90c4be0ef73f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
