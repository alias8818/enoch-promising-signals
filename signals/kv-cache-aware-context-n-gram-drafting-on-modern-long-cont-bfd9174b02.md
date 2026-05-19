# KV-cache-aware context n-gram drafting on modern long-context workloads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-aware-context-n-gram-drafting-on-modern-long-cont-bfd9174b02`
Run ID: `kv-cache-aware-context-n-gram-drafting-on-modern-long-cont-bfd9174b02-20260514T024856780162+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc1935697b9c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 direct replay found mechanism support but missed the predeclared 20% mean target-call reduction threshold across the real workload mix; this is not publication-grade evidence.

## Recommended next action

Stop this paper path for now; if continuing, run a bounded model-integrated follow-up on code and repeated-document RAG prompts where the Tier 1 replay showed the effect is concentrated.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-integrated cache-aware n-gram drafting on code and repeated-document long-context prompts
- Success threshold: At least 15% median wall-clock latency reduction and at least 20% target-call reduction on code/RAG workloads, with no measured quality regression and with shuffled/reordered controls near zero benefit.
- Stop condition: Stop if model-integrated latency gain is below 10% median or if acceptance gains disappear outside repeated-passage/code-heavy prompts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-context-n-gram-drafting-on-modern-long-cont-bfd9174b02`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
