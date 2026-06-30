# Eviction-policy comparison for KV cache on GB10: sliding window vs H2O vs learned sparse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `eviction-policy-comparison-for-kv-cache-on-gb10-sliding-window-vs-h2o-vs-learned-sparse-5090a0bf361f`
Run ID: `eviction-policy-comparison-for-kv-cache-on-gb10-sliding-window-vs-h2o-vs-learned-sparse-5090a0bf361f-20260610T094751808974+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86984726c00f

## What looked useful

Across five calibrated seeds, sliding window retained the most attention mass (mean 0.993171), H2O preserved injected long-range anchors best (0.000000 anchor miss), and the learned sparse MLP was mixed: better retained mass than H2O (0.858727 vs 0.759303) but below sliding window and seed-variable. GB10 synthetic KV gather latencies were effectively indistinguishable at about 0.010-0.011 ms.

## Boundaries and scale limits

Proxy-only evidence: no real LLM perplexity, task accuracy, output equivalence, fused attention kernel, paged cache manager, or end-to-end serving throughput was measured. The learned policy was trained on generated traces and evaluated on held-out generated decode steps, not real model activations.

## Claim scope

Bounded synthetic KV-cache eviction comparison on GB10 using generated long-context attention traces at seq_len=4096, retained-token budget=512, and GPU index_select gather timing for synthetic KV tensors.

## Why it stopped

Proxy-only bounded evidence is insufficient for a paper-positive claim; it supports a mixed mechanism signal rather than full validation.

## Recommended next action

Stop this proxy run as no-paper useful signal; the next concrete test should embed the three policies into a small real decoder and measure perplexity or task accuracy plus decode latency on real prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder KV eviction comparison for sliding window, H2O, and learned sparse selectors
- Success threshold: Learned sparse must improve long-range retrieval accuracy or anchor-hit rate by at least 5 percentage points over sliding window while staying within 1% perplexity degradation and 5% decode-latency overhead at the same KV budget.
- Stop condition: Stop if learned sparse fails to beat sliding window on either real-task quality or long-range retrieval at equal budget, or if policy overhead exceeds 5% decode latency without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/eviction-policy-comparison-for-kv-cache-on-gb10-sliding-window-vs-h2o-vs-learned-sparse-5090a0bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
