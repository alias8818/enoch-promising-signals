# Direct LLM-Agent Contradiction Recovery Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-llm-agent-contradiction-recovery-benchmark-eeb1daa2d8`
Run ID: `direct-llm-agent-contradiction-recovery-benchmark-eeb1daa2d8-20260513T211036727032+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71ba98c819f4

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Mechanism support came from a small direct synthetic benchmark, not from publication-grade direct evidence across models, phrasings, and real agent traces.

## Recommended next action

Stop this run as no-paper: the Tier 1 direct test supports contradiction recovery on one small model, but only a bounded medium multi-model/multi-turn confirmation could make the claim publication-relevant.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Multi-Model Contradiction Recovery Confirmation
- Success threshold: Contradiction recovery accuracy at least 90% for each tested model and prompt family, with stale-value error rate at most 5% and no more than a 5 percentage point drop from clean controls.
- Stop condition: Stop as negative if any target model falls below 80% contradiction recovery or stale-value errors exceed 15% on explicit newer-evidence prompts.

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-agent-contradiction-recovery-benchmark-eeb1daa2d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
