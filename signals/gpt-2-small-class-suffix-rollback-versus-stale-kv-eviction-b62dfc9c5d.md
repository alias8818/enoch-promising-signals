# GPT-2-small-class suffix rollback versus stale KV eviction under fixed KV budgets

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-class-suffix-rollback-versus-stale-kv-eviction-b62dfc9c5d`
Run ID: `gpt-2-small-class-suffix-rollback-versus-stale-kv-eviction-b62dfc9c5d-20260609T115213728950+0000`

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
- Parent run decision: Trained-model suffix rollback evaluation against no-rollback KV eviction: enoch://control-plane/projects/trained-model-suffix-rollback-evaluation-against-no-rollba-cfd3f26a51/runs/trained-model-suffix-rollback-evaluation-against-no-rollba-cfd3f26a51-20260609T072202926545+0000

## What looked useful

Rollback preserved exact recompute predictions and NLLs with 1.0 agreement and zero NLL delta in every SST-2 cell. Stale suffix carryover fell to 0.3594-0.6380 agreement with exact, had mean absolute NLL deltas of 1.6389-1.7694, and showed 0.9974 normal-vs-reversed stale prediction mismatch at every budget.

## Boundaries and scale limits

One real classification task only; most prompts were shorter than the tested budgets, so only the 64-token budget produced any prompt truncation. The harness models visible token history rather than a production KV-cache implementation benchmark. No model-family replication or long-context workload was completed.

## Claim scope

On GPT-2-small zero-shot SST-2 class-suffix likelihood scoring, rollback of candidate suffix state exactly matches the recompute baseline across fixed visible-history budgets 64/128/256/512, while stale no-rollback suffix carryover causes large NLL shifts and order-dependent predictions.

## Why it stopped

Medium local evidence supports the mechanism, but the validation is too narrow and does not sufficiently stress long-context eviction budgets for a paper claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with deliberately long real prompts, at least one additional cached dataset, and implementation-level KV timing/correctness checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Long-prompt KV-cache implementation check for suffix rollback versus stale carryover
- Success threshold: Rollback agreement with exact >= 0.99 and mean abs NLL delta <= 1e-4 across datasets/budgets; stale agreement at least 10 percentage points lower than rollback or stale order-mismatch >= 0.10 under at least two budgets.
- Stop condition: Stop as negative if stale policy agrees with exact within 1 percentage point and has mean abs NLL delta < 0.05 across all long-prompt datasets/budgets, or if rollback fails to match exact due to implementation constraints.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-suffix-rollback-versus-stale-kv-eviction-b62dfc9c5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
