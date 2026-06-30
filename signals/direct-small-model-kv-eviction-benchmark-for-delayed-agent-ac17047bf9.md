# Direct Small-Model KV Eviction Benchmark for Delayed Agent Facts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-small-model-kv-eviction-benchmark-for-delayed-agent-ac17047bf9`
Run ID: `direct-small-model-kv-eviction-benchmark-for-delayed-agent-ac17047bf9-20260527T040333326453+0000`

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

- Parent run decision: Importance-Gated KV Eviction for Long Agent Traces: enoch://control-plane/projects/importance-gated-kv-eviction-for-long-agent-traces-4d1fcfd2d227/runs/importance-gated-kv-eviction-for-long-agent-traces-4d1fcfd2d227-20260524T180235537889+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

Two small pretrained causal LMs showed consistent paired degradation from evicting the fact KV span: gpt2 mean fact-vs-control answer-logprob delta -3.7246 with 95% bootstrap CI [-3.8509, -3.5998], and distilgpt2 delta -2.5037 with CI [-2.6948, -2.3215]. All 96 paired trials per model moved in the negative direction.

## Boundaries and scale limits

Tested only gpt2 and distilgpt2 on 96 trials each, with single color facts, candidate log-likelihood scoring, and delays up to 512 tokens. It does not validate real agent traces, instruction-tuned chat models, long-context models, learned eviction policies, or serving-scale memory/latency tradeoffs.

## Claim scope

In a controlled synthetic delayed-fact task on GPT-2-small-class causal LMs, targeted eviction of the cached token span containing the fact substantially reduces later answer-token likelihood compared with full cache and same-width distractor eviction controls.

## Why it stopped

No-paper useful signal: this run produced direct small-model mechanism evidence, but it is synthetic and too narrow for publication readiness.

## Recommended next action

Run a bounded deepen test on an instruction-tuned small model with agent-like multi-fact transcripts, matched non-fact eviction controls, and a pre-registered success threshold for both accuracy and answer log-likelihood.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Instruction-Tuned Agent-Trace KV Fact Eviction Benchmark
- Success threshold: Across at least 200 paired trials, fact-span eviction should reduce answer log-likelihood versus matched non-fact eviction with a bootstrap 95% CI entirely below -0.5 nats and reduce forced-choice accuracy by at least 10 percentage points.
- Stop condition: Stop if full-cache accuracy is below 50% on the task or if the paired fact-vs-control answer-logprob CI overlaps 0 after the planned trial count.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-model-kv-eviction-benchmark-for-delayed-agent-ac17047bf9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
