# Noisy metadata cascaded memory rerank on realistic replay transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `noisy-metadata-cascaded-memory-rerank-on-realistic-replay-32fcac3277`
Run ID: `noisy-metadata-cascaded-memory-rerank-on-realistic-replay-32fcac3277-20260621T051132156652+0000`

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

- Parent run decision: Cascaded retrieval-then-rerank agent memory: enoch://control-plane/projects/cascaded-retrieval-then-rerank-agent-memory-823412608276/runs/cascaded-retrieval-then-rerank-agent-memory-823412608276-20260621T040542557419+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5f990dbbbaa

## What looked useful

Across 960 controlled replay tasks, cascaded_memory_rerank reached 0.834 hit@1 and 0.891 MRR versus the best non-cascaded baseline at 0.674 hit@1 and 0.744 MRR. The predeclared >=10 point hit@1 margin threshold was met overall (+0.160) and at high metadata noise rates 0.50/0.75 (+0.133).

## Boundaries and scale limits

Synthetic controlled replay transcripts only; no private/operator production logs, no independently labeled held-out real replay corpus, no learned retriever, and no downstream agent answer evaluation.

## Claim scope

On a deterministic Tier 1 controlled replay-memory corpus with stale facts, decoys, and injected metadata corruption, cascaded memory reranking improved current-fact retrieval hit@1 over transcript search, flat retrieval, and layered-doctrine baselines.

## Why it stopped

No-paper useful signal: controlled direct mechanism support was produced, but the evidence is generated Tier 1 data rather than publication-grade real replay validation.

## Recommended next action

Run a deepen follow-up on a held-out real replay transcript set with independently labeled current facts and naturally extracted noisy metadata; stop paper consideration unless the >=10 point hit@1 advantage persists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out real replay transcript confirmation for noisy metadata cascaded rerank
- Success threshold: Cascaded rerank improves hit@1 by at least 10 percentage points over the best non-cascaded baseline overall and by at least 5 points within each measured metadata-noise bucket, without a material MRR regression.
- Stop condition: Stop as no-paper if the held-out real replay set shows less than a 5 point hit@1 gain over the best baseline or if failures concentrate on metadata/content patterns absent from the controlled generator.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-metadata-cascaded-memory-rerank-on-realistic-replay-32fcac3277`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
