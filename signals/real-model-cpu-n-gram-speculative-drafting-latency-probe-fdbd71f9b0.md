# Real-Model CPU N-Gram Speculative Drafting Latency Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-cpu-n-gram-speculative-drafting-latency-probe-fdbd71f9b0`
Run ID: `real-model-cpu-n-gram-speculative-drafting-latency-probe-fdbd71f9b0-20260604T011601046157+0000`

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

- Parent run decision: CPU N-Gram Cache Speculative Drafting: enoch://control-plane/projects/cpu-n-gram-cache-speculative-drafting-1c10ec21d00c/runs/cpu-n-gram-cache-speculative-drafting-1c10ec21d00c-20260603T212913746032+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/287d448b6e23

## What looked useful

A real-model CPU Tier 1 probe found exact-output n-gram speculative drafting speedups of 1.07x to 2.16x when draft acceptance was 63.6% to 93.6%; aggregate acceptance was 81.3% and aggregate mean speedup was 1.71x.

## Boundaries and scale limits

Single small real model, three repetition-rich prompts, 48 generated tokens per prompt, one CPU host, one n-gram configuration, no natural-corpus prompt suite, no repeated-run confidence intervals, no larger-model validation.

## Claim scope

On three controlled repeated-context prompts with Qwen/Qwen3-0.6B on CPU, deterministic n-gram speculative drafting preserved exact greedy output and reduced mean latency from 147.29 ms/token to 94.95 ms/token.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is too narrow and controlled for publication readiness.

## Recommended next action

Run a bounded deepen test on a larger natural repeated-context prompt suite with two real causal LMs and n-gram/draft-length ablations; stop if median speedup falls below 1.0x or any exact-output mismatch appears.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Prompt Suite CPU N-Gram Speculative Drafting Confirmation
- Success threshold: All outputs match greedy exactly, no configuration has correctness failures, and the best predeclared configuration reaches at least 1.2x median speedup with at least 1.0x p25 speedup on both models.
- Stop condition: Stop as negative if any exact-output mismatch appears, if median speedup is below 1.0x on either model, or if acceptance below 50% dominates natural prompts.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-n-gram-speculative-drafting-latency-probe-fdbd71f9b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
