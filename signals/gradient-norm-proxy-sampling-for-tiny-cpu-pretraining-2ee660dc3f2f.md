# Gradient-Norm Proxy Sampling for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-proxy-sampling-for-tiny-cpu-pretraining-2ee660dc3f2f`
Run ID: `gradient-norm-proxy-sampling-for-tiny-cpu-pretraining-2ee660dc3f2f-20260604T004101338641+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0464243693d3

## What looked useful

The proxy is technically faithful to true gradient norm in the tested model, but gradient magnitude alone is insufficient as a sampling rule because noisy high-gradient examples receive extra sampling probability. An oracle clean-only proxy sampler performs much better, indicating that usefulness filtering is the key missing component.

## Boundaries and scale limits

Synthetic Markov-token data only; tiny embedding/MLP causal predictor only; 3 seeds per clean/noisy condition; 500 training steps per sampler; not a natural-language tokenizer, Transformer, GPT-2-small-class, or long-run validation.

## Claim scope

Bounded synthetic tiny-CPU next-token pretraining probe: a forward-pass output-layer gradient-norm proxy correlates with true per-example gradient norm, but naive probability-proportional proxy sampling does not reliably improve clean validation loss versus uniform sampling and slightly underperforms when 25% noisy distractor sequences are present.

## Why it stopped

Proxy/local early falsification of naive gradient-norm proxy sampling as a standalone pretraining sampler; it measures gradient norm well but does not produce robust validation-loss gains in the bounded direct training test.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up implementing a deployable capped or filtered proxy sampler and require improvement over both uniform and naive proxy sampling on the mixed-corpus benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Capped or Filtered Gradient-Proxy Sampling for Noisy Tiny Pretraining
- Success threshold: On the 25% noisy benchmark, the filtered/capped proxy sampler must improve mean clean validation loss by at least 0.03 versus uniform and by at least 0.04 versus naive grad_proxy across 3 seeds, while selecting no more than 27% noisy examples in expectation.
- Stop condition: Stop if the filtered/capped sampler fails to beat uniform by the threshold, selects more than 27% noisy examples, or only succeeds through oracle clean/noise labels.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-proxy-sampling-for-tiny-cpu-pretraining-2ee660dc3f2f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
