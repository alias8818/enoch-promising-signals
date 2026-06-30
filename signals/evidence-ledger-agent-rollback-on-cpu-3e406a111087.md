# Evidence-Ledger Agent Rollback on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-rollback-on-cpu-3e406a111087`
Run ID: `evidence-ledger-agent-rollback-on-cpu-3e406a111087-20260527T135143911097+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c397c3a251f1

## What looked useful

Rollback produced a +0.01625 final-accuracy delta and +0.02986 mean trajectory-accuracy delta in the main 12% corruption run, zero delta in a no-corruption control, and +0.09237 final-accuracy delta under 25% corruption. Isolated ledger replay was 1.356x slower than baseline but still processed about 29k events/sec with 22.7 MiB max RSS.

## Boundaries and scale limits

CPU-only Python simulation; 40-seed main and stress runs over 200 tasks and 80 steps; synthetic facts and oracle retraction signals only; no real LLM agent traces, persistent backend, or non-oracle contradiction detector.

## Claim scope

In a synthetic binary-fact agent harness with delayed oracle retractions, an append-only evidence ledger with rollback improves decision accuracy over a no-rollback accumulator when corrupt evidence is present.

## Why it stopped

No-paper closure: mechanism supported only in a synthetic/proxy harness, not direct production-agent validation.

## Recommended next action

Stop this run as a bounded synthetic useful signal; next evidence should replay realistic agent traces with non-oracle contradiction detection before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger rollback on realistic agent traces
- Success threshold: At least a +5 percentage point recovery-success improvement or 20% faster recovery on contaminated traces, no statistically meaningful regression on clean traces, and less than 2x runtime overhead.
- Stop condition: Stop if rollback causes clean-trace regressions above 2 percentage points, false rollbacks erase useful evidence often enough to offset contaminated-trace gains, or overhead exceeds 2x without a clear indexing fix.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-rollback-on-cpu-3e406a111087`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
