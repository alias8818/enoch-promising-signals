# Small-LM Decode Validation for 2-Bit Per-Head KV Codebooks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-lm-decode-validation-for-2-bit-per-head-kv-codebooks-27760f3237`
Run ID: `small-lm-decode-validation-for-2-bit-per-head-kv-codebooks-27760f3237-20260605T153846458002+0000`

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

- Parent run decision: 2-Bit KV Cache with Per-Head Codebooks: enoch://control-plane/projects/2-bit-kv-cache-with-per-head-codebooks-5ebf8a76fc52/runs/2-bit-kv-cache-with-per-head-codebooks-5ebf8a76fc52-20260604T184633036860+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3c542971de2e

## What looked useful

Learned 2-bit per-head codebooks achieved about 7.95x estimated cache compression and reduced relative cache MSE to 0.0133 versus 0.1073 for random codebooks, but added +1.383 NLL versus full precision and preserved only 42.9% full-precision top-1 agreement.

## Boundaries and scale limits

32 samples, 64-token prompts, 32-token continuations, 1024 decode steps; distilgpt2 only; scalar k-means codebooks only; estimated packed-cache size only, no packed GPU kernel or serving throughput measurement.

## Claim scope

Tier 1 direct decode test on distilgpt2 with Wikitext-2 prompts: scalar 2-bit per-head KV codebooks are meaningfully better than random same-bit codebooks but are not close enough to full-precision KV cache behavior to support drop-in decode quality.

## Why it stopped

Tier 1 direct validation found mechanism support versus random control but a large full-precision decode-quality gap, so the current scalar 2-bit per-head codebook idea is not paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; deepen only if testing a specific improved 2-bit design that targets <= +0.30 NLL delta while retaining >= 7x estimated cache compression on the same direct decode benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual or vector 2-bit per-head KV codebooks for small-LM decode
- Success threshold: Improved 2-bit design has <= +0.30 NLL delta versus full precision, at least 70% full-precision top-1 agreement, and >= 7x estimated cache compression, while outperforming scalar 2-bit on NLL and KL.
- Stop condition: Stop if the improved 2-bit design still has > +0.75 NLL delta or < 55% top-1 agreement on the same benchmark, because that would indicate 2-bit quality remains too lossy for this small-LM decode setting.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-decode-validation-for-2-bit-per-head-kv-codebooks-27760f3237`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
