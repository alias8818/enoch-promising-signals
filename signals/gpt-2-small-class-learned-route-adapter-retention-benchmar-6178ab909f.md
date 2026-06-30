# GPT-2-small-class learned-route adapter retention benchmark

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `gpt-2-small-class-learned-route-adapter-retention-benchmar-6178ab909f`
Run ID: `gpt-2-small-class-learned-route-adapter-retention-benchmar-6178ab909f-20260522T035528441572+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Neural Adapter Route-Bounded Fine-Tuning Probe: enoch://control-plane/projects/neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c/runs/neural-adapter-route-bounded-fine-tuning-probe-1d5d50ae8c-20260522T033630004041+0000
- Parent run decision: Small Transformer Learned-Route Adapter Retention Test: enoch://control-plane/projects/small-transformer-learned-route-adapter-retention-test-b70bae4e6d/runs/small-transformer-learned-route-adapter-retention-test-b70bae4e6d-20260522T034522711990+0000

## What looked useful

Mean Task-A retention delta loss after Task-B adaptation was 1.6091 for dense fine-tuning, 0.0577 for shared adapter, and 0.0020 for learned-route adapters across seeds 0,1,2. Learned-route diagnostics routed A to route 0 with mean 0.99959 and B to route 1 with mean 0.99988 after adaptation.

## Boundaries and scale limits

This run used a 2-layer d_model=96 CPU transformer on synthetic sequence recurrences, not GPT-2-small-class parameters, natural text, long-context data, or marker-free route discovery. The CPU worker and 15-minute CPU-only efficiency rule prevented direct GPT-2-small-class validation here.

## Claim scope

In a compact synthetic causal-LM retention benchmark with explicit domain markers, learned-route two-adapter training preserved Task-A performance during Task-B adaptation better than dense sequential fine-tuning and a shared-adapter control across three fixed seeds.

## Why it stopped

Moderate synthetic evidence supports the retention mechanism, but the literal GPT-2-small-class learned-route adapter claim remains unvalidated and is not paper-ready.

## Recommended next action

Stop this worker run as no-paper useful signal; use scripts/retention_benchmark.py and results/medium_aggregate.json to design a direct GPT-2-small-class or close parameter-matched GPU validation rather than launching another small CPU proxy.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-learned-route-adapter-retention-benchmar-6178ab909f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
