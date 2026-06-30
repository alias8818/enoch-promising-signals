# Multi-dataset CPU text router cascade with representative local heavy model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-dataset-cpu-text-router-cascade-with-representative-9c66a4843f`
Run ID: `multi-dataset-cpu-text-router-cascade-with-representative-9c66a4843f-20260604T174400983137+0000`

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

- Parent run decision: Tiny Router Cascade for Local CPU Inference: enoch://control-plane/projects/tiny-router-cascade-for-local-cpu-inference-eab320b675c4/runs/tiny-router-cascade-for-local-cpu-inference-eab320b675c4-20260604T073219408888+0000
- Parent run decision: CPU Text Router Cascade With Real Local Runtime: enoch://control-plane/projects/cpu-text-router-cascade-with-real-local-runtime-05e1e63b48/runs/cpu-text-router-cascade-with-real-local-runtime-05e1e63b48-20260604T114731250975+0000

## What looked useful

Selected cascades achieved AG News accuracy 0.8701 vs heavy 0.8796 with 24.84% heavy use, SMS accuracy 0.9860 vs heavy 0.9862 with 1.00% heavy use, and TREC accuracy 0.8080 vs heavy 0.8153 with 39.40% heavy use. At matched heavy fractions, confidence routing beat random routing by +0.0357, +0.0016, and +0.0247 accuracy respectively, and inverted routing was worse on all datasets.

## Boundaries and scale limits

The heavy model was a local feature-rich CPU classifier, not a modern transformer or LLM-class model. Cascade latency was estimated from measured cheap and heavy prediction wall times rather than measured in a production serving stack. Results cover three small/medium public text classification datasets, not generative local-model workloads or distribution-shift robustness.

## Claim scope

Across AG News, SMS spam, and TREC with fixed seeds 13, 17, and 23, a cheap Naive Bayes confidence router feeding a heavier local CPU feature-rich Naive Bayes classifier preserved near-heavy accuracy while reducing heavy invocations by about 60% to 99%; matched random and inverted controls support cheap confidence as a useful routing signal.

## Why it stopped

Tier 2 bounded mechanism evidence is positive, but the representative-heavy-model claim is only partially satisfied because the heavy model is a feature-rich classifier rather than a modern local heavy model; this is not publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with the same fixed-seed threshold/control design using an actual local transformer or LLM-class CPU heavy model and end-to-end latency measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU text router cascade with actual local transformer heavy model
- Success threshold: For at least two of three datasets, cascade accuracy is within 1 percentage point of heavy-all or at least 99% of heavy-all accuracy, while invoking the heavy model on no more than 50% of examples and beating matched random routing by at least 1 percentage point where heavy and cheap accuracies differ materially.
- Stop condition: Stop as negative if an actual local heavy model is not materially more accurate than the cheap router on at least two datasets, or if no threshold can keep accuracy within 1 percentage point of heavy-all while reducing heavy invocations by at least 50%.

## Evidence references

- Artifact root: `<local-path>/projects/multi-dataset-cpu-text-router-cascade-with-representative-9c66a4843f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
