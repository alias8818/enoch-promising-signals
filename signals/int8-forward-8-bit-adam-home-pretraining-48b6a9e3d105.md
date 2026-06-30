# Int8 Forward 8-Bit Adam Home Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-forward-8-bit-adam-home-pretraining-48b6a9e3d105`
Run ID: `int8-forward-8-bit-adam-home-pretraining-48b6a9e3d105-20260607T193112574910+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f3795769f29a

## What looked useful

Int8-forward linear projections alone matched the AdamW baseline validation loss (2.3433 vs 2.3430), while simple per-tensor 8-bit Adam reduced optimizer state to 25% of baseline but destabilized the combined recipe, reaching validation losses above 1500.

## Boundaries and scale limits

This is a small local pretraining proxy. It does not test fused int8 GEMM kernels, production blockwise 8-bit Adam, GPT-2-small-class scaling, tokenizer-scale corpora, or long-run convergence.

## Claim scope

On a 1.8M-parameter character-level causal LM trained for 300 steps on Tiny Shakespeare with CUDA on GB10, fake-int8 linear forward projections were stable with AdamW, but the combined fake-int8-forward plus simple per-tensor 8-bit Adam state recipe diverged at both 3e-4 and 3e-5 learning rates.

## Why it stopped

Moderate local proxy evidence falsified the naive combined int8-forward plus per-tensor 8-bit Adam recipe; this is not a full-scale validation, but the divergence is strong enough to avoid scaling this exact design.

## Recommended next action

Stop this recipe as not paper-ready; the concrete next bounded test is replacing per-tensor 8-bit Adam with a blockwise/clipped stable optimizer and requiring combined int8-forward training to stay within 10% of AdamW validation loss for 1000 small-LM steps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise stable 8-bit Adam under int8-forward LM training
- Success threshold: Combined int8-forward plus blockwise 8-bit Adam validation loss within 10% of baseline AdamW after 1000 steps, with optimizer state no more than 35% of AdamW state bytes and no loss spike above 2x baseline after step 100.
- Stop condition: Stop if the combined variant diverges twice under documented learning-rate settings or if optimizer state exceeds 50% of AdamW state bytes without a compensating stability benefit.

## Evidence references

- Artifact root: `<local-path>/projects/int8-forward-8-bit-adam-home-pretraining-48b6a9e3d105`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
