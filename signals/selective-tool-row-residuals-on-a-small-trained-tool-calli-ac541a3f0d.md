# Selective Tool-Row Residuals on a Small Trained Tool-Calling Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `selective-tool-row-residuals-on-a-small-trained-tool-calli-ac541a3f0d`
Run ID: `selective-tool-row-residuals-on-a-small-trained-tool-calli-ac541a3f0d-20260602T222032314656+0000`

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

- Parent run decision: Selective FP16 Residuals for Agent Tool-Calling Heads: enoch://control-plane/projects/selective-fp16-residuals-for-agent-tool-calling-heads-93a67087c4d0/runs/selective-fp16-residuals-for-agent-tool-calling-heads-93a67087c4d0-20260602T180645259129+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/878afbbb9b2b

## What looked useful

Tool-row residuals can be sufficient to redirect learned tool-token routing when the base model already encodes the request, but row selectivity alone did not improve old-routing retention over dense fine-tuning in this conflicting remap setup.

## Boundaries and scale limits

The result is limited to a synthetic single-turn dataset, a toy transformer, four tool tokens, three seeds, and a conflicting remap. It does not validate real tool-calling corpora, GPT-2-small-class or larger pretrained models, multi-turn conversations, context-gated adapters, or retention under broader distributions.

## Claim scope

On a synthetic trained small causal transformer tool-calling task with held-out requests and a weather/search remap, residual updates restricted to the four tool-token LM-head rows matched dense fine-tuning on adapted tool-call accuracy and response exactness, while an equal-size non-tool-row residual control stayed at the no-adaptation baseline.

## Why it stopped

No-paper closure: the Tier 1 direct synthetic test supports the routing mechanism but is narrow, synthetic, and mixed because base routing retention was not better than dense fine-tuning.

## Recommended next action

Run a bounded deepen follow-up testing context-gated or regularized tool-row residuals on non-conflicting new-tool additions and conflicting remaps, with retention improvement over dense fine-tuning as a required metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Context-Gated Tool-Row Residuals for Tool Routing Without Retention Loss
- Success threshold: Gated or regularized tool-row residuals must reach at least 95% adapted response exactness, beat non-tool-row controls by at least 20 percentage points, and improve base tool retention by at least 20 percentage points over dense fine-tuning on conflicting remaps.
- Stop condition: Stop if gated or regularized tool-row residuals fail to beat dense fine-tuning base retention by at least 10 percentage points while matching adapted accuracy in a three-seed pilot.

## Evidence references

- Artifact root: `<local-path>/projects/selective-tool-row-residuals-on-a-small-trained-tool-calli-ac541a3f0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
