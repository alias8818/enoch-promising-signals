# Context-Local N-Gram Speculative Drafting with Zero Extra VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d`
Run ID: `context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d-20260528T232933276261+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/792c980d2760

## What looked useful

A CPU-side n-gram proposer using only prompt/generated context accepted multi-token drafts often enough to cut ideal verifier calls from 1152 to 187 on repeated prompts and from 1152 to 275 on a low-repeat synthetic control, with observed target GPU allocation under 0.71 GB.

## Boundaries and scale limits

Evidence is limited to synthetic prompts, GPT-2-small greedy continuations, and trace replay. It does not establish production wall-clock speedup, natural-corpus robustness, sampling behavior, or modern 1B-7B+ model performance.

## Claim scope

On synthetic GPT-2-small greedy traces, context-local token n-gram drafting can reduce ideal target verifier calls by 76-84% without a separate draft model or additional GPU-resident draft weights.

## Why it stopped

Bounded useful signal only: the run measured trace-level verifier-call reduction, not production latency or broad workload validity.

## Recommended next action

Implement an exact live KV-cache speculative decoder and evaluate wall-clock tokens/s plus VRAM delta on natural long-context corpora before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live KV-Cache Context N-Gram Speculative Decoder on Natural Long-Context Corpora
- Success threshold: At least 20% median wall-clock throughput improvement over greedy decoding on repeated natural contexts, no output divergence for greedy decoding, and less than 1% additional peak VRAM versus the target-only baseline.
- Stop condition: Stop if live decoding shows less than 5% throughput improvement or requires material extra VRAM on two natural repeated-context datasets despite trace-level verifier-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/context-local-n-gram-speculative-drafting-with-zero-extra-vram-0da0a6edfc9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
