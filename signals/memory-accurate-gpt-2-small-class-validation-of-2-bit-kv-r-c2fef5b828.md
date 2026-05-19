# Memory-accurate GPT-2-small-class validation of 2-bit KV residual correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-accurate-gpt-2-small-class-validation-of-2-bit-kv-r-c2fef5b828`
Run ID: `memory-accurate-gpt-2-small-class-validation-of-2-bit-kv-r-c2fef5b828-20260514T120836781858+0000`

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

- Internal Enoch project: Memory-accurate GPT-2-small-class validation of 2-bit KV residual correction: internal_generated:memory-accurate-gpt-2-small-class-validation-of-2-bit-kv-r-c2fef5b828

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct GPT-2-small validation supports the residual-window mechanism but not publication readiness: naive 2-bit KV is unusable, residual windows repair much of the loss, and the best tested useful tradeoffs still leave either a 20.2% perplexity increase at 4.78x simulated KV compression or only 1.73x compression at a 6.6% perplexity increase. Packed int2 storage was memory-accounted but not physically implemented in the attention kernel.

## Recommended next action

Stop this paper path for this run; only continue via a bounded packed-int2 KV attention follow-up requiring at least 3x measured KV memory reduction with no more than 5% perplexity increase versus fp16.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed int2 KV residual-window validation with measured memory
- Success threshold: At least one residual-corrected packed int2 configuration reaches >=3x measured KV memory reduction versus fp16 KV with <=5% perplexity increase on fixed-seed GPT-2-small-class validation, while naive int2 remains a worse control.
- Stop condition: Finalize negative if packed-cache implementation cannot be completed locally or if all tested residual windows miss either the >=3x measured KV memory reduction or <=5% perplexity increase threshold.

## Evidence references

- Artifact root: `<local-path>/projects/memory-accurate-gpt-2-small-class-validation-of-2-bit-kv-r-c2fef5b828`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
