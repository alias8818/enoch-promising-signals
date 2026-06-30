# Trained-model suffix rollback evaluation against no-rollback KV eviction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trained-model-suffix-rollback-evaluation-against-no-rollba-cfd3f26a51`
Run ID: `trained-model-suffix-rollback-evaluation-against-no-rollba-cfd3f26a51-20260609T072202926545+0000`

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

- Parent run decision: Layer-wise KV eviction with suffix rollback for long-context home inference: enoch://control-plane/projects/layer-wise-kv-eviction-with-suffix-rollback-for-long-context-home-inference-b98d61e2d895/runs/layer-wise-kv-eviction-with-suffix-rollback-for-long-context-home-inference-b98d61e2d895-20260609T041837675583+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

Tier 1 direct test met the predeclared threshold on all seeds: rollback accuracy 1.0000 vs no-rollback accuracy mean 0.0343, mean rollback advantage 0.9657, threshold requiring rollback accuracy >= 0.80 and advantage >= 0.25.

## Boundaries and scale limits

Synthetic task only; 2-layer 64-hidden decoder, window 32, lag 8, vocab 32, three seeds, GB10 local run. Does not test natural language, pretrained GPT-2-class models, RoPE/ALiBi, production serving kernels, latency overhead, or large-context workloads.

## Claim scope

In a controlled toy trained causal transformer with learned absolute positions and a fixed KV budget, recomputing the retained active suffix under current window positions preserved relative-position retrieval accuracy, while no-rollback KV eviction with stale retained suffix state failed near chance.

## Why it stopped

No-paper useful signal: the controlled Tier 1 mechanism threshold was supported, but evidence remains synthetic toy-scale rather than publication-grade.

## Recommended next action

Run a bounded deepen follow-up on a GPT-2-small-class or comparable pretrained/fine-tuned decoder with learned-position and RoPE variants, measuring perplexity/accuracy and recomputation cost under a fixed KV budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class suffix rollback versus stale KV eviction under fixed KV budgets
- Success threshold: Rollback must improve perplexity or task accuracy by at least 10% relative over no-rollback stale KV eviction at the same KV budget while keeping recomputation overhead below 2x on the tested local setup.
- Stop condition: Stop if rollback does not improve quality on at least two model/task settings or if overhead exceeds 2x without a quality gain large enough to justify the cost.

## Evidence references

- Artifact root: `<local-path>/projects/trained-model-suffix-rollback-evaluation-against-no-rollba-cfd3f26a51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
