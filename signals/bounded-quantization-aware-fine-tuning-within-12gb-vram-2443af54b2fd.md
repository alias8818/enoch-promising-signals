# Bounded Quantization-Aware Fine-Tuning Within 12GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-quantization-aware-fine-tuning-within-12gb-vram-2443af54b2fd`
Run ID: `bounded-quantization-aware-fine-tuning-within-12gb-vram-2443af54b2fd-20260613T214928947083+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

QAT stayed within the bounded memory target and optimized nearly as well as dense in short probes, but it did not materially reduce training memory and slowed throughput by about 27-30%. This supports feasibility of bounded fake-QAT mechanics, not a paper-ready claim.

## Boundaries and scale limits

Evidence is synthetic, short-horizon, single-seed, and not based on a pretrained public model or real validation set. The implementation uses fake quantization and keeps FP parameters, gradients, activations, and AdamW states resident, so it does not validate true low-bit optimizer-state or checkpoint memory savings.

## Claim scope

Straight-through fake-quantized QAT fine-tuning ran successfully under a 12 GiB CUDA allocator budget for synthetic causal language-model probes up to 310,962,176 parameters, batch size 4, sequence length 256, BF16 autocast, and AdamW on NVIDIA GB10.

## Why it stopped

Synthetic short-horizon proxy evidence is useful but insufficient for publication-grade validation; fake QAT did not show memory savings over dense training because optimizer and parameter storage remained full precision.

## Recommended next action

Stop this run as no-paper useful evidence; next run should fine-tune a pretrained GPT-2-small-class model on a public language dataset under the same 12 GiB allocator cap with dense BF16, fake-QAT, and LoRA/QLoRA-style controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2-small 12GB QAT versus dense and LoRA controls
- Success threshold: Fake-QAT completes under 12 GiB reserved memory, reaches validation perplexity within 5% of dense BF16 at the same token budget, and provides a clearly better accuracy-memory or accuracy-throughput tradeoff than at least one bounded control.
- Stop condition: Stop if fake-QAT exceeds 12 GiB, is more than 10% worse in validation perplexity than dense BF16 after the planned token budget, or remains slower without any memory or quality advantage over bounded controls.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-quantization-aware-fine-tuning-within-12gb-vram-2443af54b2fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
