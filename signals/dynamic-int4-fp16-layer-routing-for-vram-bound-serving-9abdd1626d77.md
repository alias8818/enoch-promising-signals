# Dynamic int4-fp16 layer routing for VRAM bound serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-int4-fp16-layer-routing-for-vram-bound-serving-9abdd1626d77`
Run ID: `dynamic-int4-fp16-layer-routing-for-vram-bound-serving-9abdd1626d77-20260608T144613775352+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5936459271af

## What looked useful

Layer sensitivity routing produced a small matched-domain quality benefit at a moderate FP16 budget, but the result was brittle: it failed on tighter budget and cross-domain calibration, and the naive int4 path was slower than all-FP16.

## Boundaries and scale limits

Small 6-block model only; deterministic short WikiText windows; modeled block-weight memory rather than actual packed VRAM residency; naive PyTorch dequantization rather than fused int4 serving kernels; no 7B+ model, long-context, production traffic, or multi-corpus robustness validation.

## Claim scope

On distilgpt2 with block-level int4 Conv1D quantization and WikiText evaluation, matched-domain sensitivity routing slightly beat positional/random baselines at a 3-of-6 FP16 block budget, but not at 2-of-6 and not under cross-domain calibration.

## Why it stopped

Bounded local evidence is mixed and does not support a publication-grade or serving-speed claim; it is useful only as an early falsification of broad dynamic routing claims and as a guide for a narrower follow-up.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use multiple calibration/evaluation corpora and an actual packed or fused int4 implementation before any larger serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust calibrated layer routing with packed int4 kernels across corpora
- Success threshold: Routing beats the best positional baseline and random mean at 2-of-6 and 3-of-6 equivalent FP16 budgets on at least two held-out corpora while preserving at least 95% of all-FP16 throughput under the measured memory budget.
- Stop condition: Stop if routed placement fails to beat the best positional baseline on two corpus pairings or if packed int4 throughput remains below all-FP16 without a compensating memory-fit scenario.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-int4-fp16-layer-routing-for-vram-bound-serving-9abdd1626d77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
