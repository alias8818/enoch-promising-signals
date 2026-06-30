# Recency+Attention KV Eviction on Long-Form Code

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `recency-attention-kv-eviction-on-long-form-code-80ad0388f904`
Run ID: `recency-attention-kv-eviction-on-long-form-code-80ad0388f904-20260611T111158322248+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59f60beba17

## What looked useful

The implemented online hybrid eviction rule did not demonstrate code-lookup quality gains. In a 220-step tiny decoder run, full-cache exact match was 0.000 and bounded-cache NLLs were indistinguishable, so the model did not use the long-range lookup. In a 64-example trace proxy, target return-value span survival was 0.000 for recency, attention-only, and hybrid at budgets 80, 112, 160, and 224, while target-name survival was 1.000 due to final-query recency. This suggests simple accumulated attention can preserve recent names without preserving the old value spans needed for lookup.

## Boundaries and scale limits

No pretrained code model, no repository-scale corpus, no 7B+ model, no production serving benchmark, and no publication-grade quality validation. Trace results are proxy evidence and model-quality results are inconclusive because full-cache exact match was 0.0.

## Claim scope

Bounded local test of a simple online recency-plus-accumulated-attention KV eviction rule on synthetic long-form code lookup streams. The direct tiny-model quality test failed its full-cache gate; the trace proxy tested only retention of target code spans under online eviction.

## Why it stopped

Proxy/early falsification: the direct model test failed its full-cache gate and the online trace proxy did not retain needed old return-value spans under the tested hybrid scoring rule.

## Recommended next action

Stop this run as a proxy/early negative; only revisit with a pretrained or sufficiently trained code model that first passes a full-cache lookup accuracy gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Code-Model KV Eviction Gate for Return-Value Lookup
- Success threshold: Hybrid improves exact match by at least 10 percentage points or answer NLL by at least 10% over recency-only at one or more constrained budgets while full-cache exact match is at least 80%.
- Stop condition: Stop if full-cache exact match remains below 80% after bounded tuning, or if real attention maps do not score old definition/value spans before they would be evicted.

## Evidence references

- Artifact root: `<local-path>/projects/recency-attention-kv-eviction-on-long-form-code-80ad0388f904`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
