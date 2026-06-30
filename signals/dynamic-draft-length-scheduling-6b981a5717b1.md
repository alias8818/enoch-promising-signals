# Dynamic Draft Length Scheduling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-draft-length-scheduling-6b981a5717b1`
Run ID: `dynamic-draft-length-scheduling-6b981a5717b1-20260604T041404854398+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f1841f57fa90

## What looked useful

Dynamic scheduling reduced target calls by roughly 20% versus prompt-best fixed baselines but increased draft calls by roughly 40%, producing mean paired wall-clock slowdowns of 5.1% for dynamic_streak and 5.8% for dynamic_ema_cost. Target-call reduction alone is an insufficient objective for this setup.

## Boundaries and scale limits

Tested 16 prompts, 48 generated tokens per prompt, greedy decoding, one small target/draft pair, straightforward Transformers inference, and two simple controllers. Not tested: optimized serving kernels, larger 7B+/70B pairs, batched traffic, entropy/learned predictors, tree speculation, or long-context reasoning workloads.

## Claim scope

On a small deterministic CUDA speculative-decoding benchmark using gpt2 as target and distilgpt2 as draft, two simple reactive dynamic draft length schedulers preserved exact greedy output and reduced target verification calls, but did not beat the best fixed draft length on wall-clock latency.

## Why it stopped

Local direct benchmark produced a mixed/negative result for simple dynamic schedulers: exactness and target-call savings were achieved, but wall-clock latency lost to fixed gamma=1 and to prompt-best fixed baselines. This is a proxy-scale early falsification of the simple-controller hypothesis, not a full rejection of dynamic draft length scheduling in optimized large-model systems.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add an entropy or acceptance-probability predictor and require paired wall-clock wins against best fixed gamma, not just fewer target calls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy-Calibrated Draft Length Scheduling
- Success threshold: Mean paired wall-clock ratio below 0.97 versus prompt-best fixed gamma, with wins on at least 10 of 16 prompts and zero exact-output mismatches.
- Stop condition: Stop if entropy/predictor scheduling still loses to prompt-best fixed gamma on mean paired wall-clock or introduces any exact-output mismatch.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-draft-length-scheduling-6b981a5717b1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
