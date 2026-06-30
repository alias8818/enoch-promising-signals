# N-Gram Speculative Drafting for 2x CPU Inference Speedup

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `n-gram-speculative-drafting-for-2x-cpu-inference-speedup-3f57b9827ef5`
Run ID: `n-gram-speculative-drafting-for-2x-cpu-inference-speedup-3f57b9827ef5-20260604T221041021846+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/78b7f7db23db

## What looked useful

Across 96 confirmation configurations, best modeled speedup was 1.129x on Alice and 1.055x on Tiny Shakespeare. Best optimistic zero-overhead target-call reduction was 1.327x, still below the 2x target. Longer drafts improved call reduction slightly but reduced modeled speedup once verifier overhead was included.

## Boundaries and scale limits

Not a real transformer LLM benchmark; no BPE tokenizer, no KV-cache kernels, no production CPU serving stack, and only two small text corpora. The result is an early falsification for the tested mechanism, not a universal claim about all n-gram speculative decoding implementations.

## Claim scope

Bounded proxy over two public text corpora using regex tokenization, a 5-gram target model, 1- to 4-gram drafters, draft lengths 2/4/8/12, and verifier overhead alpha 0.05/0.10/0.20. Within this setting, n-gram speculative drafting did not approach 2x CPU inference speedup.

## Why it stopped

Proxy early falsification rather than full validation: the local n-gram corpus replay did not meet the 2x threshold, with best modeled speedup 1.129x and best zero-overhead target-call speedup 1.327x.

## Recommended next action

Stop this project as a no-paper bounded negative; only revisit with a real CPU LLM/BPE verifier benchmark if a specific implementation claims much higher acceptance or near-zero marginal verification cost.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-drafting-for-2x-cpu-inference-speedup-3f57b9827ef5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
