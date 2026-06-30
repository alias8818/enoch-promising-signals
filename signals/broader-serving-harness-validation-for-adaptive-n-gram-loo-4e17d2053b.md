# Broader serving-harness validation for adaptive n-gram lookahead

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `broader-serving-harness-validation-for-adaptive-n-gram-loo-4e17d2053b`
Run ID: `broader-serving-harness-validation-for-adaptive-n-gram-loo-4e17d2053b-20260604T043914056004+0000`

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

- Parent run decision: Adaptive N-gram Lookahead in a Serving Baseline: enoch://control-plane/projects/adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc/runs/adaptive-n-gram-lookahead-in-a-serving-baseline-fb23737fcc-20260604T020652574055+0000
- Parent run decision: N-gram KV Cache Lookahead Drafting: enoch://control-plane/projects/n-gram-kv-cache-lookahead-drafting-87467d11d8c0/runs/n-gram-kv-cache-lookahead-drafting-87467d11d8c0-20260604T001513474828+0000

## What looked useful

Coherent n-gram speculative lookahead produced exact baseline-equivalent outputs and large target-call reductions, while randomized n-gram control had low draft acceptance and much smaller call reductions. Adaptive control is plausible but only weakly better than fixed lookahead in this run.

## Boundaries and scale limits

Single small causal LM, one corpus, 36 medium prompt/seed records across n=2 and n=3 ablations, custom Python harness, no continuous batching, no production KV-cache accounting, no multi-user traffic model, and no larger-model or multi-dataset validation.

## Claim scope

On distilgpt2 with Wikitext-2 prompt windows, a custom serving-style harness showed exact greedy-output preservation and about 48-52% target-model invocation reduction for coherent n-gram lookahead versus baseline greedy decoding; adaptive lookahead modestly improved over fixed lookahead by about 1-1.5 percentage points on average.

## Why it stopped

Tier 2 direct validation supports the mechanism but does not establish broad serving robustness or a strong adaptive-over-fixed advantage.

## Recommended next action

Stop this run as no-paper useful signal; next bounded evidence should integrate the same policies into a KV-cache-aware serving harness and test at least two model sizes and two corpora before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware multi-model validation of adaptive n-gram lookahead
- Success threshold: Adaptive must preserve exact greedy outputs on all checked requests, beat greedy by at least 25% end-to-end throughput, and beat fixed lookahead by at least 5 percentage points mean target-call reduction without worse p95 latency.
- Stop condition: Stop if adaptive fails exact-match equivalence, fails to beat fixed by 5 percentage points on both corpora, or KV-cache/memory overhead erases the greedy throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/broader-serving-harness-validation-for-adaptive-n-gram-loo-4e17d2053b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
