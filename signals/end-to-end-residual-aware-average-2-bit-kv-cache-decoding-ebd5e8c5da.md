# End-to-end residual-aware average-2-bit KV cache decoding probe

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `end-to-end-residual-aware-average-2-bit-kv-cache-decoding-ebd5e8c5da`
Run ID: `end-to-end-residual-aware-average-2-bit-kv-cache-decoding-ebd5e8c5da-20260524T190344444889+0000`

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

- Parent run decision: Residual-Channel-Aware 2-bit KV Cache Compression for Long Context: enoch://control-plane/projects/residual-channel-aware-2-bit-kv-cache-compression-for-long-context-59ccd1fff678/runs/residual-channel-aware-2-bit-kv-cache-compression-for-long-context-59ccd1fff678-20260524T161925398195+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c558e37ba4a

## What looked useful

Residual-aware recent-token windows monotonically reduced naive 2-bit NLL damage on GPT-2, but the 4-token window still caused 26.65% NLL/token degradation and 77.60% top-1 agreement versus fp cache; even a 16-token window missed the <=5% NLL degradation target while costing 6.67 payload bits/value on a 48-token context.

## Boundaries and scale limits

Tested GPT-2 small only, 12 local text passages, 576 teacher-forced tokens, dense dequantized Hugging Face attention path, payload-bit accounting excludes metadata and storage overhead, no long-context serving kernel or large-model benchmark.

## Claim scope

Small direct GPT-2 teacher-forced decoding test: residual-window 2-bit KV cache mutation improves over naive 2-bit cache but does not preserve fp-cache next-token behavior under the stated threshold.

## Why it stopped

Controlled small direct test failed the stated preservation threshold, although it showed residual-window mechanism support relative to naive 2-bit.

## Recommended next action

Stop this run as no-paper useful signal; only revisit with a different residual coding scheme that keeps average bits near 2 while directly targeting <=5% NLL degradation and >=95% top-1 agreement.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Error-feedback residual coding for near-2-bit KV cache decoding
- Success threshold: At <=2.5 effective bits/value including metadata on the 48-token setup, achieve <=10% NLL/token degradation versus fp cache, >=90% top-1 agreement, and >=50% relative NLL-degradation reduction versus naive 2-bit.
- Stop condition: Stop if metadata-aware effective bits exceed 2.5 or if NLL degradation remains above 20% on GPT-2 after one implemented residual-coding variant.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-residual-aware-average-2-bit-kv-cache-decoding-ebd5e8c5da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
