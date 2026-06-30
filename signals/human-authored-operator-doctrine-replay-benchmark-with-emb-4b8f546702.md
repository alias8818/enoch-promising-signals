# Human-authored operator-doctrine replay benchmark with embedding flat baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `human-authored-operator-doctrine-replay-benchmark-with-emb-4b8f546702`
Run ID: `human-authored-operator-doctrine-replay-benchmark-with-emb-4b8f546702-20260620T165000404750+0000`

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

- Parent run decision: Operator-Doctrine Memory vs Flat Retrieval on CPU: enoch://control-plane/projects/operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76/runs/operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76-20260620T163942579555+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a0ad0c6bd9

## What looked useful

Layered doctrine memory reached 1.000 source accuracy and 1.000 MRR versus the best baseline transcript_search at 0.944 source accuracy and 0.963 MRR; flat_embedding reached 0.722 source accuracy and 0.843 MRR.

## Boundaries and scale limits

Small worker-authored task set; deterministic hashed embeddings rather than a production embedding model; no real/private operator traces; no LLM generation or long-context persistence test; CPU-only Tier 1 runtime under one second.

## Claim scope

On an 18-task hand-authored operator-doctrine replay benchmark, a category-gated doctrine memory retriever improved required-source retrieval over no-memory, transcript-search, and flat hashed TF-IDF embedding baselines.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal, but the evidence is small, worker-authored, and proxying real embeddings and generation; this is not full validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up with at least 100 held-out human-authored replay tasks, a standard embedding model baseline, noisy long transcript distractors, and a deterministic answer-quality rubric before considering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out operator-doctrine replay benchmark with real embedding baselines
- Success threshold: Layered doctrine memory improves required-source retrieval by at least 10 absolute percentage points over the best flat embedding baseline and does not reduce answer-quality rubric score by more than 2 percentage points.
- Stop condition: Stop as no-paper if the advantage is below 5 absolute percentage points, if gains disappear under doctrine-gating ablation, or if answer-quality scoring shows the selected sources do not improve final operator actions.

## Evidence references

- Artifact root: `<local-path>/projects/human-authored-operator-doctrine-replay-benchmark-with-emb-4b8f546702`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
