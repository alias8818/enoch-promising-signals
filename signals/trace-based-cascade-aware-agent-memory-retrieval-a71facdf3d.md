# Trace-Based Cascade-Aware Agent Memory Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-based-cascade-aware-agent-memory-retrieval-a71facdf3d`
Run ID: `trace-based-cascade-aware-agent-memory-retrieval-a71facdf3d-20260610T220059483351+0000`

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

- Parent run decision: Layered Agent Memory: Cascade-Aware Retrieval vs Flat Vector: enoch://control-plane/projects/layered-agent-memory-cascade-aware-retrieval-vs-flat-vector-1e9b1ce23c12/runs/layered-agent-memory-cascade-aware-retrieval-vs-flat-vector-1e9b1ce23c12-20260610T211358190247+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7322411afbae

## What looked useful

Semantic-gap condition: flat answerable rate 0.00 and support recall 0.25; cascade answerable rate 1.00 and support recall 1.00 across 5/5 seeds, latency ratio about 1.00. Anchored negative control: both methods reached 1.00 answerable rate, showing the benefit is conditional on lexical/support-chain gaps.

## Boundaries and scale limits

Tier 1 controlled direct test only: synthetic traces, TF-IDF flat baseline, deterministic support-completeness answerability metric, 5 semantic-gap seeds with 600 queries and 4000 memories per seed, plus an anchored negative control and budget ablation. No real agent traces, embedding retriever, LLM answer evaluation, or production-scale memory system was tested.

## Claim scope

In a controlled synthetic agent-trace memory store with explicit dependency edges, cascade-aware retrieval recovered complete four-step causal support chains under a fixed budget when upstream memories lacked the query anchor; it did not improve over flat retrieval when all required memories shared the anchor.

## Why it stopped

The Tier 1 test supports the mechanism only in a controlled semantic-gap condition and is not publication-grade evidence; the anchored negative control shows no general benefit when flat retrieval already sees the chain.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded deepen test should use a real or higher-fidelity agent trace corpus with embedding retrieval and downstream LLM answer scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding-baseline cascade retrieval on realistic agent traces
- Success threshold: Across at least 500 held-out queries, cascade expansion must improve complete support-chain recovery by at least 15 percentage points and downstream answer correctness by at least 10 percentage points over the strongest embedding baseline, with retrieval latency no more than 2x baseline.
- Stop condition: Stop if embedding or reranker baselines recover complete support within 5 percentage points of cascade retrieval, or if cascade expansion exceeds 2x latency before reaching the support and answer-correctness thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/trace-based-cascade-aware-agent-memory-retrieval-a71facdf3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
