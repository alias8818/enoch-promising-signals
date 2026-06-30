# KV-cache-aware n-gram speculative decoding for realistic local inference prompts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-aware-n-gram-speculative-decoding-for-realistic-l-3a15ad966e`
Run ID: `kv-cache-aware-n-gram-speculative-decoding-for-realistic-l-3a15ad966e-20260526T124841470640+0000`

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

- Parent run decision: N-gram Speculative Draft for Local Inference: enoch://control-plane/projects/n-gram-speculative-draft-for-local-inference-fdf423905c1f/runs/n-gram-speculative-draft-for-local-inference-fdf423905c1f-20260526T013821480154+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fe9efb9df68

## What looked useful

Prompt-suffix n-gram speculative decoding exactly matched greedy token IDs on all tested GPT-2 prompts. On repeated prompts, draft length 4 accepted 347/402 proposed tokens, reduced target forward calls by 62.2%, and ran at 0.411x baseline latency; draft length 8 accepted 348/454 proposed tokens, reduced calls by 73.2%, and ran at 0.283x baseline latency. A lower-repeat control had much lower acceptance and smaller speedup, supporting the repeat-exploitation mechanism.

## Boundaries and scale limits

Small model, greedy-only decoding, 8 repeated prompts plus 4 lower-repeat controls, single local process, Hugging Face cache path, no production serving backend, no 7B-class model, no sampling, no concurrency.

## Claim scope

Tier 1 controlled local inference test: GPT-2 small greedy decoding on 8 repeated operational/code/markdown prompts, comparing baseline KV-cache greedy decoding to prompt-suffix n-gram speculative block verification with exact token equivalence.

## Why it stopped

Tier 1 direct test produced useful mechanism support but not publication-grade evidence; closing as no-paper useful signal under the strict paper gate.

## Recommended next action

Run a bounded deepen follow-up on a 7B-class local model and real serving backend with the same exact-output metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 7B serving-backend validation of KV-cache-aware n-gram speculative decoding
- Success threshold: At least 95% exact-run completion with exact greedy token equivalence, at least 35% mean target forward-call reduction, and at least 20% median latency improvement on repeated realistic prompts, with the lower-repeat control showing materially lower acceptance.
- Stop condition: Stop if exact token equivalence fails, if mean forward-call reduction is below 15%, or if serving-backend cache management overhead eliminates latency improvement despite accepted drafts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-n-gram-speculative-decoding-for-realistic-l-3a15ad966e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
