# H2O+SlidingWindow KV eviction on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `h2o-slidingwindow-kv-eviction-on-gb10-1b1dedd032f6`
Run ID: `h2o-slidingwindow-kv-eviction-on-gb10-1b1dedd032f6-20260528T191954383022+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6b9b255ca769

## What looked useful

Across three seeds, pure H2O raised MSE versus sliding by 39.4%, 101.2%, and 272.7% at budgets 64, 128, and 256 respectively. The 50/50 hybrid stayed within about 0.5% MSE of sliding and did not improve retained full-attention mass. Single-seed 25% and 75% hybrid-window ablations also failed to produce a meaningful win.

## Boundaries and scale limits

No trained LLM weights, no downstream perplexity or task metric, no long-context prompt suite, no production serving integration, and no latency claim because policy-order CUDA warmup affects timing.

## Claim scope

On synthetic online causal-attention traces on GB10 at sequence length 1024, 8 heads, head dimension 64, fp16, and cache budgets 64/128/256, H2O-style accumulated-score KV retention underperforms sliding-window retention, and a recent-plus-H2O hybrid does not materially improve fidelity over sliding.

## Why it stopped

Synthetic online-attention evidence does not support the H2O+sliding hybrid as meaningfully better than sliding; this is not a full real-model validation.

## Recommended next action

Stop this run as a proxy early falsification; the only worthwhile next step is a bounded real-model attention-trace replay before considering any larger GB10 serving experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace replay for H2O+sliding KV eviction
- Success threshold: Hybrid beats sliding by at least 5% lower mean attention-output MSE or at least 2 percentage points higher retained full-attention mass at two or more budgets, with no more than 10% policy-overhead regression.
- Stop condition: Stop if hybrid remains within noise of sliding or if H2O-selected non-recent tokens do not correspond to persistent high-attention tokens on trained-model traces.

## Evidence references

- Artifact root: `<local-path>/projects/h2o-slidingwindow-kv-eviction-on-gb10-1b1dedd032f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
