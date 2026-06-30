# Cumulative KV eviction for long-context home agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cumulative-kv-eviction-for-long-context-home-agents-172a9cb53bdd`
Run ID: `cumulative-kv-eviction-for-long-context-home-agents-172a9cb53bdd-20260607T165609540907+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a5e63a14f587

## What looked useful

Plain cumulative-attention eviction was not a robust improvement over sliding-window and often underperformed at larger cache sizes. A decayed/age-adjusted cumulative variant improved low-capacity all-query top1 by about 0.016 over sliding at capacities 64 and 128, but simple last-attention or random eviction often protected delayed one-shot facts better at larger capacities.

## Boundaries and scale limits

No real transformer KV cache, no generation-quality evaluation, no real transcript corpus, no GPU attention-kernel latency measurement, and no multi-layer model behavior. Main evidence is 5,000 synthetic stream steps across 12 seeds and cache capacities 64-512, plus two smaller query-mix ablations.

## Claim scope

Synthetic attention-retrieval proxy for KV eviction in long-context home-agent memory streams with recurring hot facts and delayed one-shot facts.

## Why it stopped

Proxy evidence is mixed: it early-falsifies plain cumulative attention as a standalone eviction policy and supports only a decayed hybrid variant, which is not direct or strong enough for publication.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded test should implement decayed cumulative eviction in a small real transformer KV cache and require it to beat sliding-window and last-attention on delayed-fact QA without hurting recurring-fact QA.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer test of decayed cumulative KV eviction on delayed home-agent facts
- Success threshold: At the same KV capacity, decayed cumulative eviction improves overall controlled QA accuracy by >=3 percentage points over both sliding-window and last-attention, with delayed one-shot QA accuracy no worse than the best baseline by more than 1 percentage point.
- Stop condition: Stop if decayed cumulative eviction fails to beat both baselines on two independent prompt seeds or if delayed one-shot accuracy drops by more than 1 percentage point versus the best baseline.

## Evidence references

- Artifact root: `<local-path>/projects/cumulative-kv-eviction-for-long-context-home-agents-172a9cb53bdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
