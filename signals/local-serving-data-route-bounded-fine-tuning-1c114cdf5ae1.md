# Local-Serving Data-Route Bounded Fine-Tuning

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `local-serving-data-route-bounded-fine-tuning-1c114cdf5ae1`
Run ID: `local-serving-data-route-bounded-fine-tuning-1c114cdf5ae1-20260521T202028084148+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42e89d1099e

## What looked useful

Across 40 seeds per setting, route-bounded updates beat dense global updates on net adaptation-minus-forgetting in all tested route-noise settings. With no routing noise, adaptation gain matched dense at 2.0548 NLL while bounded forgetting was 0.0000 versus dense 0.3502. At 30% route noise, bounded forgetting remained 0.0420 versus dense 0.3502 and bounded net gain remained higher, 1.8549 versus 1.7046.

## Boundaries and scale limits

Standard-library count-based Markov proxy only; no neural LLM, LoRA/adapters, production serving traces, latency measurements, memory measurements, or large-scale route classifier behavior were tested.

## Claim scope

In a synthetic route-conditioned Markov next-token model, applying serving-time updates only to the observed route preserved shifted-route adaptation while substantially reducing unrelated-route forgetting versus applying the same update to every route.

## Why it stopped

Proxy evidence supports the route-bounding mechanism but is not full validation because it used synthetic Markov data and count updates rather than neural fine-tuning on real or realistic serving traces.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded neural adapter follow-up using a small language model with parameter-matched dense and route-bounded updates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Adapter Route-Bounded Fine-Tuning Probe
- Success threshold: Bounded update retains >=80% of dense shifted-route adaptation and reduces mean unrelated-route forgetting by >=50% at <=10% routing noise across at least three seeds.
- Stop condition: Stop if bounded updates lose more than half of dense adaptation or fail to reduce unrelated-route forgetting by at least 25% in the first three-seed neural probe.

## Evidence references

- Artifact root: `<local-path>/projects/local-serving-data-route-bounded-fine-tuning-1c114cdf5ae1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
