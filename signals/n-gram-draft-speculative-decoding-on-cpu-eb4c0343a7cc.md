# N-Gram Draft Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-draft-speculative-decoding-on-cpu-eb4c0343a7cc`
Run ID: `n-gram-draft-speculative-decoding-on-cpu-eb4c0343a7cc-20260609T001144377096+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/aa358701de54

## What looked useful

Best trace result reached only 1.193 tokens per target call; best measured CPU proxy speedup was 0.446x, so verification overhead dominated saved target calls.

## Boundaries and scale limits

This run did not benchmark a real transformer, tokenizer, KV cache, or production serving stack. It used held-out text as the acceptance oracle and matrix multiplication as a CPU target-cost proxy.

## Claim scope

On a 60k-token Pride and Prejudice word/punctuation trace with deterministic n-gram drafts and measured NumPy CPU target-cost proxy, n-gram drafting reduced target-call count only modestly and was slower than baseline after verification work.

## Why it stopped

Proxy/early falsification: deterministic n-gram acceptance was too low on held-out natural language and measured CPU verification was slower than baseline, but this is not a full transformer validation.

## Recommended next action

Stop this run as a proxy early falsification; run one bounded direct small-LM CPU benchmark only if a real-model confirmation is needed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-LM CPU speculative decoding benchmark for n-gram drafts
- Success threshold: Speculative decoding must improve end-to-end median tokens/s by at least 10% over cached baseline while preserving sampled-token equivalence under the chosen verification rule.
- Stop condition: Stop if the best real-model configuration is below 1.0x baseline tokens/s or if acceptance stays below 1.5 emitted tokens per target verification call on natural-language prompts.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-cpu-eb4c0343a7cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
