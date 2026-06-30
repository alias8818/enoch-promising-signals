# Learned small-model validation of non-oracle anchors for dual-resolution memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-small-model-validation-of-non-oracle-anchors-for-d-a2d2bdaac0`
Run ID: `learned-small-model-validation-of-non-oracle-anchors-for-d-a2d2bdaac0-20260527T060417440938+0000`

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

- Parent run decision: Dual-Resolution Memory with Exact Anchor Bank: enoch://control-plane/projects/dual-resolution-memory-with-exact-anchor-bank-f00a8134b242/runs/dual-resolution-memory-with-exact-anchor-bank-f00a8134b242-20260525T033811119411+0000
- Parent run decision: Non-oracle anchor selection for dual-resolution memory on a small language-memory task: enoch://control-plane/projects/non-oracle-anchor-selection-for-dual-resolution-memory-on-f2f015adbc/runs/non-oracle-anchor-selection-for-dual-resolution-memory-on-f2f015adbc-20260526T224821224272+0000

## What looked useful

Learned validation beat the heuristic baseline in every seed/regime at budgets 1-4: +0.251 to +0.294 absolute accuracy at budget 1, +0.206 to +0.347 at budget 2, and +0.062 to +0.267 at budget 4. A no-query ablation was consistently weaker than the full validator, supporting query-conditioned anchor validation as the mechanism.

## Boundaries and scale limits

Synthetic documents, synthetic queries, engineered features, and answer-span-retention metric only; no real corpus, real LLM summaries, production retrieval stack, or downstream generation-quality validation. The effect mostly vanishes when the high-resolution budget is loose enough to store half of all candidates.

## Claim scope

In a controlled synthetic dual-resolution memory task with non-oracle candidate anchors, a small learned validator improves answer-span retention over random and heuristic anchor-selection baselines under tight high-resolution budgets across 5 fixed seeds and three regimes.

## Why it stopped

Medium synthetic evidence supports the mechanism but is not direct enough for publication-grade validation; closing as no-paper useful signal rather than treating proxy evidence as paper-positive.

## Recommended next action

Run a bounded real-corpus deepen test using public long-document QA or citation-retrieval data, fixed document-level train/test split, BM25 or embedding candidate generation, and the same answer-retention budget metric before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus learned validation of non-oracle dual-resolution memory anchors
- Success threshold: At budget levels storing no more than 25% of candidates, learned validation improves answer-span retention by >=5 absolute points over BM25/embedding score in at least two datasets or two query regimes, with the no-query ablation below the full validator.
- Stop condition: Stop as negative if the learned validator fails to beat the candidate-generator baseline by 5 absolute points at tight budgets, or if gains vanish under document-level train/test separation.

## Evidence references

- Artifact root: `<local-path>/projects/learned-small-model-validation-of-non-oracle-anchors-for-d-a2d2bdaac0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
