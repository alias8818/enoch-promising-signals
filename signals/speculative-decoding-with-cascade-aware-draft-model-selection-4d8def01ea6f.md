# Speculative Decoding with Cascade-Aware Draft Model Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-cascade-aware-draft-model-selection-4d8def01ea6f`
Run ID: `speculative-decoding-with-cascade-aware-draft-model-selection-4d8def01ea6f-20260529T100311328159+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/39de4d2c5a52

## What looked useful

Cascade-aware draft selection has a bounded mechanism signal: the selector beat the best fixed draft by 0.67% at k=8 and 1.34% at k=16 with bootstrap lower bounds above zero, while k=4 showed no gain. The oracle gap indicates more routing signal remains, but the current evidence is not paper-ready.

## Boundaries and scale limits

Synthetic categorical target/draft distributions only; no real LLM logits, no live serving latency, no KV-cache or batching effects, no tokenizer/model-family robustness, and no GPU inference benchmark.

## Claim scope

In a reproducible synthetic speculative-decoding simulator with fixed target block cost, per-token draft costs, and held-out train/test contexts, an entropy-binned draft selector improves tokens per cost over the best fixed draft for k=8 and k=16, but not for k=4.

## Why it stopped

Stopped after a synthetic mechanism probe because it provides useful no-paper evidence but lacks direct LLM serving validation; this is not a full validation.

## Recommended next action

Run a bounded real-model follow-up using small target/draft LMs to collect actual logits, acceptance rates, and wall-clock latency for fixed drafts, entropy/routing selectors, and an oracle upper bound.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model cascade-aware draft selection trace benchmark
- Success threshold: Selector improves measured tokens/sec or tokens per target-call-equivalent by at least 3% over the best fixed draft at k=8 or k=16, with bootstrap p05 relative delta above zero and no regression greater than 1% at k=4.
- Stop condition: Stop if the selector fails to beat the best fixed draft on real-model traces for both k=8 and k=16, or if routing overhead exceeds the measured throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-cascade-aware-draft-model-selection-4d8def01ea6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
