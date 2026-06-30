# Direct CPU LLM benchmark for n-gram prompt-lookup speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-cpu-llm-benchmark-for-n-gram-prompt-lookup-speculat-11159661e0`
Run ID: `direct-cpu-llm-benchmark-for-n-gram-prompt-lookup-speculat-11159661e0-20260607T050708286333+0000`

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

- Parent run decision: N-gram speculative CPU decoding: enoch://control-plane/projects/n-gram-speculative-cpu-decoding-934122555113/runs/n-gram-speculative-cpu-decoding-934122555113-20260607T012505183104+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6b86760bd48b

## What looked useful

Prompt-lookup speculative decoding produced a strong bounded CPU latency signal on distilgpt2: median baseline latency was 2.4403 s, prompt-lookup latency was 0.7959 s, median speedup was 3.066x, and requested-length token-prefix equivalence was 100%. The result is useful for deciding to run a larger robustness benchmark, but not enough for a paper.

## Boundaries and scale limits

One small model, one library implementation, one CPU host, small controlled prompt suite, no batching or serving stack, no sampling modes, no long-context corpus, and no 7B-class model validation. Prompt lookup returned 66 tokens instead of the requested 64 in 9 of 18 assisted runs, so full termination semantics need further characterization.

## Claim scope

On a CPU-only direct benchmark using distilgpt2, 6 controlled prompts, 64 requested new tokens, greedy decoding, and 3 repeats per condition, Hugging Face prompt-lookup assisted generation reduced median wall-clock latency by 3.066x versus baseline greedy generation while preserving the first 64 generated tokens in all 18 matched comparisons.

## Why it stopped

Tier 1 direct validation target was met and produced a useful no-paper signal; publication-grade claims require broader model/prompt/serving robustness and characterization of the observed max_new_tokens overshoot.

## Recommended next action

Run a bounded medium confirmation on 2-3 larger CPU-feasible or quantized causal LMs with natural repeated-context prompts, explicit requested-length and full-length equivalence checks, and serving-style latency accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium CPU robustness benchmark for prompt-lookup speculative decoding
- Success threshold: At least 1.5x median speedup on repeated-context prompts, no more than 10% slowdown on low-repeat controls, 100% requested-length token-prefix equivalence, and characterized full-length/termination behavior.
- Stop condition: Stop if speedup falls below 1.2x median on two model families, requested-length token-prefix equivalence is below 99%, or max_new_tokens overrun cannot be bounded or explained.

## Evidence references

- Artifact root: `<local-path>/projects/direct-cpu-llm-benchmark-for-n-gram-prompt-lookup-speculat-11159661e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
