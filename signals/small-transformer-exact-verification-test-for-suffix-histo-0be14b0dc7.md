# Small-transformer exact-verification test for suffix-history drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-transformer-exact-verification-test-for-suffix-histo-0be14b0dc7`
Run ID: `small-transformer-exact-verification-test-for-suffix-histo-0be14b0dc7-20260619T081203622657+0000`

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

- Parent run decision: Suffix-Tree Drafter Accelerates Long-Context Decoding Without Quality Loss: enoch://control-plane/projects/suffix-tree-drafter-accelerates-long-context-decoding-without-quality-loss-2b2da2e3076b/runs/suffix-tree-drafter-accelerates-long-context-decoding-without-quality-loss-2b2da2e3076b-20260619T075142194008+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e33b636a484

## What looked useful

Suffix-history drafting passed the Tier 1 direct threshold: mean exact token hit rate was 0.9843 versus 0.0347 for unigram and 0.0315 for shuffled suffix history; mean accepted length over an 8-token draft horizon was 7.246 versus 0.036 for unigram and 0.033 for shuffled suffix. The shuffled control shows correct suffix-token alignment, not unigram skew or table coverage alone, drives the effect.

## Boundaries and scale limits

Synthetic suffix-structured data only; tiny target model only; greedy exact-match verifier only; no natural-language corpus, GPT-2-small-class baseline, stochastic verifier, neural drafter comparison, KV-cache integration, or end-to-end latency measurement.

## Claim scope

In a synthetic order-3 suffix-process setting, a 349k-parameter causal Transformer trained from scratch was exactly greedily verified against suffix-history draft tokens. Across three seeds, training-corpus suffix histograms produced high multi-token exact acceptance and strongly beat unigram and shuffled-suffix controls.

## Why it stopped

Tier 1 small direct test completed and supports the mechanism, but the evidence remains synthetic/tiny-model only and is not paper-positive.

## Recommended next action

Run a bounded natural-language follow-up using a GPT-2-small-class target on a fixed public corpus, measuring exact greedy acceptance and latency against shuffled suffix, n-gram, retrieval, and small neural draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small exact-verification test for suffix-history drafting on natural text
- Success threshold: At least 2x token hit rate over shuffled suffix and unigram controls, at least +0.5 mean accepted tokens per 8-token draft over the best non-neural control, and no latency regression after verification overhead on the bounded setup.
- Stop condition: Stop as unsupported if suffix-history fails to beat shuffled suffix by 1.5x token hit rate or fails to add +0.25 mean accepted tokens after matched-memory tuning.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-exact-verification-test-for-suffix-histo-0be14b0dc7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
