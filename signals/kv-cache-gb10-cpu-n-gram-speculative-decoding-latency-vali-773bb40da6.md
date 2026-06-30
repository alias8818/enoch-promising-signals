# KV-cache GB10 CPU n-gram speculative decoding latency validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-gb10-cpu-n-gram-speculative-decoding-latency-vali-773bb40da6`
Run ID: `kv-cache-gb10-cpu-n-gram-speculative-decoding-latency-vali-773bb40da6-20260607T213552145749+0000`

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

- Parent run decision: CPU N-Gram Draft Speculative Decoding for GB10 Inference: enoch://control-plane/projects/cpu-n-gram-draft-speculative-decoding-for-gb10-inference-23f19b41f141/runs/cpu-n-gram-draft-speculative-decoding-for-gb10-inference-23f19b41f141-20260607T180015216903+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/98febe24a9fe

## What looked useful

Corrected direct runs preserved exact greedy token equality. In the accepting condition, speculative decoding reduced target forwards from 97 to 28 for 96 generated tokens and improved warm mean latency by about 2.65x. In the non-accepting condition, accepted drafts were zero and warm speedup was about 0.99x.

## Boundaries and scale limits

Tier 1 small direct test only: one small Hugging Face model, two hand-selected prompts, Python reference implementation, greedy decoding only, no large model serving stack and no broad prompt distribution.

## Claim scope

On GB10 with distilgpt2 greedy decoding, CPU n-gram speculative drafting can reduce latency when generated continuations are locally repetitive and drafts match the target model, but it provides no general speedup when the draft acceptance rate is zero.

## Why it stopped

Small direct validation produced mixed conditional evidence rather than publication-grade support for a general GB10 latency claim.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a bounded prompt-suite test on a larger local model only if the controller wants broader direct evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-suite acceptance and latency test for CPU n-gram speculative decoding on a larger local model
- Success threshold: Exact token equality for all prompts, p50 speedup >= 1.2x on the high-acceptance subset, and p95 slowdown <= 5 percent on the low-acceptance subset.
- Stop condition: Stop if exact token equality fails, if high-acceptance prompts do not reach 1.2x p50 speedup, or if low-acceptance prompts exceed 5 percent p95 slowdown.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-gb10-cpu-n-gram-speculative-decoding-latency-vali-773bb40da6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
