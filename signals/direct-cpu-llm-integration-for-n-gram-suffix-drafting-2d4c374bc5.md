# Direct CPU LLM Integration for N-Gram Suffix Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-cpu-llm-integration-for-n-gram-suffix-drafting-2d4c374bc5`
Run ID: `direct-cpu-llm-integration-for-n-gram-suffix-drafting-2d4c374bc5-20260619T075401018447+0000`

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

- Parent run decision: N-Gram Suffix Drafting for Speculative Decoding on CPU: enoch://control-plane/projects/n-gram-suffix-drafting-for-speculative-decoding-on-cpu-704376831413/runs/n-gram-suffix-drafting-for-speculative-decoding-on-cpu-704376831413-20260619T073122500385+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

The direct CPU test showed exact output equality across 6 prompts, 2.566x total speedup, 71.48% target-call reduction, and 97.90% draft acceptance; this supports the mechanism but is too narrow for paper readiness.

## Boundaries and scale limits

One small pretrained model, one controlled prompt suite, greedy decoding only, single-request Python/Hugging Face implementation, weak long-generation non-repetition controls because the target model often degenerated into repetitive continuations.

## Claim scope

In a bounded CPU-only greedy decoding benchmark on distilgpt2, n-gram suffix drafting from prior context preserved exact target token outputs and reduced target-model calls and wall-clock latency on controlled repeated-context prompts.

## Why it stopped

Tier 1 direct validation completed with a useful mechanism signal but insufficient breadth and control quality for publication readiness.

## Recommended next action

Run a bounded corpus-derived direct benchmark with clean low-repetition controls, repeated trials, and a success threshold of exact equality plus >1.10x total speedup on repeated contexts without material overhead on controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Derived Control Benchmark for CPU N-Gram Suffix Drafting
- Success threshold: Exact equality on 100% of prompts, repeated-context total speedup >1.10x, median repeated prompt speedup >1.05x, and low-repetition control slowdown no worse than 5%.
- Stop condition: Stop if any token divergence occurs, repeated-context total speedup is <=1.10x, or low-repetition controls show >5% slowdown after timing-noise checks.

## Evidence references

- Artifact root: `<local-path>/projects/direct-cpu-llm-integration-for-n-gram-suffix-drafting-2d4c374bc5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
