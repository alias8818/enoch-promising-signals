# Cascade-Aware Dynamic Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-aware-dynamic-speculative-decoding-d90bf2c57f86`
Run ID: `cascade-aware-dynamic-speculative-decoding-d90bf2c57f86-20260602T120213569938+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/250464260a3e

## What looked useful

Model-based state inference from acceptance histories was consistently better than best fixed gamma in the simulator (+1.14% to +13.70% paired mean improvement), while a simple streak heuristic was brittle. Real small-model acceptance traces showed positive lag-1 acceptance autocorrelation for fixed gamma values, supporting a bounded direct scheduler follow-up.

## Boundaries and scale limits

Simulator uses assumed Markov acceptance regimes and cost model; direct probe uses 12 prompts, GPT-2-class models, greedy decoding, and serial verifier calls rather than a production batched speculative decoding kernel.

## Claim scope

Simulator evidence shows that a Bayesian/HMM-style cascade-aware speculative decoding scheduler can improve simulated tokens-per-cost over the best fixed draft length across four controlled cascade regimes; a small real distilgpt2-to-gpt2 probe shows local acceptance clustering but does not validate real serving throughput.

## Why it stopped

No-paper closure: current positive evidence is mostly simulator-based, and the real model probe only validates acceptance clustering, not production-quality speculative decoding speedup.

## Recommended next action

Run a bounded direct implementation with batched target verification and a learned/calibrated HMM cascade scheduler on cached GPT-2-class or SmolLM-class model pairs, comparing paired wall-clock tokens/s against best fixed gamma and EWMA.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched real-model validation of HMM cascade-aware speculative decoding
- Success threshold: HMM cascade policy improves paired wall-clock tokens/s by >=5% over the best fixed gamma with a 95% bootstrap confidence interval excluding 0, while producing identical greedy target outputs.
- Stop condition: Stop if HMM policy overhead or misclassification makes paired wall-clock tokens/s <= best fixed gamma, or if acceptance traces show no positive local clustering on the tested real model pair.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-aware-dynamic-speculative-decoding-d90bf2c57f86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
