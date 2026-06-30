# INT2 KV Cache with Per-Layer Outlier Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-kv-cache-with-per-layer-outlier-residual-channel-6d08ec40b4fe`
Run ID: `int2-kv-cache-with-per-layer-outlier-residual-channel-6d08ec40b4fe-20260630T132904439477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5ae17bc3184a

## What looked useful

Outlier residual selection is a real mechanism signal, beating random residuals by roughly 8.5-36.7% attention-error reduction at matched payload, but INT2 plus fp16 residual channels is not competitive with simple INT4 in this bounded probe.

## Boundaries and scale limits

Single GPT-2-small model, synthetic prompt set, no full decode perplexity, no serving kernel, payload bits exclude scale/metadata/packing overhead.

## Claim scope

On GPT-2 KV-cache tensors at seq_len 128 and 512, per-layer mean-absolute outlier residual channels reduce INT2 reconstruction and one-step attention-output error more than random residual channels, but remain far less accurate than plain INT4 at similar payload cost.

## Why it stopped

Bounded direct KV-cache probe found mechanism support against random controls but early practical falsification against an INT4 baseline; this is not full validation or a paper-positive result.

## Recommended next action

Stop this run as no-paper useful-signal evidence; a bounded follow-up should test full decode perplexity with equal-memory INT2 residual variants versus INT4 before any larger serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-memory decode-quality test for low-bit KV residual schemes
- Success threshold: At equal or lower effective KV memory than INT4, the residual scheme should be within 5% relative perplexity of INT4 and reduce attention-output error by at least 80% versus plain INT2.
- Stop condition: Stop if full decode quality remains materially worse than INT4 at equal memory or if metadata/residual overhead removes the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/int2-kv-cache-with-per-layer-outlier-residual-channel-6d08ec40b4fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
