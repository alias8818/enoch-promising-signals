# Confidence-Thresholded Two-Model Local Cascade on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-thresholded-two-model-local-cascade-on-gb10-956a529a43ad`
Run ID: `confidence-thresholded-two-model-local-cascade-on-gb10-956a529a43ad-20260619T050912261273+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/886dd2a97b95

## What looked useful

DistilBERT-to-RoBERTa-base at threshold 0.98 reached 0.9300 accuracy versus 0.9404 for RoBERTa-only and 0.9106 for DistilBERT-only, with estimated throughput 1156.6 examples/s versus 1101.2 for RoBERTa-only. Matching RoBERTa accuracy required threshold 0.999, 38.5% escalation, and estimated throughput 885.1 examples/s, making the cascade 24.4% slower than RoBERTa-only. Tiny-BERT-to-DistilBERT was also unattractive near large-model accuracy.

## Boundaries and scale limits

Tested only SST-2 sequence classification over 872 validation examples. Cascade latency is estimated from measured model throughput rather than direct request-level serving. This does not validate 7B+ generation, quantized local LLM serving, multi-turn assistant quality, or production batching.

## Claim scope

On GB10, full GLUE SST-2 validation with cached local Hugging Face classifiers showed that confidence-thresholded two-model cascades can create a bounded speed/accuracy tradeoff, but did not preserve the stronger model's accuracy while reducing latency.

## Why it stopped

Moderate direct classifier evidence found only a speed/accuracy tradeoff, not accuracy-preserving cascade acceleration; broader LLM-serving claims remain proxy-only.

## Recommended next action

Stop this run as a no-paper useful signal; a separate bounded follow-up should directly measure request-level local generative-model cascades with calibrated confidence if the research program wants to continue.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct request-level confidence cascade for local generative models on GB10
- Success threshold: At least 15% latency reduction versus large-only at no more than 1 percentage point quality loss on a fixed local benchmark with direct measured cascade serving.
- Stop condition: Stop if matching the quality threshold requires enough escalations that measured cascade latency is not at least 15% lower than large-only, or if confidence is too poorly calibrated to separate easy and hard cases.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-thresholded-two-model-local-cascade-on-gb10-956a529a43ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
