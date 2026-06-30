# KNN-on-Embeddings Difficulty Router for Cascade Escalation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `knn-on-embeddings-difficulty-router-for-cascade-escalation-fa32d61fd55c`
Run ID: `knn-on-embeddings-difficulty-router-for-cascade-escalation-fa32d61fd55c-20260614T045430379067+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/353f49aa9e91

## What looked useful

KNN difficulty routing had cheap-error AUCs of 0.6865, 0.7973, and 0.7148 across breast_cancer, digits, and wine, beating shuffled-label KNN controls, but cheap confidence AUC was 0.9266, 0.9267, and 0.9430 and generally produced higher cascade accuracy at low-to-moderate escalation budgets.

## Boundaries and scale limits

This run used small tabular/image datasets, logistic-regression cheap models, random-forest strong models, and PCA feature embeddings. It did not test LLM outputs, production text/code embeddings, API/model serving costs, latency, domain shift, or large-scale calibration.

## Claim scope

On three small scikit-learn classification proxies using PCA feature embeddings, KNN over calibration examples labeled by cheap-model errors detects local difficulty signal above shuffled-label and random controls, but it does not outperform a cheap-model confidence router for cascade escalation accuracy.

## Why it stopped

No-paper useful signal: this proxy test supports local neighborhood difficulty structure but early-falsifies KNN as a standalone replacement for simple confidence routing in the tested cascade setting.

## Recommended next action

Stop paper path for this proxy result; if continuing, run one bounded direct text-embedding cascade benchmark with cheap/strong model correctness labels and compare KNN against confidence, learned logistic routing, and random controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Text-Embedding Cascade Router Benchmark Against Confidence and Learned Routing
- Success threshold: KNN must improve cascade accuracy over cheap confidence by at least 1 absolute percentage point at two of 5%, 10%, and 20% escalation budgets, or match confidence while requiring no cheap-model probability/confidence access.
- Stop condition: Stop if KNN fails to beat confidence or the learned router by at least 1 absolute point at low escalation budgets, or if shuffled-label/negative controls erase the observed KNN advantage.

## Evidence references

- Artifact root: `<local-path>/projects/knn-on-embeddings-difficulty-router-for-cascade-escalation-fa32d61fd55c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
