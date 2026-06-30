# N-Gram Draft Speculative Decoding for Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-local-llms-1db2d507cdc2`
Run ID: `n-gram-draft-speculative-decoding-for-local-llms-1db2d507cdc2-20260524T012757340834+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c67014ae553a

## What looked useful

Exact n-gram drafting appears workload-dependent: weak on broad natural prose, strong on repeated text, and modestly positive on a small generated trace. It is worth testing only where prompts or outputs contain repeated boilerplate, code, or document-editing structure.

## Boundaries and scale limits

No 7B-class local serving benchmark was run; GPT-2 trace covered only eight short generations and 1,481 total tokens; verifier batch-cost model is analytical rather than measured in llama.cpp or vLLM.

## Claim scope

Offline exact n-gram prompt-lookup drafting over 120k-token natural text streams is near break-even under a conservative verifier batch-cost model, while a small GPT-2 generated trace shows a modest 1.084x conservative speedup and repeated synthetic text shows the mechanism can work when exact continuations are common.

## Why it stopped

Closed as no-paper useful signal: offline and small-model evidence is mixed and insufficient for a broad local-LLM acceleration claim.

## Recommended next action

Run a direct llama.cpp or vLLM throughput benchmark for n-gram prompt lookup on a 7B-class local model with separate general-chat, code, and repetition-rich prompt suites; stop if the geometric mean speedup is below 1.15x at equal output quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 7B Local Serving Benchmark for N-Gram Prompt Lookup
- Success threshold: Geometric mean tokens/sec speedup >= 1.15x on repetition-rich tasks with no more than 2% slowdown on general chat and no quality regression by deterministic or paired human-free checks.
- Stop condition: Stop if a 50-prompt pilot shows <1.05x repetition-rich speedup or >5% general-chat slowdown, because the offline signal is too small to justify broader local serving work.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-local-llms-1db2d507cdc2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
