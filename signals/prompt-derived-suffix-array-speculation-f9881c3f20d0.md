# Prompt-Derived Suffix Array Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-derived-suffix-array-speculation-f9881c3f20d0`
Run ID: `prompt-derived-suffix-array-speculation-f9881c3f20d0-20260518T182613624478+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6dcd20e5834b

## What looked useful

Longest-match suffix-array copying accepted about 29.1 of 32 proposed bytes on a mutated repetition positive control, but only 1.09 bytes on the primary natural heldout split; it appears useful as an opportunistic repeated-context copier rather than a general draft model.

## Boundaries and scale limits

Tested only local byte-level corpora up to 24KB prompt and 12KB heldout with a Python suffix-array implementation; no tokenizer, no target model verifier, no GPU serving path, no broad user prompt distribution, and no latency speedup measurement.

## Claim scope

Byte-level local evaluation shows prompt-derived suffix-array copying can produce long accepted proposals when heldout text repeats or lightly mutates prompt-local material, but it is weak on the primary natural heldout split and is not validated as an end-to-end LLM speculative decoder.

## Why it stopped

No-paper useful signal: byte-level proxy supports a narrow repeated-context mechanism but does not provide direct, publication-grade speculative decoding evidence.

## Recommended next action

Do not write a paper from this run; run a bounded token-level verifier experiment on repeated-document/code/log prompts and compare end-to-end accepted tokens and latency against no-draft and fixed n-gram copy baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level verifier test for prompt-local copy speculation
- Success threshold: At least 20% end-to-end latency improvement over no-draft decoding on repeated-context workloads, with no regression on nonrepetitive controls and a clear advantage over fixed n-gram copy baselines.
- Stop condition: Stop if accepted tokens per verifier call remain below 2 or end-to-end latency fails to improve by at least 10% on repeated-context workloads.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-derived-suffix-array-speculation-f9881c3f20d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
