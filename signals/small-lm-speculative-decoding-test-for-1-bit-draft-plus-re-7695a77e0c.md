# Small-LM speculative decoding test for 1-bit draft plus residual channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-lm-speculative-decoding-test-for-1-bit-draft-plus-re-7695a77e0c`
Run ID: `small-lm-speculative-decoding-test-for-1-bit-draft-plus-re-7695a77e0c-20260527T024915084051+0000`

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

- Parent run decision: 1-bit draft with residual channel for speculation: enoch://control-plane/projects/1-bit-draft-with-residual-channel-for-speculation-cf0507322e10/runs/1-bit-draft-with-residual-channel-for-speculation-cf0507322e10-20260524T193223217261+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3865595438b

## What looked useful

Residual adapters consistently raised binary draft acceptance by a mean +0.00326 absolute and lowered KL by a mean -0.00397 versus binary-only across seeds 7/17/29, but the dense draft remained about +0.05195 acceptance ahead and the measured-cost speed proxy for binary+residual was only 0.977x because the residual channel increased draft forward cost.

## Boundaries and scale limits

Small synthetic token stream only; small transformer target and drafts only; no natural-language corpus; no GPT-2-small-class baseline; no production speculative decoding loop; binary and residual layers are naive PyTorch modules rather than optimized kernels.

## Claim scope

On a controlled small synthetic language-model task, a rank-8 full-precision residual channel added to a 1-bit binary-weight draft improved target-to-draft KL and mean speculative acceptance probability versus a binary-only draft across three seeds, but did not produce a measured-cost speed win.

## Why it stopped

Tier 1 direct small test produced useful mechanism support but no practical speed win and no publication-grade evidence.

## Recommended next action

Run a bounded deepen test with an optimized or lower-rank residual path and a real speculative decoding loop; stop unless binary+residual beats binary-only on acceptance and achieves a measured end-to-end speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cost-aware residual channel ablation for 1-bit speculative drafts
- Success threshold: Binary+residual must improve mean acceptance over binary-only by at least +0.003 absolute and achieve at least 1.05x measured end-to-end speculative decoding speedup with no worse KL than binary-only.
- Stop condition: Stop if every residual rank either loses the acceptance/KL improvement or raises measured draft cost enough to keep end-to-end speedup at or below binary-only.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-speculative-decoding-test-for-1-bit-draft-plus-re-7695a77e0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
