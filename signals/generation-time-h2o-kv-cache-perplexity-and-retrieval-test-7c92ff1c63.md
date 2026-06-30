# Generation-time H2O KV-cache perplexity and retrieval test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `generation-time-h2o-kv-cache-perplexity-and-retrieval-test-7c92ff1c63`
Run ID: `generation-time-h2o-kv-cache-perplexity-and-retrieval-test-7c92ff1c63-20260529T163033316561+0000`

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

- Parent run decision: H2O heavy-hitter KV eviction for long local context: enoch://control-plane/projects/h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4/runs/h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4-20260529T064021255382+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

H2O-style pruning produced PPL 33.36 vs full-cache 26.47 and recent-only 1070.17 on a 512-token Wikitext-2 stream; on passkey answer tokens, H2O NLL was 1.36 vs full 1.83 and recent-only 18.41, with mean rank 2.0 vs 3.0 and 11846.5 respectively.

## Boundaries and scale limits

One 124M-parameter GPT-2 model, one seed, 512 Wikitext-2 tokens, one synthetic passkey prompt, one cache budget, no long-context or production serving benchmark, and no exact passkey argmax success.

## Claim scope

On a bounded GPT-2 Tier 1 direct test, generation-time H2O-style heavy-hitter plus recency KV pruning at a 128-token cache cap preserved next-token perplexity and passkey answer likelihood far better than a same-size recent-only cache.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is too narrow for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with multi-budget curves and multiple retrieval prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-budget generation-time H2O KV-cache curves on perplexity and passkey retrieval
- Success threshold: H2O PPL ratio to full cache <= 1.35 at budgets 128 and 256, H2O PPL at least 3x better than recent-only, and H2O improves answer NLL or rank over recent-only on at least 80% of passkey prompts.
- Stop condition: Stop if H2O fails to beat recent-only by at least 2x PPL at budget 128 or does not improve passkey NLL/rank on a majority of prompts.

## Evidence references

- Artifact root: `<local-path>/projects/generation-time-h2o-kv-cache-perplexity-and-retrieval-test-7c92ff1c63`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
