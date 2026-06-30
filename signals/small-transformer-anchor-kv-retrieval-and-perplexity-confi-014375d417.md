# Small-transformer Anchor-KV retrieval and perplexity confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-anchor-kv-retrieval-and-perplexity-confi-014375d417`
Run ID: `small-transformer-anchor-kv-retrieval-and-perplexity-confi-014375d417-20260628T025345453776+0000`

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

- Parent run decision: Anchor-KV: Long-Context KV Compression with Exact Token Anchors: enoch://control-plane/projects/anchor-kv-long-context-kv-compression-with-exact-token-anchors-b1da7085ebd3/runs/anchor-kv-long-context-kv-compression-with-exact-token-anchors-b1da7085ebd3-20260628T023234878627+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9f1b28255977

## What looked useful

Primary 2,000-case run: Anchor-KV accuracy 1.0000, full-KV 1.0000, recency-only 0.1730, random-budget 0.2095; Anchor-KV perplexity 1.0081 versus recency-only 19.6544 and random-budget 17.3359. Five-seed sweep passed the registered threshold on all seeds.

## Boundaries and scale limits

This was a controlled small direct cache-policy test, not a trained small-transformer benchmark. It used synthetic data, a hand-constructed retrieval head, short contexts, and no natural-language corpus or parameter-matched learned baseline.

## Claim scope

In a deterministic NumPy causal attention-style synthetic anchor/value retrieval task with 96-token sequences, 12 anchor/value pairs, and a 16-entry cache budget, Anchor-KV retained anchor-associated value entries and matched full-KV retrieval accuracy and target-token perplexity while outperforming same-budget recency-only and random cache controls.

## Why it stopped

Tier 1 mechanism support was obtained, but the evidence is hand-constructed and synthetic rather than a learned-model confirmation, so the strict paper gate remains closed.

## Recommended next action

Run a bounded learned small-transformer follow-up on the same anchor-retrieval distribution, comparing full-KV, Anchor-KV, recency-only, and random retention under matched cache budgets with retrieval accuracy, NLL/perplexity, and cache/memory diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned small-transformer Anchor-KV retrieval and perplexity confirmation
- Success threshold: Anchor-KV should recover at least 95% of full-KV retrieval accuracy, improve mean target-token NLL by at least 1.0 over recency-only, and pass on at least three fixed seeds or an equivalent robustness sweep.
- Stop condition: Stop if a learned small transformer fails to exceed recency-only by at least 0.25 mean NLL or fails to retain at least 80% of full-KV retrieval accuracy under the matched cache budget after a verified training/evaluation run.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-anchor-kv-retrieval-and-perplexity-confi-014375d417`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
