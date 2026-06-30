# Entropy-based local cascade router for GPT-2 family serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-based-local-cascade-router-for-gpt-2-family-serving-b57beb8e1e60`
Run ID: `entropy-based-local-cascade-router-for-gpt-2-family-serving-b57beb8e1e60-20260530T065423868212+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7f71c05face3

## What looked useful

Entropy routing beat random matched-fraction routing in both bounded runs, but entropy AUROC for identifying tokens where the larger model had lower NLL was weak: 0.5498 for distilgpt2->gpt2 and 0.5056 for gpt2->gpt2-medium. At 50% large-model routing, cascades improved over small-only NLL but retained meaningful gaps to large-only NLL.

## Boundaries and scale limits

Tested only 12,288 token decisions for distilgpt2->gpt2 and 4,096 token decisions for gpt2->gpt2-medium on WikiText-2 validation. Did not test end-to-end autoregressive serving latency, KV-cache scheduling, dynamic batching, request-level quality, larger corpora, or generation metrics.

## Claim scope

Bounded WikiText-2 token-level evidence for GPT-2-family local cascades shows entropy-only routing consistently improves next-token NLL over random same-budget routing, but only modestly and with weak classifier signal.

## Why it stopped

No-paper useful signal: bounded direct token-NLL tests show entropy-only routing is better than random but too weak to support a publication-grade local cascade claim.

## Recommended next action

Stop this entropy-only paper path; if continuing, run a bounded deepen test with richer router features and true KV-cache decode latency before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Feature-Rich GPT-2 Cascade Router With KV-Cache Decode Benchmark
- Success threshold: At a fixed large-model-call fraction of 30% to 50%, the richer router should reduce NLL by at least 0.05 versus entropy-only routing and improve measured tokens/s or latency-normalized NLL versus always-large under the same local serving harness.
- Stop condition: Stop if richer-router AUROC remains below 0.60 or if KV-cache decode measurements show no latency-normalized advantage over always-large or simple random routing.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-based-local-cascade-router-for-gpt-2-family-serving-b57beb8e1e60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
