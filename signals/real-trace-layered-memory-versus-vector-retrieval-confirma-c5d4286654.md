# Real-trace layered memory versus vector retrieval confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-layered-memory-versus-vector-retrieval-confirma-c5d4286654`
Run ID: `real-trace-layered-memory-versus-vector-retrieval-confirma-c5d4286654-20260620T203823957847+0000`

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

- Parent run decision: Layered User/Project Memory Hierarchy vs Flat Vector Retrieval: enoch://control-plane/projects/layered-user-project-memory-hierarchy-vs-flat-vector-retrieval-435a9eeb3857/runs/layered-user-project-memory-hierarchy-vs-flat-vector-retrieval-435a9eeb3857-20260620T201252260570+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

Layered memory reached 24/24 accuracy versus 17/24 for flat retrieval, a +0.292 absolute gain over a predeclared +0.15 threshold, with strongest gains on conditional and policy questions.

## Boundaries and scale limits

No real private/public trace dataset was present; fixture traces were hand-authored, the vector baseline was deterministic TF-IDF rather than an embedding service, and layered memory used hand-authored extractors/query routing. This is mechanism evidence only, not publication-grade real-trace confirmation.

## Claim scope

In a deterministic Tier-1 controlled trace-shaped replay fixture with 6 projects and 24 keyed memory queries, explicit layered doctrine/project/constraint/decision memory outperformed flat lexical retrieval on stale-update, policy, and conditional recall without query-kind regressions.

## Why it stopped

Tier-1 controlled direct mechanism test completed and met threshold, but the absence of real trace data and neural vector retrieval means the result is no-paper useful signal rather than real-trace confirmation.

## Recommended next action

Run the same fixed evaluator contract on 50-100 anonymized real replay traces with answer keys and a real embedding/vector retrieval baseline; stop if layered memory fails to beat vector retrieval by at least 0.10 absolute accuracy or introduces any policy/conditional regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anonymized real-trace layered memory versus embedding retrieval confirmation
- Success threshold: Layered memory beats embedding/vector retrieval by >=0.10 absolute accuracy overall and has no lower accuracy on policy or conditional query kinds.
- Stop condition: Stop as no-paper negative if layered memory does not beat the vector baseline by >=0.10 absolute accuracy, any policy/conditional regression appears, or answer-keyed real traces cannot be obtained.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-layered-memory-versus-vector-retrieval-confirma-c5d4286654`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
