# Two-stage home-memory anchor selection plus exact rehydration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `two-stage-home-memory-anchor-selection-plus-exact-rehydrat-e3a53780bc`
Run ID: `two-stage-home-memory-anchor-selection-plus-exact-rehydrat-e3a53780bc-20260613T163432931883+0000`

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

- Parent run decision: Long-context exact anchor indexing for home AI memory retrieval: enoch://control-plane/projects/long-context-exact-anchor-indexing-for-home-ai-memory-retrieval-d94c81ac61dc/runs/long-context-exact-anchor-indexing-for-home-ai-memory-retrieval-d94c81ac61dc-20260613T160800453036+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/32895b5f366b

## What looked useful

Exact rehydration is useful only after anchor selection finds the right record: it cleanly restores exact facts absent from compressed memory, but cannot compensate for ambiguous or missing anchor fields.

## Boundaries and scale limits

Test used 1,600 synthetic records, 400 deterministic lexical queries, and BM25-style token matching. It did not test real user memory distributions, learned embedding/reranker selectors, LLM generation, privacy constraints, or long-context serving costs. Underspecified queries failed at 0.49 recall@5, so robust disambiguation is unresolved.

## Claim scope

In a deterministic synthetic home-memory benchmark with fully specified anchor fields, compact anchor selection followed by exact full-record rehydration recovered exact hidden values at 1.00 recall@5 and 1.00 exact-answer accuracy@5, while compressed summaries alone recovered 0.00 exact values.

## Why it stopped

No-paper useful signal: the Tier 1 controlled small direct test supports the mechanism on fully specified anchors but exposes a major failure mode on underspecified anchors; this is not publication-grade evidence.

## Recommended next action

Run a bounded deepen test adding second-pass disambiguation or reranking for underspecified anchor queries, and stop unless recall@5 reaches at least 0.90 without reducing fully specified exact accuracy below 0.99.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-pass disambiguation for underspecified home-memory anchor queries
- Success threshold: Underspecified-query two-stage recall@5 and exact-answer accuracy@5 >= 0.90, fully specified exact-answer accuracy@5 >= 0.99, and compressed-only exact-answer accuracy@5 <= 0.05.
- Stop condition: Stop as negative if underspecified recall@5 remains below 0.80 or if the method requires scanning more than 25% of full-memory bytes per query.

## Evidence references

- Artifact root: `<local-path>/projects/two-stage-home-memory-anchor-selection-plus-exact-rehydrat-e3a53780bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
