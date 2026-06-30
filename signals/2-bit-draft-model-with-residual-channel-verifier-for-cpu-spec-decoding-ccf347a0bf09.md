# 2-bit Draft Model with Residual-Channel Verifier for CPU Spec Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-draft-model-with-residual-channel-verifier-for-cpu-spec-decoding-ccf347a0bf09`
Run ID: `2-bit-draft-model-with-residual-channel-verifier-for-cpu-spec-decoding-ccf347a0bf09-20260629T090452039368+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66965a9ddd71

## What looked useful

Residual-channel policy mattered: target_toplogit residuals at 64 entries per row improved expected acceptance from 0.7366 to 0.8072 and top-1 agreement from 0.0947 to 1.0 at 4.41x fp16-logit compression; absolute-error residuals were much weaker, reaching only 0.7593 expected acceptance and 0.1104 top-1 agreement.

## Boundaries and scale limits

No trained language model, tokenizer, natural text corpus, or end-to-end CPU decoder was tested. Timing covers NumPy row scoring only, not autoregressive KV-cache behavior or verifier scheduling.

## Claim scope

On a deterministic synthetic 1024-token transition model, a row-wise 2-bit draft distribution plus a sparse probability-aware residual channel improved speculative acceptance versus 2-bit draft-only while retaining at least 4x compression versus fp16 logits.

## Why it stopped

Proxy-only useful signal: the synthetic transition-model evidence supports the mechanism direction but is insufficient for paper-positive claims about CPU speculative decoding.

## Recommended next action

Run a bounded real-model CPU follow-up with a small transformer or GPT-2-small-class baseline, comparing dense draft, 2-bit draft-only, and 2-bit plus probability-aware residual verifier on real prompts with measured tokens/sec and acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of probability-aware residual verifier for 2-bit speculative draft decoding
- Success threshold: At least +5 absolute percentage points acceptance over 2-bit draft-only and at least 1.10x end-to-end CPU tokens/sec over the dense draft baseline at comparable output quality on the fixed prompt suite.
- Stop condition: Stop if the residual variant fails to improve acceptance by 3 absolute percentage points over 2-bit draft-only or loses end-to-end CPU throughput versus dense draft on the smoke prompt suite.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-draft-model-with-residual-channel-verifier-for-cpu-spec-decoding-ccf347a0bf09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
