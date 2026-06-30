# GPT-2-small async LoRA plus sparse residual over 2-bit quantized layers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-async-lora-plus-sparse-residual-over-2-bit-qua-2165261859`
Run ID: `gpt-2-small-async-lora-plus-sparse-residual-over-2-bit-qua-2165261859-20260621T082323109428+0000`

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

- Parent run decision: Home distributed LoRA + residual training over 2-bit base on volunteer nodes: enoch://control-plane/projects/home-distributed-lora-residual-training-over-2-bit-base-on-volunteer-nodes-5385408ed3fd/runs/home-distributed-lora-residual-training-over-2-bit-base-on-volunteer-nodes-5385408ed3fd-20260621T080411923410+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/114ecde8251c

## What looked useful

LoRA recovered mean eval loss by 0.539 over frozen 2-bit GPT-2-small. Sparse residual added repeatable but small gains: synchronous sparse improved mean final loss by 0.034 over LoRA-only, while async sparse improved by 0.016 but lagged synchronous sparse.

## Boundaries and scale limits

Only 80 adapter steps, two seeds, one corpus, one LoRA rank, one sparse density, one async period, float32 CUDA training, dequantized 2-bit weights rather than packed int2 kernels, and no long-run or downstream validation.

## Claim scope

Two-seed Tier 1 GPT-2-small adapter test on Wikitext-2 slices: frozen 2-bit quantized GPT-2 Conv1D weights with rank-4 LoRA, 0.1% quantization-error-targeted sparse residual, and async LoRA updates every second step.

## Why it stopped

No-paper useful signal: the mechanism improves over LoRA-only in a small direct GPT-2-small test, but the async variant is only modestly better than LoRA-only and worse than synchronous sparse residual, so publication-grade support is absent.

## Recommended next action

Run a bounded deepen follow-up with at least 3 seeds, 300-500 adapter steps, a small density/async-period sweep, and an explicit update-cost metric to test whether async sparse residual has a real advantage over synchronous sparse residual.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer GPT-2-small density and async-period sweep for sparse residual over 2-bit layers
- Success threshold: Async sparse residual must beat LoRA-only by at least 0.03 eval loss on mean across seeds and match synchronous sparse residual within 0.01 eval loss while using fewer LoRA update steps or showing a stability advantage.
- Stop condition: Stop if async sparse residual fails to beat LoRA-only by 0.03 mean eval loss or remains worse than synchronous sparse residual by more than 0.01 after the planned 300-500 step budget.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-async-lora-plus-sparse-residual-over-2-bit-qua-2165261859`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
