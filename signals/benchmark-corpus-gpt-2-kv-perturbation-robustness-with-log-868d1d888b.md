# Benchmark-corpus GPT-2 KV perturbation robustness with logit and generation metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `benchmark-corpus-gpt-2-kv-perturbation-robustness-with-log-868d1d888b`
Run ID: `benchmark-corpus-gpt-2-kv-perturbation-robustness-with-log-868d1d888b-20260523T195131193357+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Held-out end-to-end GPT-2 KV residual decode test: enoch://control-plane/projects/held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3/runs/held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3-20260523T192913400832+0000
- Parent run decision: Multi-corpus GPT-2 KV residual decode robustness test: enoch://control-plane/projects/multi-corpus-gpt-2-kv-residual-decode-robustness-test-0c0ea680bd/runs/multi-corpus-gpt-2-kv-residual-decode-robustness-test-0c0ea680bd-20260523T194442920991+0000

## What looked useful

4096 WikiText-103 windows and 262144 continuation tokens showed almost no NLL movement for KV Gaussian sigma 0.003-0.03, moderate degradation at 0.1, severe degradation at 0.3-1.0, and strong collapse for zero-cache control. Generation diverged earlier than logit metrics: sigma 0.03 retained only 0.667 clean-token agreement despite delta NLL of 0.0026; sigma 0.1 retained 0.344 agreement with delta NLL of 0.0279.

## Boundaries and scale limits

Single model family member, one benchmark corpus split, fixed seed/lengths, greedy decoding only, synthetic inference-time perturbations only, random overlapping windows from about 286k corpus tokens; no larger-model, multi-corpus, sampled-decoding, or training-time robustness validation.

## Claim scope

On GPT-2 small with cached WikiText-103 test windows, inference-time Gaussian perturbations to the prefix KV cache show smooth logit degradation by perturbation scale; very small perturbations preserve one-step continuation logits, while greedy generation is substantially more sensitive.

## Why it stopped

Direct bounded validation produced a useful scoped signal but not a paper-positive claim or new method; evidence is limited to GPT-2 small on WikiText-103 with synthetic inference-time KV perturbations.

## Recommended next action

Stop this run as no-paper useful evidence; if one more bounded follow-up is allowed at depth 3, test whether the logit-vs-generation sensitivity gap persists across distilgpt2/gpt2-medium, a second corpus, and sampled decoding with confidence intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-model and sampled-decoding validation of GPT-2 KV perturbation sensitivity gap
- Success threshold: Across at least two models and two corpora, sigma 0.03 should keep delta NLL below 0.01 while reducing clean-generation token agreement by at least 20 percentage points versus sigma 0.003; zero-cache must remain a strong destructive control.
- Stop condition: Stop if the sensitivity gap fails on either the second model or second corpus, or if sampled decoding removes the effect under fixed seeds and matched prompts.

## Evidence references

- Artifact root: `<local-path>/projects/benchmark-corpus-gpt-2-kv-perturbation-robustness-with-log-868d1d888b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
