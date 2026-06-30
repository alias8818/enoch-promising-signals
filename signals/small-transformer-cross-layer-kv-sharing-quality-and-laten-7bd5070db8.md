# Small-transformer cross-layer KV sharing quality and latency check

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-cross-layer-kv-sharing-quality-and-laten-7bd5070db8`
Run ID: `small-transformer-cross-layer-kv-sharing-quality-and-laten-7bd5070db8-20260523T175504481625+0000`

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

- Parent run decision: Cross-layer KV sharing cuts CPU RAM: enoch://control-plane/projects/cross-layer-kv-sharing-cuts-cpu-ram-b8fed4815209/runs/cross-layer-kv-sharing-cuts-cpu-ram-b8fed4815209-20260523T173334565225+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ba0aaaf3c26

## What looked useful

Shared-pair KV reduced parameters by 7.53% and worsened validation loss by only 1.28%, but cleaned single-thread cached decode speedup was 8.91%, below the 10% success threshold.

## Boundaries and scale limits

Small CPU-only direct test: about 0.49M baseline parameters, byte-level text, short training budget, no fused inference kernel, no GPT-2-small-class or web-scale tokenized validation.

## Claim scope

In a 4-layer, d_model=96 byte-level CPU PyTorch transformer trained for 300 steps on Tiny Shakespeare across 3 seeds, adjacent-layer KV sharing preserved validation loss within the 3% threshold but did not reach the predefined 10% cached decode speedup threshold.

## Why it stopped

Controlled small direct test completed; quality support was positive but latency missed the predefined threshold, so this is not a paper-positive result.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should use a larger small transformer or fused one-cache-per-pair inference path and require both <=3% validation-loss degradation and >=10% cached decode speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger-width or fused-cache KV sharing latency confirmation
- Success threshold: Shared-pair KV validation loss <=3% worse than baseline and cached decode tokens/s >=10% faster on the cleaned benchmark across matched seeds.
- Stop condition: Stop if validation loss is >3% worse or cleaned cached decode speedup remains <10%, since that would reproduce the current no-paper latency limitation.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-cross-layer-kv-sharing-quality-and-laten-7bd5070db8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
