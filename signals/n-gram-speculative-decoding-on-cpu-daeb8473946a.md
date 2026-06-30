# N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-daeb8473946a`
Run ID: `n-gram-speculative-decoding-on-cpu-daeb8473946a-20260527T024413154126+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01d3df5daa94

## What looked useful

High repetition produced 0.92-1.00 acceptance, 82-88% target-call reduction, and 1.35-2.56x CPU proxy speedups. Alice in Wonderland prose produced only 0.1-0.9% target-call reduction and 0.82-0.99x speed, so broad CPU benefit is unsupported.

## Boundaries and scale limits

No real transformer, KV cache, tokenizer, sampling mode, or production serving stack was benchmarked. The public prose trace used whitespace tokens from one book; synthetic traces intentionally bracket repetition extremes. Results are not publication-grade LLM inference evidence.

## Claim scope

A self-contained CPU proxy benchmark shows n-gram prompt-lookup speculative decoding can reduce target calls and improve wall-clock speed on highly repetitive token streams, but does not improve and can slow down ordinary prose traces under the tested settings.

## Why it stopped

Proxy and trace evidence is mixed: the mechanism works on repeated contexts but fails to produce speedup on ordinary prose, so this is not a broad or paper-ready validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen only with a direct llama.cpp or equivalent CPU CausalLM benchmark on repetition-heavy code/RAG/editing traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM Benchmark for N-Gram Speculation on Repetition-Heavy Workloads
- Success threshold: At least 1.25x median tokens/sec speedup with identical greedy outputs on two repetition-heavy workload classes, while prose/control traces do not regress by more than 5%.
- Stop condition: Stop if accepted-token rate stays below 20% or target-call reduction below 15% on all repetition-heavy traces, or if wall-clock speedup remains below 1.10x after n-gram and draft-length sweeps.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-daeb8473946a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
