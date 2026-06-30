# Contradiction ledger for small CPU agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `contradiction-ledger-for-small-cpu-agents-689a7463150e`
Run ID: `contradiction-ledger-for-small-cpu-agents-689a7463150e-20260524T170847093499+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0e85bfeb5280

## What looked useful

Ledger-triggered verification is a useful implementation signal versus naive memory, but the tested ledger policy is not performance-novel because smallest-margin uncertainty verification was consistently stronger across budgets and noise rates.

## Boundaries and scale limits

Synthetic structured claims only; no natural-language extraction, real LLM traces, live agent tool latency, temporal persistence, or long-horizon multi-agent setting. Runs were CPU-only and bounded to 20 smoke episodes, 2,000 main episodes, and 10,000 sweep episodes.

## Claim scope

On a synthetic structured fact-stream benchmark with functional attributes, noisy reports, and limited oracle verification, a contradiction-ledger agent improves final QA accuracy over recency, majority, and random-verification baselines but does not beat a simpler uncertainty-based verification baseline.

## Why it stopped

Bounded synthetic evidence is mixed: the mechanism works against weak baselines but fails against a simple strong control, so this is a useful signal rather than a paper-positive validation.

## Recommended next action

Stop this run as no-paper evidence; next test should isolate temporal persistence or recurring contradictions where ledger memory may beat margin-based verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Temporal contradiction ledger with recurring disputes
- Success threshold: Persistent ledger improves QA accuracy by at least 2 percentage points over uncertainty-only verification or reduces verification calls by at least 20% at matched accuracy across at least three seeds.
- Stop condition: Stop if the persistent ledger is not better than uncertainty-only on either accuracy or verification-call efficiency in the temporal benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/contradiction-ledger-for-small-cpu-agents-689a7463150e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
