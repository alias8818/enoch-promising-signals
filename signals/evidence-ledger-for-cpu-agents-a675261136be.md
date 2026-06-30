# Evidence ledger for CPU agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-cpu-agents-a675261136be`
Run ID: `evidence-ledger-for-cpu-agents-a675261136be-20260602T114230624714+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bb39e358c230

## What looked useful

A ledger requiring byte-stable evidence spans reduced unsupported accepted claims from 20.1% to 0.0% in a unique-subject corpus and from 20.1% to 7.5% in a repeated-subject corpus. The repeated-subject run found that quote containment alone can validate the wrong record unless the ledger binds evidence to the task/source identity.

## Boundaries and scale limits

Synthetic corpus only; no real LLM or production CPU-agent traces; exact answer containment only; no semantic entailment, adversarial retrieval, or multi-step workflow validation.

## Claim scope

Synthetic CPU-local fact lookup traces show that an exact-span evidence ledger can reduce accepted unsupported claims with tens of microseconds of per-claim overhead; it eliminates injected wrong answers only when entity/source namespaces are unambiguous.

## Why it stopped

Closed as no-paper useful signal: proxy evidence supports a mechanism and exposes a failure mode, but synthetic exact-match traces are not direct publication-grade validation.

## Recommended next action

Run a bounded deepen test that adds explicit source/task binding to the ledger and measures whether repeated-subject unsupported accept rate falls to zero without excessive rejection of correct claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Source-bound evidence ledger under entity-collision traces
- Success threshold: Unsupported accepted claims are 0/1000 on repeated-subject and adversarial-collision benchmarks, accepted accuracy is at least 0.99, and mean latency overhead remains below 150 microseconds per claim.
- Stop condition: Stop if source binding still accepts any unsupported claims caused by entity collision or rejects more than 5% of correct claims in the non-adversarial repeated-subject benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-cpu-agents-a675261136be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
