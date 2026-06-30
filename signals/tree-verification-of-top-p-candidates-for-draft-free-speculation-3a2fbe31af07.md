# Tree Verification of Top-p Candidates for Draft-Free Speculation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tree-verification-of-top-p-candidates-for-draft-free-speculation-3a2fbe31af07`
Run ID: `tree-verification-of-top-p-candidates-for-draft-free-speculation-3a2fbe31af07-20260525T185211074718+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f0343368d0fd

## What looked useful

Small branch caps were tractable but accepted less than one token on average in the best latency-relevant settings; wider caps raised coverage but caused complete-tree node counts to explode. The best optimistic latency margins were negative on both distilgpt2 and gpt2.

## Boundaries and scale limits

Tested GPT-2-class models, 16 prompts per model, 32 sampled steps per prompt, p in {0.8, 0.9, 0.95}, branch caps in {2, 4, 8, 16, 32}, depths in {2, 4, 6}. No production tree-attention verifier or 7B+ serving workload was implemented.

## Claim scope

Bounded local mechanism probe on distilgpt2 and gpt2: complete capped trees built from the target model's own top-p candidates did not produce enough accepted sampled tokens to beat an optimistic batched target-evaluation latency proxy.

## Why it stopped

Proxy early falsification: the tested target-only capped top-p tree did not clear optimistic latency break-even, and exact top-p expansion required hundreds to thousands of candidates on average.

## Recommended next action

Stop this draft-free top-p tree path as a no-paper early falsification unless a future project introduces a materially different proposal/pruning mechanism and validates it end-to-end.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tree-verification-of-top-p-candidates-for-draft-free-speculation-3a2fbe31af07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
