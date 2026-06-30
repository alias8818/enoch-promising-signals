# TernRes-LoRA tiny language-model confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternres-lora-tiny-language-model-confirmation-de86b8a4e3`
Run ID: `ternres-lora-tiny-language-model-confirmation-de86b8a4e3-20260628T080005757390+0000`

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

- Parent run decision: TernRes-LoRA: Ternary Weights with LoRA-Style Residual Adapters: enoch://control-plane/projects/ternres-lora-ternary-weights-with-lora-style-residual-adapters-7465077d0b01/runs/ternres-lora-ternary-weights-with-lora-style-residual-adapters-7465077d0b01-20260628T073112432279+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c84415f6acd

## What looked useful

TernRes-LoRA improved shifted-domain validation loss over the frozen base by 79.46% and beat post-hoc ternarized LoRA by 0.5272 nats, but remained 0.2239 nats worse than full-precision LoRA versus the predeclared <=0.05 nat threshold.

## Boundaries and scale limits

Synthetic token-transition data, tiny MLP LM, CPU-only local run, no natural-language corpus, no GPT-2-class Transformer, no deployment kernel benchmark, and no broad hyperparameter sweep.

## Claim scope

Three-seed synthetic tiny MLP next-token language-model adaptation test comparing frozen base, full-precision LoRA, post-hoc ternarized LoRA, and STE-trained TernRes-LoRA at matched rank and steps.

## Why it stopped

Direct Tier 1 tiny-LM test missed the full-precision LoRA closeness threshold while passing frozen-improvement and post-hoc-ternary controls.

## Recommended next action

Stop this run as no-paper Tier 1 evidence; if pursued, run a bounded deepen test of residual-corrected or rank-scheduled TernRes-LoRA that must close the <=0.05 nat loss gap on the same tiny LM and a small Transformer control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-corrected TernRes-LoRA loss-gap closure on tiny and small Transformer LMs
- Success threshold: Mean validation loss within 0.05 nats of full-precision LoRA, at least 25% improvement over frozen, at least 0.03 nats better than post-hoc ternary LoRA, and at least 4x adapter payload reduction.
- Stop condition: Stop as negative if the improved TernRes variant remains more than 0.05 nats worse than full-precision LoRA on either the tiny LM or small Transformer control across the planned seeds.

## Evidence references

- Artifact root: `<local-path>/projects/ternres-lora-tiny-language-model-confirmation-de86b8a4e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
