# Speculative Decode via Residual Channel Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decode-via-residual-channel-draft-model-afdfca9c57ba`
Run ID: `speculative-decode-via-residual-channel-draft-model-afdfca9c57ba-20260605T033141088361+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6bd3f315dc2e

## What looked useful

Across three held-out runs, residual extrapolation improved one-step acceptance over the trigram control by only about 0.00025 on average, while KL and observed perplexity were worse and sampled gamma-token block deltas were mixed. Future neural versions should include a plain intermediate-layer LM-head control because residual extrapolation alone may not add meaningful acceptance.

## Boundaries and scale limits

This is not transformer, neural-head, subword, large-model, or latency evidence. It does not validate or falsify residual-channel draft models in real LLM serving; it only tests a transparent n-gram analogue of residual refinement and speculative acceptance.

## Claim scope

CPU-bounded n-gram proxy: a validation-calibrated residual log-probability extrapolation draft was compared with unigram, bigram, and trigram drafts against a smoothed 4-gram character target on Tiny Shakespeare. The residual draft beats weaker unigram/bigram drafts but does not materially or quality-consistently beat the plain trigram intermediate-channel control.

## Why it stopped

Proxy early falsification of the residual-extrapolation mechanism: the tested residual draft did not materially outperform the direct intermediate-channel trigram control on the primary acceptance metric and was worse on KL/perplexity.

## Recommended next action

Stop this run as a no-paper proxy result; a bounded follow-up should test a neural residual draft head on a small transformer against a same-layer plain LM-head control before any larger-scale serving experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer Residual Draft Head vs Same-Layer LM Head
- Success threshold: Residual-channel draft improves mean accepted tokens by at least 5% over the same-layer plain LM-head control without worse draft perplexity or higher measured draft cost.
- Stop condition: Stop if the residual head fails to beat the same-layer plain LM-head control by at least 1% accepted-token improvement after a small-model validation run.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decode-via-residual-channel-draft-model-afdfca9c57ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
