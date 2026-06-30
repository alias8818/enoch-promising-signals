# INT2 FFN with Parallel FP32 Residual Adapters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int2-ffn-with-parallel-fp32-residual-adapters-486872bdae11`
Run ID: `int2-ffn-with-parallel-fp32-residual-adapters-486872bdae11-20260603T134912680474+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bfc35e4763c

## What looked useful

Across ranks 4/8/16/32, INT2+adapter reduced INT2-only FFN reconstruction MSE by about 20.5%/26.0%/34.8%/47.2%; rank 32 used about 13.05% effective storage versus dense FP32 FFN.

## Boundaries and scale limits

No full transformer, language-model loss, pretrained activation distribution, real INT2 packing/kernel, latency, throughput, or training-stability validation was performed.

## Claim scope

Synthetic block-level FFN reconstruction only: for d_model=128, d_ff=512 Gaussian inputs and random dense teacher FFNs, a trained parallel FP32 bottleneck adapter added to an INT2-quantized FFN consistently reduced output MSE across three seeds.

## Why it stopped

No-paper closure: the evidence is a synthetic CPU block-level proxy that supports the mechanism but does not validate a model-level architecture or deployment claim.

## Recommended next action

Run a bounded tiny-transformer validation comparing dense FFN, INT2-only FFN, and INT2 FFN plus FP32 adapters on validation loss and wall-clock throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer validation of INT2 FFNs with FP32 residual adapters
- Success threshold: INT2+adapter improves validation loss versus INT2-only by at least 25% of the dense-vs-INT2 degradation while keeping effective FFN storage at or below 20% of dense FP32.
- Stop condition: Stop if INT2+adapter fails to improve validation loss over INT2-only by at least 10% of the dense-vs-INT2 degradation for two adapter ranks, or if training cost exceeds the local bounded budget.

## Evidence references

- Artifact root: `<local-path>/projects/int2-ffn-with-parallel-fp32-residual-adapters-486872bdae11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
