# Anchor-hash KV with 8-bit summaries for 64k local document QA without RAG

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-hash-kv-with-8-bit-summaries-for-64k-local-document-qa-without-rag-b08ed75a182f`
Run ID: `anchor-hash-kv-with-8-bit-summaries-for-64k-local-document-qa-without-rag-b08ed75a182f-20260602T103748173018+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e07d7bd80473

## What looked useful

At 64k tokens/document, 8-bit SimHash summary routing was near random: recall@8 0.0251 versus random 0.0176. Exact 8-bit anchor buckets reached recall@4 0.9557 and recall@8 0.9997 with median target rank 2, showing the mechanism is viable only as exact anchor bucketing plus disambiguation, not as a general 8-bit semantic summary.

## Boundaries and scale limits

No transformer KV-cache integration, no end-to-end answer generation, no real-document corpus, and no test of noisy/paraphrased/missing anchor extraction. CPU-only benchmark, 512 chunks per document, 128 generated tokens per chunk.

## Claim scope

Synthetic 64k-token local-document QA routing over 24 generated documents and 3,072 entity-value queries. Plain 8-bit SimHash summaries fail as semantic routers; exact 8-bit anchor buckets work when query and chunk share an exactly recoverable anchor.

## Why it stopped

Proxy/mechanism run completed: plain 8-bit summaries are early-falsified as general routers, while exact anchor buckets produce a useful but assumption-dependent signal that is not paper-ready.

## Recommended next action

Run a bounded direct follow-up that implements exact anchor extraction plus bucketed KV lookup in a small local transformer/KV-cache simulator and evaluates real long-document QA routing under paraphrase and repeated-anchor cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV-cache test for exact anchor buckets under noisy long-document QA anchors
- Success threshold: On at least 500 real or semi-real 64k-token QA queries, 8-bit anchor buckets achieve at least 95% target-chunk recall@8, no more than 8 inspected chunks on average, and answer accuracy within 5 percentage points of the best local baseline.
- Stop condition: Stop if anchor extraction fails to identify a matching anchor for more than 20% of answerable queries or if repeated/paraphrased anchors push recall@8 below 80%.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-hash-kv-with-8-bit-summaries-for-64k-local-document-qa-without-rag-b08ed75a182f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
