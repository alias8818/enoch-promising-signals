# Medium Text Benchmark for Entropy-Routed Local Model Cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-text-benchmark-for-entropy-routed-local-model-casca-f17e689242`
Run ID: `medium-text-benchmark-for-entropy-routed-local-model-casca-f17e689242-20260527T023903966871+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Entropy-Routed Local Model Cascade: enoch://control-plane/projects/entropy-routed-local-model-cascade-61953b0579e5/runs/entropy-routed-local-model-cascade-61953b0579e5-20260524T194219125923+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a9550f8d4233

## What looked useful

Across five seeds, small-only accuracy averaged 0.5621, strong-only 0.6438, and the best <=25% entropy-routed cascade 0.5918. The cascade gained 0.0297 accuracy over small-only and 0.0094 over random routing at the same route fraction, with 1.47x estimated speedup versus strong-only. Entropy detected small-model errors with AUC 0.7599.

## Boundaries and scale limits

Five 6k-train/2k-test subset runs on one dataset family; no decoder LLMs, no GPU serving path, no production latency model, no distribution-shift test, and no learned-router baseline.

## Claim scope

On 20 Newsgroups medium-length documents with local classical text classifiers, normalized entropy from a cheap small model is a useful router: routing the highest-entropy 25% of examples to a stronger local model improved mean accuracy over small-only and random routing while preserving a measured speed advantage over strong-only inference.

## Why it stopped

Tier 1 direct evidence supports the routing mechanism but is not publication-grade because it uses classical classifiers on one benchmark family and the 25% cascade remains 5.2 accuracy points behind strong-only inference.

## Recommended next action

Stop this run as no-paper useful signal; deepen with local transformer or quantized local LLM cascades on at least two medium-text datasets and compare entropy routing against margin routing and a learned lightweight router.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Medium-Text Entropy Cascade With Router Controls
- Success threshold: At <=35% strong-model calls, entropy routing must recover at least 50% of the small-to-strong accuracy gap, beat random routing by at least 1.0 accuracy point, match or beat margin routing, and retain at least 1.3x speedup versus strong-only inference on both datasets.
- Stop condition: Stop if entropy routing fails to beat random routing by 1.0 accuracy point on either dataset, fails to recover 50% of the small-to-strong gap, or measured local inference is not faster than strong-only by at least 1.3x.

## Evidence references

- Artifact root: `<local-path>/projects/medium-text-benchmark-for-entropy-routed-local-model-casca-f17e689242`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
