# Independent Sanitized Trace Doctrine Memory Answer-Level Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `independent-sanitized-trace-doctrine-memory-answer-level-v-41e8d58635`
Run ID: `independent-sanitized-trace-doctrine-memory-answer-level-v-41e8d58635-20260621T171242213183+0000`

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

- Parent run decision: Sanitized Real-Trace Doctrine Memory Replay: enoch://control-plane/projects/sanitized-real-trace-doctrine-memory-replay-2838aec344/runs/sanitized-real-trace-doctrine-memory-replay-2838aec344-20260621T164801210039+0000
- Parent run decision: Operator-Doctrine Memory: Reusable Procedures from Repeated Agent Traces: enoch://control-plane/projects/operator-doctrine-memory-reusable-procedures-from-repeated-agent-traces-03721b03091a/runs/operator-doctrine-memory-reusable-procedures-from-repeated-agent-traces-03721b03091a-20260621T163202544118+0000

## What looked useful

Layered doctrine memory reached 1.0000 accuracy versus 0.9917 for flat retrieval, 0.9185 for the no-source-gate ablation, 0.9731 for the no-recency ablation, 0.6694 for transcript search, and 0.2361 for no memory. Bootstrap delta versus flat retrieval was +0.0083 accuracy with 95% CI +0.0037 to +0.0139.

## Boundaries and scale limits

No real private/operator trace corpus, no blinded human labels, no live repeated-agent sessions, and no LLM-in-the-loop answer generation were used. The positive delta over flat retrieval is small and synthetic-only.

## Claim scope

On a deterministic synthetic sanitized repeated-trace benchmark with 5 fixed seeds, 3 noise levels, 1080 answer-level tasks, and 6480 strategy trials, layered doctrine memory improves exact answer-policy accuracy over no-memory, transcript-search, and flat-retrieval baselines; source-gating and recency ablations reduce accuracy.

## Why it stopped

Synthetic Tier 2 evidence supports the mechanism but is not publication-grade direct evidence on real traces or LLM-in-the-loop agent answers.

## Recommended next action

Stop paper escalation here; run a bounded real-trace replay follow-up using the same answer-level metric and ablations on sanitized held-out operator traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Sanitized Trace Replay for Doctrine Memory Answer-Level Validation
- Success threshold: Layered doctrine memory improves exact answer-policy accuracy over flat retrieval by at least 0.02 absolute with bootstrap 95% CI lower bound above 0, and both ablations score below the full layered strategy.
- Stop condition: Stop as no-paper if the real-trace delta versus flat retrieval is below 0.02 absolute, its bootstrap 95% CI crosses 0, or either ablation matches/exceeds the full layered strategy.

## Evidence references

- Artifact root: `<local-path>/projects/independent-sanitized-trace-doctrine-memory-answer-level-v-41e8d58635`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
