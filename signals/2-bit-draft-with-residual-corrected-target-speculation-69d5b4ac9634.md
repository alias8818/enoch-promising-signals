# 2-bit Draft with Residual-Corrected Target Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634`
Run ID: `2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634-20260523T113045486686+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

Residual correction is a real mechanism signal because it improves acceptance and KL beyond temperature-only calibration, but the corrected naive 2-bit draft still has 0 target top-1 agreement, total variation 0.889, and only 11.1% expected acceptance.

## Boundaries and scale limits

Small pretrained model, single corpus, deterministic bounded split, single-token distributional proxy, no end-to-end speculative decoding throughput, naive uniform 2-bit whole-model quantization, and global vocab-bias residual rather than context-conditioned correction.

## Claim scope

On distilgpt2 over 80 held-out Tiny Shakespeare contexts, a global residual correction of a naive per-tensor whole-model 2-bit draft improves the one-token speculative acceptance proxy from 0.0000053 to 0.1108312 and KL target||draft from 81.1432 to 6.4967, but remains too inaccurate for practical speculation.

## Why it stopped

Proxy/local early falsification for the naive version: residual correction helps distributional metrics but does not make this 2-bit draft practically viable; this is not a full validation.

## Recommended next action

Run a bounded deepen test with a context-conditioned residual adapter and a groupwise/weight-only 2-bit draft; stop if held-out expected acceptance remains below 0.4 or if actual speculative decoding fails to beat target-only wall-clock throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Context-conditioned residual adapter for 2-bit draft speculation
- Success threshold: Held-out expected one-token acceptance above 0.4, nonzero target top-1 agreement above 0.2, and actual speculative decoding wall-clock speedup above 1.1x after draft and correction overhead.
- Stop condition: Stop as negative if acceptance remains below 0.4 or measured end-to-end speedup is at or below 1.0x on the bounded model/corpus.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
