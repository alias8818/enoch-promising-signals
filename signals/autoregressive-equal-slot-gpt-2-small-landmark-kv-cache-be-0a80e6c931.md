# Autoregressive equal-slot GPT-2-small landmark KV-cache benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `autoregressive-equal-slot-gpt-2-small-landmark-kv-cache-be-0a80e6c931`
Run ID: `autoregressive-equal-slot-gpt-2-small-landmark-kv-cache-be-0a80e6c931-20260602T101700820005+0000`

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

- Parent run decision: Fixed-anchor landmark KV pooling on GPT-2-small: enoch://control-plane/projects/fixed-anchor-landmark-kv-pooling-on-gpt-2-small-923fbb1e84b1/runs/fixed-anchor-landmark-kv-pooling-on-gpt-2-small-923fbb1e84b1-20260531T234130899768+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/14e8254f30b8

## What looked useful

With 48 examples, 48 records per prompt, mean prefix length 739 tokens, and a 96-slot budget, landmark cache improved mean target-token NLL over sliding by 0.513 nats and won 29/48 paired examples. At 192 slots it improved mean NLL by 0.740 nats and won 47/48 examples. Landmark remained 6.34 to 7.94 nats worse than full cache and did not improve accuracy.

## Boundaries and scale limits

Only pretrained GPT-2-small was tested; prompts were synthetic; landmark selection was oracle/query-aware; no training, autonomous landmark selector, natural long-context workload, larger model, or publication-grade robustness study was run. Full-context behavior was not recovered and top-1 accuracy remained near zero.

## Claim scope

In a controlled GPT-2-small CPU inference benchmark with synthetic key-value records and oracle/query-aware landmark selection, an equal-slot landmark KV cache improved target-token NLL over a recency-only sliding cache when the queried fact was outside the sliding window.

## Why it stopped

Bounded Tier 1 direct test completed: equal-slot landmarking beat sliding on NLL but failed to recover full-context likelihood or top-1 accuracy, so the evidence supports only a narrow mechanism signal rather than publication readiness.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should add target-rank/top-k diagnostics and header/fact/tail cache ablations before attempting any trained or natural-workload landmark selector.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small landmark KV-cache rank and span-ablation diagnostics
- Success threshold: A follow-up is useful if an equal-slot non-sliding cache improves target-token NLL over sliding by at least 0.5 nats, improves top-10 target inclusion by at least 10 percentage points, and reduces the landmark-minus-full NLL gap below 4 nats on the 48-example benchmark.
- Stop condition: Stop if span ablations do not improve top-k/rank metrics over the current oracle fact landmark policy or if full-cache accuracy/rank remains too weak to support interpretable recall conclusions.

## Evidence references

- Artifact root: `<local-path>/projects/autoregressive-equal-slot-gpt-2-small-landmark-kv-cache-be-0a80e6c931`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
