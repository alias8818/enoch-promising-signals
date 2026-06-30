# N-gram speculative decoding for CPU model cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-cpu-model-cascade-a5ce021377f2`
Run ID: `n-gram-speculative-decoding-for-cpu-model-cascade-a5ce021377f2-20260527T185920998933+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba419e89fff0

## What looked useful

N-gram speculation strongly helps highly repetitive traces, reaching 5.6x to 6.5x modeled speedup on synthetic boilerplate, but natural word-token traces showed effectively no useful gain: best modeled speedups were 1.0019x on Alice and 1.00005x on Tiny Shakespeare.

## Boundaries and scale limits

No real LLM tokenizer, neural drafter, target model, or measured transformer verification latency was used. Corpora were capped at 350k characters and results are proxy evidence, not full model-cascade validation.

## Claim scope

Trace-driven proxy for n-gram prompt-lookup speculative decoding on two natural text corpora and one repetitive synthetic corpus, using char and word tokenization with a simple CPU verification cost model.

## Why it stopped

Proxy evidence is mixed and not paper-ready: the mechanism works on repetitive traces but natural word-token traces fail to produce meaningful modeled speedup.

## Recommended next action

Run a bounded deepen test with a real LLM tokenizer and CPU target model on repeated-document prompts; otherwise stop treating plain n-gram cascade speculation as broadly useful for natural word-token generation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer CPU prompt-lookup speculative decoding benchmark
- Success threshold: At least 10% wall-clock tokens/second improvement over no-drafter baseline on repeated-span workloads without more than 2% regression on ordinary prose.
- Stop condition: Stop if real-tokenizer acceptance on repeated-span prompts is below 5% or if measured verification overhead eliminates speedup in two independent workloads.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-model-cascade-a5ce021377f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
