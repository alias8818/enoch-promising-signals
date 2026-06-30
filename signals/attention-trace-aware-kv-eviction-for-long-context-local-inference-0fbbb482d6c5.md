# Attention-trace-aware KV eviction for long-context local inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `attention-trace-aware-kv-eviction-for-long-context-local-inference-0fbbb482d6c5`
Run ID: `attention-trace-aware-kv-eviction-for-long-context-local-inference-0fbbb482d6c5-20260613T175001619533+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d25e02f83924

## What looked useful

Decayed attention traces can change eviction choices beyond lifetime cumulative attention: at decay 0.90, retained attention mass improved over H2O-style cumulative scoring by +0.0208, +0.0217, and +0.0300 at budgets 32, 64, and 128 respectively. Structural sink+recent protection explained a large share of the gain over pure recency.

## Boundaries and scale limits

Proxy-only attention replay; no patched KV-cache generation, no perplexity or task-quality measurement, no throughput measurement, synthetic fallback texts, distilgpt2 only, and maximum tested sequence length was 512 tokens.

## Claim scope

On distilgpt2 512-token attention-trace replay over 8 synthetic long-context sequences, a sink+recent-protected exponentially decayed attention trace with decay 0.90 preserved more full-cache attention mass than pure recency, sink+recent, and H2O-style cumulative attention at budgets 32, 64, and 128.

## Why it stopped

No-paper closure: the run produced a useful proxy signal but not direct generated-quality or production-inference evidence.

## Recommended next action

Run a bounded patched-cache autoregressive evaluation on a small local model comparing decay-trace, H2O cumulative, sink+recent, and recency on perplexity and exact-generation quality at equal KV budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Patched-cache generation test for decayed attention-trace KV eviction
- Success threshold: At two or more tested budgets, decayed trace must reduce next-token loss delta versus H2O cumulative by at least 5% relative without worse wall-clock or memory than the same-budget baseline.
- Stop condition: Stop if patched-cache decoding shows no loss-quality improvement over H2O cumulative at budget 64 or 128, or if implementation overhead eliminates any plausible local-inference benefit.

## Evidence references

- Artifact root: `<local-path>/projects/attention-trace-aware-kv-eviction-for-long-context-local-inference-0fbbb482d6c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
