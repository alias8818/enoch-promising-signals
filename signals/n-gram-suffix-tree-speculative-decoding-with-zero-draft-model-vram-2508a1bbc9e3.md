# N-gram suffix-tree speculative decoding with zero draft-model VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-tree-speculative-decoding-with-zero-draft-model-vram-2508a1bbc9e3`
Run ID: `n-gram-suffix-tree-speculative-decoding-with-zero-draft-model-vram-2508a1bbc9e3-20260621T051800721937+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8fbf2e47f7f9

## What looked useful

Model-free n-gram/suffix proposers can reduce target verification passes on repetitive or prompt-grounded traces, with best observed pass-reduction bound of 3.646x for prompt_ngram_2 and 2.308x for suffix-cache variants. They provide no benefit on low-repetition random traces or shifted numeric templates, and the tested suffix-cache variants did not beat simpler prompt n-gram lookup.

## Boundaries and scale limits

No real target LLM, no GPU/vLLM/TensorRT-LLM integration, no KV-cache or serving latency measurement, no real benchmark tasks, and no quality/sampling distribution validation.

## Claim scope

Deterministic trace-level oracle simulation of zero-draft-model n-gram and suffix-cache speculative proposers on four synthetic token workloads.

## Why it stopped

Closed as no-paper useful signal because this run is a trace-level proxy and public systems/literature already cover n-gram and suffix-tree draft-model-free speculative decoding.

## Recommended next action

Run a bounded direct vLLM or TensorRT-LLM latency comparison on a small target model using repeated code-edit and prompt-copy prompts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model latency validation for zero-draft-model n-gram versus suffix-cache speculation
- Success threshold: At least 1.25x end-to-end latency improvement over greedy and at least 1.10x over prompt n-gram on a repeated real-model workload, with no output-quality regression and no added draft-model VRAM.
- Stop condition: Stop if suffix-cache speculation is not faster than prompt n-gram after overhead, or if accepted tokens per pass are not high enough to reduce end-to-end latency on the favorable workload.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-tree-speculative-decoding-with-zero-draft-model-vram-2508a1bbc9e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
