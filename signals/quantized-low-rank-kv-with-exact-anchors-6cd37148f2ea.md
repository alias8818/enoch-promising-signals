# Quantized Low-Rank KV with Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-low-rank-kv-with-exact-anchors-6cd37148f2ea`
Run ID: `quantized-low-rank-kv-with-exact-anchors-6cd37148f2ea-20260607T185355219442+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e787b6d18d00

## What looked useful

On structured_mixed synthetic KV, anchor_lowrank_q4 achieved median relative output error 0.0245 and improved over matched lowrank_q4 in 100% of configs with median error ratio 0.0468. On a distilgpt2 512-token trace, anchor_lowrank_q4 had median layer error 0.0571 at 7.76x estimated compression and improved over lowrank_q4 in all 6 layers. On random full-rank KV, median error remained high at 0.860.

## Boundaries and scale limits

No end-to-end perplexity, logit-KL, long-context generation, latency, production kernel, or large-model validation was run. Random full-rank KV remains a clear failure case.

## Claim scope

Bounded proxy evidence: exact anchors plus q4 low-rank residuals reduce attention-output reconstruction error versus q4 low-rank alone and anchors alone on structured synthetic KV and a distilgpt2 Q/K/V trace.

## Why it stopped

Closed as no-paper useful signal because current evidence is attention-output reconstruction and trace/proxy evidence only, not a full language-model or serving validation.

## Recommended next action

Run a bounded deepen follow-up that substitutes the compressed KV cache during real autoregressive distilgpt2/GPT-2-small evaluation and measures logit KL and perplexity against a full-KV baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive GPT-2 KV-cache substitution test for exact-anchor q4 low-rank compression
- Success threshold: At >=4x estimated KV compression, exact-anchor q4 low-rank has median logit KL <=0.05 or perplexity degradation <=5% and beats both q4 low-rank only and anchors only on the same snippets.
- Stop condition: Stop if all >=4x configurations exceed median logit KL 0.1 or perplexity degradation 10%, or if the method fails to beat either component baseline.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-low-rank-kv-with-exact-anchors-6cd37148f2ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
